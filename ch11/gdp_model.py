from pyomo.gdp import Disjunct, Disjunction
import pyomo.environ as pyo


model = pyo.AbstractModel()

model.NumTimePeriods = pyo.Param()
model.GENERATORS = pyo.Set()
model.TIME = pyo.RangeSet(model.NumTimePeriods)

model.MaxPower = pyo.Param(model.GENERATORS, within=pyo.NonNegativeReals)
model.MinPower = pyo.Param(model.GENERATORS, within=pyo.NonNegativeReals)
model.RampUpLimit = pyo.Param(model.GENERATORS, within=pyo.NonNegativeReals)
model.RampDownLimit = pyo.Param(model.GENERATORS, within=pyo.NonNegativeReals)
model.StartUpRampLimit = pyo.Param(model.GENERATORS, within=pyo.NonNegativeReals)
model.ShutDownRampLimit = pyo.Param(model.GENERATORS, within=pyo.NonNegativeReals)

def Power_bound(m, g, t):
    return (0, m.MaxPower[g])
model.Power = pyo.Var(model.GENERAOTR, model.TIME, bounds=Power_bound)

def GenOn(b, g, t):
    m = b.model()
    b.power_limit = pyo.Constraint(
        expr=pyo.inequality(m.MinPower[g], m.Power[g, t], m.MaxPower[g])
    )
    if t == m.TIME.first():
        return
    b.ramp_limit = pyo.Constraint(
        expr=pyo.inequality(-m.RampDownLimit[g], m.Power[g, t] - m.Power[g, t-1], m.RampUplimit[g])
    )
model.GenOn = Disjunct(model.GENERATORS, model.TIME, rule=GenOn)

def GenOff(b, g, t):
    m = b.model()
    b.power_limit = pyo.Constraint(
        expr=m.Power[g, t] == 0
    )
    if t == m.TIME.first():
        return
    b.ramp_limit = pyo.Constraint(
        expr=m.Power[g, t-1] <= m.StartUpRampLimit[g]
    )
model.GenOff = Disjunct(model.GENERATORS, model.TIME, rule=GenOff)

def GenStartUp(b, g, t):
    m = b.model()
    b.power_limit = pyo.Constraint(
        expr=m.Power[g, t] <= m.StartUpRampLimit[g]
    )
model.GenStartUp = Disjunct(model.GENERATORS, model.TIME, rule=GenStartUp)


def bind_generators(m, g, t):
    return [m.GenOn[g, t], m.GenOff[g, t], m.GenStartup[g,t]]
model.bind_generators = Disjunction(model.GENERATORS, model.TIME, rule=bind_generators)

def onState(m, g, t):
    if t == m.TIME.first():
        return pyo.LogicalConstraint.Skip
    return m.GenOn[g, t].indicator_var.implies(
            pyo.lor(m.GenOn[g, t-1].indicator_var,m.GenStartup[g, t-1].indicator_var)
    )
model.onState = pyo.LogicalConstraint(model.GENERATORS, model.TIME, rule=onState)

def startupState(m, g, t):
    if t == m.TIME.first():
        return pyo.LogicalConstraint.Skip
    return m.GenStartUp[g, t].indicator_var.implies(m.GenOff[g, t-1].indicator_var)
model.startupState = pyo.LogicalConstraint(model.GENERATORS, model.TIME, rule=startupState)



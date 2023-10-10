import pyomo.environ as pyo

model = pyo.ConcreteModel()

# expr
model.x = pyo.Var([1, 2], initialize=1.0)
model.diff = pyo.Constraint(expr=model.x[2] - model.x[1] <= 7.5)

# rule
model.x = pyo.Var([1, 2], initialize=1.0)

def diff_rule(model):
    return model.x[2] - model.x[1] <= 7.5
model.diff = pyo.Constraint(rule=diff_rule)

# constraint can be indexed
N = [1, 2, 3]

a = {1:1, 2: 3.1, 3: 4.5}
b = {1:1, 2: 2.9, 3: 3.1}

model = pyo.ConcreteModel()

model.y = pyo.Var(N, within=pyo.NonNegativeReals, initialize=1.0)

def CoverConstr_rule(model, i):
    return a[i] * model.u[i] >= b[i]
model.CoverConstr = pyo.ConcreteModel(N, rule=CoverConstr_rule)

# no Constrain

model = pyo.ConcreteModel()
TimePeriods = [1, 2, 3, 4, 5]
LastTimePeriod = 5

model.StartTime = pyo.Var(TimePeriods, initialize=1.0)

def Pred_rule(model, t):
    if t == LastTimePeriod:
        return pyo.Constraint.Skip
    else:
        return model.StartTime[t] <= model.StartTime[t + 1]

model.Pred = pyo.Constraint(TimePeriods, rule=Pred_rule)

# scont.py
import pyomo.environ as pyo
from pyomo.gdp import Disjunct, Disjunction

L = [1,2,3]
U = [2,4,6]
index = [0,1,2]

model = pyo.ConcreteModel()
model.x = pyo.Var(index, within=pyo.Reals, bounds=(0,20))
model.x_nonzero = pyo.Var(index, bounds=(0,1))
# Each disjunction is a semi-continuous variable
# x[k] == 0 or L[k] <= x[k] <= U[k]
def d_0_rule(d, k):
    m = d.model()
    d.c = pyo.Constraint(expr=m.x[k] == 0)
model.d_0 = Disjunct(index, rule=d_0_rule)

def d_nonzero_rule(d, k):
    m = d.model()
    d.c = pyo.Constraint(expr=pyo.inequality(L[k], m.x[k], U[k]))
    d.count = pyo.Constraint(expr=m.x_nonzero[k] == 1)
model.d_nonzero = Disjunct(index, rule=d_nonzero_rule)

def D_rule(m, k):
    return [m.d_0[k], m.d_nonzero[k]]
model.D = Disjunction(index, rule=D_rule)

# Minimize the number of x variables that are nonzero
model.o = pyo.Objective(expr=sum(model.x_nonzero[k] for k in index))
# Satisfy a demand that is met by these variables
model.c = pyo.Constraint(expr=sum(model.x[k] for k in index) >= 7)

# There are three ways to apply either the Big-M or Hull transformation to solve
# this model:
# 1. through the pyomo command line,
# 2. through a scripting interface, or
# 3. through a BuildAction.

# 1、
# pyomo solve scont.py --transform gdp.bigm --solver=glpk

# 2、script
# xfrm = pyo.TransformationFactory('gdp.bigm')
# xfrm.apply_to(model)

# solver = pyo.SolverFactory('glpk')
# status = solver.solve(model)
# model.pprint()

# 3、buildAction
def transform_gdp(m):
    xfrm = pyo.TransformationFactory('gdp.bigm')
    xfrm.apply_to(m)

model.transform_gdp = pyo.BuildAction(rule=transform_gdp)
model.pprint()


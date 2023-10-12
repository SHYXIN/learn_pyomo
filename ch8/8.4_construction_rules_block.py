import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.P = pyo.Param(initialize=3)
model.T = pyo.RangeSet(model.P)

def xyb_rule(b, t):
    b.x = pyo.Var()
    b.I = pyo.RangeSet(t)
    b.y = pyo.Var(b.I)
    b.c = pyo.Constraint(expr=b.x == 1 - sum(b.y[i] for i in b.I))

model.xyb = pyo.Block(model.T, rule=xyb_rule)

for t in model.T:
    print(model.xyb[t].c.body)


import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.P = pyo.Param(initialize=3)
model.T = pyo.RangeSet(model.P)

def xyb_rule(b, t):
    b.x = pyo.Var()
    b.I = pyo.RangeSet(t)
    b.y = pyo.Var(b.I, initialize=1.0)
    def _b_c_rule(_b):
        return _b.x == 1.0 - sum(_b.y[i] for i in _b.I)
    b.c = pyo.Constraint(rule=_b_c_rule)

model.xyb = pyo.Block(model.T, rule=xyb_rule)

for t in model.T:
    print(model.xyb[t].c.body)


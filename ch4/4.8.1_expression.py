import pyomo.environ as pyo

model = pyo.ConcreteModel()

# create a single,non-indexed Expression object
model.e = pyo.Expression()

# expr or rule keywords can be used to initialize a named expression
model.x = pyo.Var()
model.el = pyo.Expression(expr=model.x+1)
def e2_rule(model):
    return model.x + 1
model.e2 = pyo.Expression(rule=e2_rule)

N = [1, 2, 3]
model.x = pyo.Var()
def e_rule(model, i):
    if i == 1:
        return pyo.Expression.Skip
    else:
        return model.x[i] ** 2
model.e = pyo.Expression(N, rule=e_rule)

import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x = pyo.Var(initialize=1.0)
model.y = pyo.Var(initialize=1.0)

model.c1 = pyo.Constraint(expr=model.y - model.x <= 7.5)
model.c2 = pyo.Constraint(expr=-2.5 <= model.y - model.x)
model.c3 = pyo.Constraint(
    expr=pyo.inequality(-3.0, model.y - model.x, 7.0)
)
# body lslack  uslack

print(pyo.value(model.c1.body))  # 0.0 = 1 - 1

print(model.c1.body())
print(model.c1.lslack())  # inf  body减去下限
print(model.c1.uslack())  # 7.5  上限减去body

print(model.c2.lslack())  # 2.5
print(model.c2.uslack())  # inf

print(model.c3.lslack())  # 3.0
print(model.c3.uslack())  # 7.0

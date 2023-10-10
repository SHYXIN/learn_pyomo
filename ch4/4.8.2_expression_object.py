import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x = pyo.Var()
model.e = pyo.Expression(expr=(model.x - 1.0) **2)
model.o = pyo.Objective(expr=0.1*model.e + model.x)
model.c = pyo.Constraint(expr=model.e <= 1.0)

# named expression and update name
model.x.set_value(2.0)
print(pyo.value(model.e))       # 1.0
print(pyo.value(model.c.body))   # 1.0

model.e.set_value((model.x - 2.0) **2)
print(pyo.value(model.e))  # 0.0
print(pyo.value(model.o))  # 2.0
print(pyo.value(model.c.body))  # 0.0

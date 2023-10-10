import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.A = pyo.Set(initialize=[1, 2, 3])
model.B = pyo.Set(initialize=['Q', 'R'])
model.x = pyo.Var()
model.y = pyo.Var()
model.o = pyo.Objective(expr=model.x)
model.c = pyo.Constraint(expr=model.x >= 0)

def d_rule(model, a):
    return a * model.x <= 0
model.d = pyo.Constraint(model.A, rule=d_rule)

# ---------
model.x = pyo.Var(initialize=3.14)
# -----------
model.A = pyo.Set(initialize=[1, 2, 3])
model.x = pyo.Var(model.A, initialize=3.14)
model.y = pyo.Var(model.A, initialize={1:1.5, 2: 4.5, 3: 5.5})
def z_init_rule(m, i):
    return float(i) + 0.5
model.z = pyo.Var(model.A, initialize=z_init_rule)

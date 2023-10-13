import pyomo.environ as pyo

m = pyo.ConcreteModel()
m.v = pyo.Var([0, 1, 2])
m.c2 = pyo.Constraint([0, 1, 2])

opt = pyo.SolverFactory('gurobi_persistent')
opt.set_instance(m)

results = opt.solve()

# index variable 需要这样改变
for i in range(3):
    m.c2[i] = m.v[i] == i

for v in m.v.values():
    opt.add_var(v)

for c in m.c2.values():
    opt.add_constraint(c)

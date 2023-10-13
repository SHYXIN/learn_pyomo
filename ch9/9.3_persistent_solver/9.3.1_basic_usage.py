import pyomo.environ as pyo

# min x^2 + y^2
# s.t. y >= -2x + 5
m = pyo.ConcreteModel()

m.x = pyo.Var()
m.y = pyo.Var()
m.obj = pyo.Objective(expr=m.x**2 + m.y**2)
m.c = pyo.Constraint(expr=m.y>=-2*m.x + 5)

# create an intance of a persistent solver through SolverFatory
opt = pyo.SolverFactory('gurobi_persistent')
print(opt)
# tell the solver about to our model
opt.set_instance(m)

# 这里不同，不要将model传入
results = opt.solve()

# add the constraint
m.c2 = pyo.Constraint(expr=m.y>=m.x)
opt.add_constraint(m.c2)

results = opt.solve()

# delete the constraint
# 删除时先删除求解器上的，然后再删除模型上的
opt.remove_constraint(m.c2)
del m.c2
results = opt.solve()
m.pprint()




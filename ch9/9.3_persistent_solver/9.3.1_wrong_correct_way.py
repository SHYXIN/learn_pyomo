import pyomo.environ as pyo

m = pyo.ConcreteModel()
m.x = pyo.Var()
m.y = pyo.Var()
m.c = pyo.Constraint(expr=m.y>=-2*m.x+5)
opt = pyo.SolverFactory('gurobi_persistent')
opt.set_instance(m)

# Wrong:
del m.c
m.c = pyo.Constraint(expr=m.y<=m.x)
opt.add_constraint(m.c)

### correct
m = pyo.ConcreteModel()
m.x = pyo.Var()
m.y = pyo.Var()
m.c = pyo.Constraint(expr=m.y>=-2*m.x+5)
opt = pyo.SolverFactory('gurobi_persistent')

opt.set_instance(m)
# correct
opt.remove_constraint(m.c)
del m.c
m.c = pyo.Constraint(expr=m.y<=m.x)
opt.add_constraint(m.c)

# 只有变量有点不同，顺序不同
m = pyo.ConcreteModel()
m.x = pyo.Var()
m.y = pyo.Var()
m.obj = pyo.Objective(expr=m.x**2 + m.y**2)
m.c = pyo.Constraint(expr=m.y>=-2*m.x+5)
opt = pyo.SolverFactory('gurobi_persistent')
opt.set_intance(m)
# 注意这里
m.x.setlb(1.0)
opt.update_var(m.x)

import pyomo.environ as pyo

m = pyo.ConcreteModel()
m.x = pyo.Var()
m.y = pyo.Var()
m.obj = pyo.Objective(expr=m.x**2 + m.y ** 2)
m.c = pyo.Constrant(expr=m.y>=-2*m.x + 5)
opt = pyo.Constraint(expr=m.y>=-2*m.c+ 5)
opt.set_instance(m)
results = opt.solve(save_results=False)

# Note that if the save results flag is set to False,
# then the following is not supported.
results = opt.solve(save_results=False, load_solutions=False)
if results.solver.termination_condition == pyo.TerminationCondition.optimal:
    try:
        m.solutions.load_from(results)
    except AttributeError:
        print('AttributeError was raised')

# However, the following will work:
results = opt.solve(save_results=False, load_solutions=False)
if results.solver.termination_condition == pyo.TerminationCondition.optimal:
    opt.load_vars()

# Addtionally, a subset of variable values may be loaded back into the model:
results = opt.solve(save_results=False, load_solutions=False)
if results.solver.termination_condition == pyo.TerminationCondition.optimal:
    opt.load_vars([m.x])

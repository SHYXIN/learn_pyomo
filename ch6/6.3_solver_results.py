from pyomo.opt import SolverStatus, TerminationCondition

# Wait to load the solution into the model untill
# after the solver status is checked
results = solver.solve(model, load_solutions=False)
if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition==TerminationCondition.optimal):
    model.solutions.load_from(results)
else:
    print("Solve failed.")

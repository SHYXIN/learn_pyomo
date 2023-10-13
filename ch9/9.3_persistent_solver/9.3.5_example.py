# In this section, we re-implement the parameter sweep example from Section 9.1.3
# using a persistent solver interface. The following is a function which performs the
# parameter sweep with a persistent solver interface
import pyomo.environ as pyo
from warehouse_localtion import create_warehouse_model
from pyomo.opt.results import assert_optimal_termination
from pyomo.common.timing import TicTocTimer


def solve_parametric_persistent():
    m = create_warehouse_model(num_locations=50, num_customers=50)
    opt = pyo.SolverFactory('gurobi_persistent')
    # opt = pyo.SolverFactory('cbc_persistent')
    opt.set_instance(m)
    p_values = list(range(1, 31))
    obj_values = list()
    for p in p_values:
        m.P.value = p
        opt.remove_constraint(m.num_warehouses)
        opt.add_constraint(m.num_warehouses)
        res = opt.solve(save_results=False)
        assert_optimal_termination(res)
timer = TicTocTimer()
timer.tic()
solve_parametric_persistent()
timer.toc('Finished parameter sweep with persistent interface')

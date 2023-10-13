import pyomo.environ as pyo
import cProfile
import pstats
import io
from pyomo.common.timing import TicTocTimer, report_timing
from pyomo.opt.results import assert_optimal_termination
from pyomo.core.expr.numeric_expr import LinearExpression
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

def create_warehouse_model(num_locations=50, num_customers=50):
    N = list(range(num_locations))  # warehouse locations
    M = list(range(num_customers))  # customers

    d = dict()
    for n in N:
        for m in M:
            d[n, m] = np.random.randint(low=1, high=100)

    max_num_warehouses = 2

    model = pyo.ConcreteModel(name='(WL)')
    model.P = pyo.Param(initialize=max_num_warehouses, mutable=True)

    model.x = pyo.Var(N, M, bounds=(0, 1))
    model.y = pyo.Var(N, bounds=(0, 1))

    def obj_rule(mdl):
        return sum(d[n,m]*mdl.x[n,m] for n in N for m in M)
    model.obj = pyo.Objective(rule=obj_rule)

    def demand_rule(mdl, m):
        return sum(mdl.x[n,m] for n in N) == 1
    model.demand = pyo.Constraint(M, rule=demand_rule)

    def warehouse_active_rule(mdl, n, m):
        return mdl.x[n,m] <= mdl.y[n]
    model.warehouse_active = pyo.Constraint(N, M, rule=warehouse_active_rule)

    def num_warehouses_rule(mdl):
        return sum(mdl.y[n] for n in N) <= model.P
    model.num_warehouses = pyo.Constraint(rule=num_warehouses_rule)

    return model

# 9.1.1 Profiling to Indentify Performance Bottlenecks
# report_timing()
# print('Building model')
# print('--------------')
# m = create_warehouse_model(num_locations=200, num_customers=200)

# 9.1.2 TicTocTimer
def solve_warehouse_localtion(m):
    opt = pyo.SolverFactory('glpk')
    res = opt.solve(m)
    assert_optimal_termination(res)

# # conda install -c gurobi gurobi=10.0.1

# timer = TicTocTimer()
# timer.tic('start')
# m = create_warehouse_model(num_locations=200, num_customers=200)
# timer.toc('Build model')
# solve_warehouse_localtion(m)
# timer.toc('Wrote LP file and solved')

# [    0.00] start
# [+   1.30] Build model
# [+  56.20] Wrote LP file and solved

# cProfile 和 line_profile
def solve_parametric():
    m = create_warehouse_model(num_locations=50, num_customers=50)
    opt = pyo.SolverFactory('glpk')
    p_values = list(range(1, 31))
    obj_values = list()
    for p in p_values:
        m.P.value = p
        res = opt.solve(m)
        assert_optimal_termination(res)
        obj_values.append(res.problem.lower_bound)


# timer = TicTocTimer()

# timer.tic('start parameter sweep')
# solve_parametric()
# timer.toc('Finished parameter sweep')

# cprofile

def print_c_profiler(pr, lines_to_print=15):
    s = io.StringIO()
    stats = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    stats.print_stats(lines_to_print)
    print(s.getvalue())
    with open("cumulative.txt", "w") as file:
        file.write(s.getvalue())
    s = io.StringIO()
    stats = pstats.Stats(pr, stream=s).sort_stats('tottime')
    stats.print_stats(lines_to_print)
    print(s.getvalue())
    with open("total_time.txt", "w") as file:
        file.write(s.getvalue())

pr = cProfile.Profile()
pr.enable()
solve_parametric()
pr.disable()
print_c_profiler(pr)

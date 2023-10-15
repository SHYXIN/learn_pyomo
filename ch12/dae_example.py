import pyomo.environ as pyo
import pyomo.dae as dae

m = pyo.ConcreteModel()

m.tf = pyo.Param(initialize=1)  # final time
m.t = dae.ContinuousSet(bounds=(0, m.tf))

m.u = pyo.Var(m.t, initialize=0)
m.x1 = pyo.Var(m.t)
m.x2 = pyo.Var(m.t)
m.x3 = pyo.Var(m.t)

# 这行代码是在创建一个 DerivativeVar（导数变量）对象 m.dx1，
# 这个导数变量用于表示变量 m.x1 关于 m.t 连续集的导数。
# 也就是说，m.dx1 表示了 m.x1 针对时间 m.t 的导数。
# 这在动态系统建模中经常用于表示状态变量对时间的变化率。
# 这可以帮助建模动态系统的微分方程。

m.dx1 = dae.DerivativeVar(m.x1, wrt=m.t)
m.dx2 = dae.DerivativeVar(m.x2, wrt=m.t)

# 这行代码创建了一个 DerivativeVar（导数变量）对象 m.dx3，
# 用于表示变量 m.x3 的导数。与前面的例子不同，这里没有指定导数相对于哪个连续集（例如时间）。
# 因此，m.dx3 表示了 m.x3 的未指定连续集的导数。在某些情况下，导数不一定与特定的连续集相关联，
# 或者可以通过其他方式确定。这可以用于表示状态变量的导数，而无需指定特定的连续集
m.dx3 = dae.DerivativeVar(m.x3)

# m.dx1dt2 = dae.DerivativeVar(m.x1, wrt=(m.t, m.t))  # 高阶求导


def _x1dot(m, t):
    return m.dx1[t] == m.x2[t]
m.x1dotcon = pyo.Constraint(m.t, rule=_x1dot)

def _x2dot(m, t):
    return m.dx2[t] == -m.x2[t] + m.u[t]
m.x2dotcon = pyo.Constraint(m.t, rule=_x2dot)

def _x3dot(m, t):
    return m.dx3[t] == m.x1[t]**2 + m.x2[t]**2 + 0.005*m.u[t] **2
m.x3dotcon = pyo.Constraint(m.t, rule=_x3dot)

m.x1dotcon[m.t.first()].deactivate()
m.x2dotcon[m.t.first()].deactivate()
m.x3dotcon[m.t.first()].deactivate()

m.x1[0].fix(0)
m.x2[m.t.first()].fix(-1)
m.x3[m.t.first()].fix(0)

m.obj = pyo.Objective(exrp=m.x3[m.tf])

def _con(m, t):
    return m.x2[t] - 8 * (t - 0.5) ** 2 + 0.5 <=0
m.con = pyo.Constraint(m.t, rule=_con)

# solve
# 1、finite_difference
discretizer = pyo.TransformationFactory('dae.finite_difference')
discretizer.apply_to(m, nfe=20, wrt=m.t, scheme='BACKWARD')

# 2 collocation
discretizer = pyo.TransformationFactory('dae.collocation')
discretizer.apply_to(m, nfe=7, ncp=6,scheme='LAGRANGE-RADAU')

# 在这里，nfe关键字参数指定了有限元的数量，ncp参数指定了每个有限元内的配点数量。
# scheme参数用于选择正交配点的类型。
# 配点的数量和类型的选择通常取决于特定问题的性质，以及希望获得的逼近精度。


# Applying Multiple Discretization

# Applying multiple finite difference schemes
discretizer = pyo.TransformationFactory('dae.finite_difference')
discretizer.apply_to(m, wrt=m.t1, nfe=10, scheme='BACKWARD')
discretizer.apply_to(m, wrt=m.t1, nfe=100, scheme='FORWARD')

# Applying multiple collocation schemes
discretizer = pyo.TransformationFactory('dae.collocation')
discretizer.apply_to(m, wrt=m.t1, nfe=4, ncp=6, scheme='LAGRANGE-LEGENDRE')
discretizer.apply_to(m, wrt=m.t2, nfe=10, ncp=3, scheme='LAGRANGE-RADAU')

# Applying a combination of finiter difference and collocation schemes
discretizer1 = pyo.TransformationFactory('dae.finite_difference')
discretizer2 = pyo.TransformationFactory('dae.collocation')
discretizer1.apply_to(m, wrt=m.t1, nfe=10, scheme='BACKWARD')
discretizer2.apply_to(m, wrt=m.t2, nfe=5, ncp=3, scheme='LAGRANGE-RADAU')

# Restricting Control Input Profiles
discretizer.reduce_collocation_points(m, var=m.u, ncp=1, contest=m.t)

# Plotting


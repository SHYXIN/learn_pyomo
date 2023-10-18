import pyomo.environ as pyo

def IC_model(A, h, d, c, b, u):

    model = pyo.ConcreteModel(name="(H)")

    def x_bounds(m, i):
        return (0, u[i])
    model.x = pyo.Var(A, bounds=x_bounds)

    def z_rule(model):
        return sum(h[i] * (model.x[i] - (model.x[i]/d[i])**2) for i in A)
    model.z = pyo.Objective(rule=z_rule, sense=pyo.maximize)

    model.budgetconstr = pyo.Constraint(
        expr=sum(c[i]*model.x[i] for i in A) <= b
    )

    return model

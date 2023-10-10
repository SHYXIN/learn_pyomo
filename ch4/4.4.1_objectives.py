import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x = pyo.Var([1, 2], initialize=1.0)

model.b = pyo.Objective(expr=model.x[1] + 2 * model.x[2])

def m_rule(model):
    expr = model.x[1]
    expr += 2*model.x[2]
    return expr

model.c = pyo.Objective(rule=m_rule)

# multiple objectives
model = pyo.ConcreteModel()

A = ['Q', 'R', 'S']
model.x = pyo.Var(A, initialize=1.0)
def d_rule(model, i):
    return model.x[i] ** 2
# 这个会形成多个目标函数
model.d = pyo.Objective(A, rule=d_rule)

def e_rule(model, i):
    if i == 'R':
        return pyo.Objective.Skip
    return model.x[i] ** 2

model.e = pyo.Objective(A, rule=e_rule)
# sense=pyo.maximize



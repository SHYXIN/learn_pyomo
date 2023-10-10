import pyomo.environ as pyo

model = pyo.ConcreteModel()


A = ['Q', 'R']
model.x = pyo.Var(A, initialize={'Q': 1.5, 'R': 2.5})
model.o = pyo.Objective(expr=model.x['Q'] + 2 * model.x['R'], sense=pyo.maximize)

# 表达式  求最大小值  求初始化状态的目标值
print(model.o.expr)  # x[Q] + 2*x[R]
print(model.o.sense)  # minimize
print(pyo.value(model.o))  # 6.5=1.5+2*2.5

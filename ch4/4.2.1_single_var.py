# 示例 1：单个标量值
import pyomo.environ as pyo

model = pyo.ConcreteModel()

# 创建集合
model.I = pyo.Set(initialize=[1, 2, 3])

# 创建所有索引都具有单个标量值的变量
model.x = pyo.Var(model.I, initialize=10)

model.obj = pyo.Objective(expr=model.I)
# 求解模型
solver = pyo.SolverFactory('glpk')
solver.solve(model)

# 打印变量值
print(model.x.value)
# 结果
# {1: 10, 2: 10, 3: 10}


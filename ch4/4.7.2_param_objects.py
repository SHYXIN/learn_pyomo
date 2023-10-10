import pyomo.environ as pyo

# # 采用稀疏处理
model = pyo.ConcreteModel()
# # model.T = pyo.Param(model.A, model.B)

model.B = pyo.Set(initialize=[1,2,3])
w = {}
w[1] = 10
w[3] = 30
model.W = pyo.Param(model.B, initialize=w)

# 因为没设置会报错
# print(model.W[2])

#########  default
model = pyo.ConcreteModel()
model.p = pyo.Param([1,2,3], initialize={1: 1.42, 3: 3.14})
model.q = pyo.Param([1,2,3], initialize={1: 1.42, 3: 3.14}, default=0)

# Demonstrating the len() function
print(len(model.p))  #  2
print(len(model.q))  #  3

# Demonstrating the 'in' operateor (checks against component keys)
print(2 in model.p)  # False
print(2 in model.q)  # True

# Demonstrating iteration over component keys
print([key for key in model.p])  # [1, 3]
print([key for key in model.q])  # [1, 2, 3]


print(model.p.sparse_keys())
print(model.p.sparse_values())
print(model.p.sparse_items())

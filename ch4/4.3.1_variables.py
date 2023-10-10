import pyomo.environ as pyo

# # domain 定义域
# model = pyo.ConcreteModel()
# model.A = pyo.Set(initialize=[1, 2, 3])
# model.y = pyo.Var(within=model.A)
# model.r = pyo.Var(domain=pyo.Reals)
# model.w = pyo.Var(within=pyo.Boolean)


# model.A = pyo.Set(initialize=[1, 2, 3])
# def s_domain(model, i):
#     return pyo.RangeSet(i, i+1, 1) # (start, end, step)
# model.s = pyo.Var(model.A, domain=s_domain)

# def x_domain(model, i):
#     if i == 1:
#         return pyo.Reals
#     elif i == 2:
#         return pyo.NonnegativeReals
#     else:
#         return pyo.PositiveReals
# model.x = pyo.Var(range(1, 4), domain=x_domain)
# # 在本例中，x_domain 函数针对每个索引返回不同的域。
# # 对于索引 1，域是所有实数。
# # 对于索引 2，域是所有非负实数。
# # 对于索引 3，域是所有正实数。

# # bounds 上下界
# model.A = pyo.Set(initialize=[1, 2, 3])
# model.a = pyo.Var(bounds=(0.0, None))

# lower = {1:2.5, 2: 4.5, 3: 6.5}
# upper = {1:3.5, 2: 4.5, 3: 7.5}

# def f(model, i):
#     return (lower[i], upper[i])
# model.b = pyo.Var(model.A, bounds=f)
# # model.b[3] => (6.5, 7.5)

#  initialize 关键字
model = pyo.ConcreteModel()
model.A = pyo.Set(initialize=[1,2,3])
model.za = pyo.Var(initialize=9.5, within=pyo.NonNegativeReals)
model.zb = pyo.Var(model.A, initialize={1: 1.5, 2: 4.5, 3: 5.5})
model.zc = pyo.Var(model.A, initialize=2.1)

print(pyo.value(model.za)) # 9.5
print(pyo.value(model.zb[3])) # 5.5
print(pyo.value(model.zc[3]))  # 2.1

model = pyo.ConcreteModel()
model.A = pyo.Set(initialize=[1,2,3])
def g(model, i):
    return 3 * i
model.m = pyo.Var(model.A, initialize=g)

print(pyo.value(model.m[1]))  # 3
print(pyo.value(model.m[3]))  # 9

import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.A = pyo.Set(initialize=[1,2,3])
model.za = pyo.Var(initialize=9.5, within=pyo.NonNegativeReals)
model.zb = pyo.Var(model.A, initialize={1: 1.5, 2:4.5, 3:5.5})
model.zc = pyo.Var(model.A, initialize=2.1)

print(pyo.value(model.zb[2])) # 4.5
print(model.za.lb) # 0 下界
print(model.za.ub)  # None 上界
# 还可以在设置上下界
model.za.setlb(1.0)
model.za.setub(1000.0)
print(model.za.lb, model.za.ub)

# 重新赋值
model.za = 8.5
model.zb[2] = 7.5
print(pyo.value(model.za))
print(pyo.value(model.zb[2]))

# 可以使用setvalues方法,???
variable_values = {
    'zc': {1: 3.0, 2: 2.0, 3:1.0},
    'zb': {1: 4.0, 2:3.2, 3:4.0}
}
model.zb.set_values(variable_values['zb'])

# print(pyo.value(model.za))
print(pyo.value(model.zb[2]), 'sadfsad')

model.zb.fix(3.0)
print(model.zb[1].fixed)  # True
print(model.zb[2].fixed) # True

model.zc[2].fix(3.0)
print(model.zc[1].fixed)
print(model.zc[2].fixed)


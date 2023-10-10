import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.A = pyo.Set(initialize=[1,2,3])
model.B = pyo.Set(initialize=['A', 'B'])
model.U = pyo.Param(model.A, initialize={1: 10, 2: 20, 3: 30})
model.T = pyo.Param(model.A, model.B,
                    initialize={(1, 'A'): 10,
                                (2, 'B'): 20,
                                (3, 'A'): 30
                                })

def X_init(model, i, j):
    return i * j
model.X = pyo.Param(model.A, model.A, initialize=X_init)


def XX_init(model, i, j):
    if i == 1 or j == 1:
        return i * j
    return i * j + model.XX[i-1, j-1]

model.XX = pyo.Param(model.A, model.A, initialize=XX_init)

# default 提供默认值
# 如创建对角矩阵
u = {}
u[1,1] = 10
u[2,2] = 20
u[3,3] = 30
model.U = pyo.Parm(model.A, model.A, initialize=u, default=0)

# validation
model.Z = pyo.Param(within=pyo.Reals)

def Y_validate(model, value):
    return value in pyo.Reals
model.Y = pyo.Param(validate=Y_validate)

model.A = pyo.Set(initialize=[1, 2, 3])
def X_validate(model, value, i):
    return value > i
model.X = pyo.Param(model.A, validate=X_validate)

# x1 + 4x2 + 9x3

model = pyo.ConcreteModel()
p = {1: 1, 2:4 , 3:9}

model.A = pyo.Set(initialize=[1,2,3])
model.p = pyo.Param(model.A, initialize=p)
model.x = pyo.Var(model.A, within=pyo.NonNegativeReals)
# 会直接计算sum，实际上传给Param是一个常数
model.o = pyo.Objective(expr=sum(model.p[i]*model.x[i] for i in model.A))

# mutable
# 设置可变
model = pyo.ConcreteModel()
p = {1:1, 2:4, 3:9}

model.A = pyo.Set(initialize=[1,2,3])
model.p = pyo.Param(model.A, initialize=p, mutable=True)  # 设置可变
model.x = pyo.Var(model.A, within=pyo.NonNegativeReals)

model.o = pyo.Objective(expr=pyo.summation(model.p, model.x,))
# 这里可以重新设置值，进行变化
model.p[2] = 4.2
model.p[3] = 4.14

# p1x1 + p2x2 + p3x3
# x1 +4.2x2 +3.14x3.
# 使用mutable会增加内存开销，默认情况下是 False



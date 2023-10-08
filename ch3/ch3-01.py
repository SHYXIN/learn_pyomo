import pyomo.environ as pyo

model = {}

model.x = pyo.Var()
model.y = pyo.Var(bounds=(-2, 4))
model.z = pyo.Var(initialize=1.0, within=pyo.NonNegativeReals)

model.obj = pyo.Objective(expr=model.x + model.y + model.z)

model.eq_con = pyo.Constraint(expr=model.x + model.y + model.z == 1)

model.ineq_con = pyo.Constraint(expr=model.x + model.y <= 0)



# 仓库选址问题，使用标量完成
# Customer locations M = {‘NYC’, ‘LA’, ‘Chicago’, ‘Houston’}
# Candidate warehouse locations N = {‘Harlingen’, ‘Memphis’, ‘Ashland’}
#           NYC LA Chicago Houston
# Harlingen 1956 1606 1410 330
# Memphis 1096 1792 531 567
# Ashland 485 2322 324 1236
model.x_Harlingen_NYC = pyo.Var(bounds=(0, 1))
model.x_Harlingen_LA = pyo.Var(bounds=(0, 1))
model.x_Harlingen_Chicago = pyo.Var(bounds=(0, 1))
model.x_Harlingen_Houston = pyo.Var(bounds=(0, 1))
model.x_Memphis_NYC = pyo.Var(bounds=(0, 1))
model.x_Memphis_LA = pyo.Var(bounds=(0, 1))

model.maxY = pyo.Constraint(expr=model.y_Harlingen + model.y_Memphis + model.y_Ashland <= P)

model.one_warehouse_for_NYC = pyo.Constraint(
    expr=model.x_Harlingen_NYC + model.x_Memphis_NYC + model.x_Ashland_NYC == 1)

model.one_warehouse_for_LA = pyo.Constraint(
    expr=model.x_Harlingen_LA + model.x_Mephis_LA + model.x_Ashland_LA == 1
)

# 太麻烦了
N = ['Harlingen', 'Memphis', 'Ashland']  # 仓库候选地址
M = ['NYC', 'LA', 'Chicago', 'Houston']  # 客户所在地址
# 使用indexed components
model.x = pyo.Var(N, M, bounds=(0, 1))
model.y = pyo.Var(N, within=pyo.Binary)

# 我们将N和M称为索引变量model.x和model.y的索引集。具体来说,变量y以N为索引,
# 变量x是一个二维数组,同时以N和M为索引。通过这种声明,可以通过model.x[i,j]访问x的一个元素,
# 其中i和j分别是集合N和M中的元素

model.num_warehouses = pyo.Constraint(expr=sum(model.y[n] for n in N <= P))

model.obj = pyo.Objective(expr=sum(d[n, m] * model.x[n, m] for n in N for m in M))

# Construction Rules
def demand_rule(mdl, m):
    "对于任意一个m属于M，客户的需求必须满足"
    return sum(mdl.x[n, m] for n in N) == 1
model.demand = pyo.Constraint(M, rule=demand_rule)

# 这里的前两行定义了一个Python函数，该函数将用于为M中的每个元素生成正确的约束表达式。
# 示例中的最后一行通过创建一个在由M定义的集合上索引的Constraint组件来声明约束。
# 关键字参数"rule"指示将调用"demand_rule"函数来构建每个约束。

# 函数"demand_rule"中的第一个参数将自动设置为正在构建的模型对象的实例。
# 接着是提供正在构建的特定约束的索引的参数。当Pyomo构建Constraint对象时，
# 构造规则会针对指定索引集的每个值调用一次。

import pyomo.environ as pyo

model = pyo.ConcreteModel()

# Set Declarations
model.A = pyo.Set()
# ----
model.A = pyo.Set()
model.B = pyo.Set()
model.C = pyo.Set(model.A)
model.D = pyo.Set(model.A, model.B)

######
model.E = pyo.Set([1, 2, 3])
f = set([1, 2, 3])
model.F = pyo.Set(f)

#### 集合操作
model.A = pyo.Set()
model.B = pyo.Set()
model.G = model.A | model.B   # set union
model.H = model.B & model.A   # set intersection
model.I = model.A - model.B  # set difference
model.J = model.A ^ model.B  # set exclusive-or  交集的补集

model.A = pyo.Set()
model.B = pyo.Set()
model.K = model.A * model.B  # cross-products


model.B = pyo.Set(initialize=[2, 3, 4])
model.C = pyo.Set(initialize=[(1, 4), (9, 16)])

F_init = {}
F_init[2] = [1,3,5]
F_init[3] = [2,4,6]
F_init[4] = [3,5,7]

model.F = pyo.Set([2,3,4], initialize=F_init)

# rule
def J_init(model, i, j):
    return range(0, i * j)
model.J = pyo.Set(model.B, model.B, initialize=J_init)

# filter
model.P = pyo.Set(initialize=[1, 2, 3, 5, 7])
def filter_rule(model, x):
    return x not in model.P
model.Q = pyo.Set(initialize=range(1, 10), filter=filter_rule)

#####
model.R = pyo.Set([1, 2, 3])
model.R[1] = [1]
model.R[2] = [1, 2]

# Validation
model.B = pyo.Set(within=model.A)


def C_validation(model, value):
    return value in model.A
model.C = pyo.Set(validate=C_validation)


# sorted order
model.A = pyo.Set(ordered=pyo.Set.SortedOrder)

# dimension
# Define a set of all pairs of integers from 1 to 100, such that the first integer is greater than the second integer.
model.pairs = pyo.Set(initialize=[(i, j) for i in range(1, 101) for j in range(1, i)], dimension=2)

# Define a set of all triangles in a graph, such that the three nodes of the triangle are in ascending order.
model.triangles = pyo.Set(initialize=[(i, j, k) for i in range(1, 101) for j in range(i + 1, 101) for k in range(j + 1, 101)], dimension=3)

# RangeSet

model.A = pyo.RangeSet(10)
model.c = pyo.RangeSet(5, 10)
model.D = pyo.RanageSet(2.5, 11, 1.5)

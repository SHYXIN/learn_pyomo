import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x = pyo.Var()
model.P = pyo.Param(initialize=5)
model.S = pyo.RangeSet(model.P)
model.b = pyo.Block()
model.b.I = pyo.RangeSet(model.P)
model.b.x = pyo.Var(model.b.I)
model.b.y = pyo.Var(model.S)
model.b.b = pyo.Block([1,2])
model.b.b[1].x = pyo.Var()
model.b.b[2].x = pyo.Var()

# name
print(model.x.local_name)           # x
print(model.x.name)                 # x

print(model.b.x.local_name)         # x
print(model.b.x.name)               # b

print(model.b.b[1].x.local_name)    # x
print(model.b.b[1].x.name)          # b.b[1].x

# 8.2
# hierarchy 层级
print(model.b.b[1].x.parent_component())  # is model.b.b[1].x
print(model.b.b[1].x.parent_block())      # is model.b.b[1]
print(model.b.b[1].x.model())             # is model
print(model.b.x[1].parent_component())    # is model.b.x
print(model.b.x[1].parent_block())        # is model.b
print(model.b.x[1].model())               # is model
print(model.b.component('x'))             # is model.b.x


# block can be also created and populated, and later added to a model
new_b = pyo.Block()
new_b.x = pyo.Var()
new_b.P = pyo.Param(initialize=5)
new_b.I = pyo.RangeSet(10)

model = pyo.ConcreteModel()
model.b = new_b
model.x = pyo.Var(model.b.I)

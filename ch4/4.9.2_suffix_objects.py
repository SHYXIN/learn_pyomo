import pyomo.environ as pyo

model = pyo.ConcreteModel()
model.x = pyo.Var()
model.y = pyo.Var([1, 2, 3])
model.foo = pyo.Suffix()

# Assign the value 1.0 to suffix 'foo' for model.x
model.x.set_suffix_value('foo', 1.0)

# Assign the value 2.0 to suffix model.foo for model.x
model.x.set_suffix_value(model.foo, 2.0)

# Get the value of suffix 'foo' for model.x
print(model.x.get_suffix_value('foo'))  # 2.0

# indexed components

# Assign the value 3.0 to suffix model.foo for model.y
model.y.set_suffix_value(model.foo, 3.0)

# Assign the value 4.0 to suffix model.foo for model.y[2]
model.y[2].set_suffix_value(model.foo, 4.0)

# Get the value of suffix 'foo' for model.y
print(model.y.get_suffix_value(model.foo))

print(model.y[1].get_suffix_value(model.foo))  # 3.0
print(model.y[2].get_suffix_value(model.foo))  # 4.0
print(model.y[3].get_suffix_value(model.foo))  # 3.0


# clear suffix
model.y[3].clear_suffix_value(model.foo)

print(model.y.get_suffix_value(model.foo)) # None
print(model.y[1].get_suffix_value(model.foo))  # 3.0
print(model.y[2].get_suffix_value(model.foo))  # 4.0
print(model.y[3].get_suffix_value(model.foo))  # None

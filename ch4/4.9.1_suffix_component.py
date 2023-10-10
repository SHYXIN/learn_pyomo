import pyomo.environ as pyo


model = pyo.ConcreteModel()
model.foo = pyo.Suffix()


# Export integer data
model.priority = pyo.Suffix(direction=pyo.Suffix.EXPORT,
                            datatype=pyo.Suffix.INT)
# Export and import floating point data
model.dual = pyo.Suffix(direction=pyo.Suffix.IMPORT_EXPORT)


model = pyo.ConcreteModel()
model.x = pyo.Var()
model.c = pyo.Constraint(expr=model.x >=1)

def foo_rule(m):
    return ((m.x, 2),(m.c,3.0))

model.foo = pyo.Suffix(initialize=foo_rule)

import pyomo.environ as pyo

model = pyo.AbstractModel()

model.I = pyo.Set()
model.K = pyo.Set()
model.V = pyo.Set()

def kv_init(m):
    return ((k, v) for k in m.K for v in m.V[k])
model.KV = pyo.Set(dimen=2, initialize=kv_init)

model.a = pyo.Param(model.I, model.K)

model.y = pyo.Var(model.I)
model.x = pyo.Var(model.I, model.KV)

# include a constrant that looks like  this:
# x[i, k, v] <= a[i, k]*y[i], for i in I, k in K, V in V[k]

def  c1Rule(m, i, k, v):
    return m.x[i, k, v] <= m.a[i, k] * m.y[i]

model.c1 = pyo.Constraint(model.I, model.KV, rule=c1Rule)

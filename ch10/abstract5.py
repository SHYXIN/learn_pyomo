# abstract5.py
import pyomo.environ as pyo
model = pyo.AbstractModel()
model.N = pyo.Set()
model.M = pyo.Set()
model.c = pyo.Param(model.N)
model.a = pyo.Param(model.N, model.M)
model.b = pyo.Param(model.M)
model.x = pyo.Var(model.N, within=pyo.NonNegativeReals)
def obj_rule(model):
    return sum(model.c[i]*model.x[i] for i in model.N)
model.obj = pyo.Objective(rule=obj_rule)
def con_rule(model, m):
    return sum(model.a[i,m]*model.x[i] for i in model.N) >= model.b[m]

model.con = pyo.Constraint(model.M, rule=con_rule)

# pyomo solve --solver=glpk abstract5.py abstract.dat
# pyomo solve --solver=glpk --namespace=data1 abstract5.py abstract5-ns1.dat
# pyomo solve --solver=glpk --namespace=data2 abstract5.py abstract5-ns1.dat
# pyomo solve --solver=glpk --namespace=c1 --namespace=data2 abstract5.py abstract5-ns2.dat

# ex1c.py
import pyomo.environ as pyo
from pyomo.mpec import ComplementarityList, complements

n = 5

model = pyo.ConcreteModel()

model.x = pyo.Var(range(1, n+1))

model.f = pyo.Objective(
    expr=sum(i*(model.x[i] - 1) **2 for i in range(1, n+1))
)

def compl_(model):
    yield complements(model.x[1]>=0, model.x[2]>=0)
    yield complements(model.x[2]>=0, model.x[3]>=0)
    yield complements(model.x[3]>=0, model.x[4]>=0)
    yield complements(model.x[4]>=0, model.x[5]>=0)
model.compl = ComplementarityList(rule=compl_)

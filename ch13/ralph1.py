# ralph1.py

# min 2x−y
# 0 ≤ y ⊥ y ≥ x
# x, y ≥ 0
import pyomo.environ as pyo
from pyomo.mpec import Complementarity, complements

model = pyo.ConcreteModel()

model.x = pyo.Var(within=pyo.NonNegativeReals)
model.y = pyo.Var(within=pyo.NonNegativeReals)

model.f1 = pyo.Objective(expr=2*model.x - model.y)

model.compl = Complementarity(
    expr=complements(0<=model.y, model.y>=model.x)
)


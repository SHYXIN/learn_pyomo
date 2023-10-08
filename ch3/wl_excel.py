# wl_excel.py：Loading Excel data using Pandas
import pandas
import pyomo.environ as pyo
from wl_concrete import create_warehouse_model

# read the data from Excel using Pandas
df = pandas.read_excel('wl_data.xlsx', 'Delivery Costs', header=0, index_col=0)

N = list(df.index.map(str))

M = list(df.columns.map(str))
d = {(r, c): df.at[r, c] for r in N for c in M}
P = 2

# create the Pyomo model
model = create_warehouse_model(N, M, d, P)

# create the solver interface and solve the model
solver = pyo.SolverFactory('glpk')
solver.solve(model)

model.y.pprint()  # print the optimal warehouse locations

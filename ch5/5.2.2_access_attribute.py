
import json
import pyomo.environ as pyo
from warehouse_model import create_wl_model

# Load the data from a json
with open('warehouse_data.json', 'r') as fd:
    data = json.load(fd)

# call function to create model
model = create_wl_model(data, P=2)

# solve the model
solver = pyo.SolverFactory('glpk')
solver.solve(model)

# 5.2.2 Accessing Attributes of Indexed Components
# indexed components
print(pyo.value(model.y['Ashland']))

##
for i in model.y:
    print('{0} = {1}'.format(model.y[i], pyo.value(model.y[i])))

###
for i in model.WH:
    print('{0} = {1}'.format(model.y[i], pyo.value(model.y[i])))
print('\nSlicing Over indices of Components\n')
# 5.2.2.1 Slicing Over indices of Components
for v in model.x['Ashland', :]:
    print('{0} = {1}'.format(v, pyo.value(v)))

# 5.2.2.2 Iterating Over All Var objects on a Model
# loop over the Var objects on the model
print('\nVar Objects: \n')
for v in model.component_objects(ctype=pyo.Var):
    for index in v:
        print('{0} <= {1}'.format(v[index], pyo.value(v[index].ub)))

# or use the following to loop over the individual indices of
# each of the Var objects directly
print('\ndirectly Var objects\n')
for v in model.component_data_objects(ctype=pyo.Var):
    print('{0} <= {1}'.format(v, pyo.value(v.ub)))

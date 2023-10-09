import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.N = pyo.Set()
model.M = pyo.set()

model.x = pyo.Var(model.N, model.M, bounds=(0, 1))
model.y = pyo.Var(model.N, within=pyo.Binary)

model.PremierSundaes = pyo.Set()
model.Toppings = pyo.Set(model.PremierSundaes)


import pyomo.environ as pyo

# 创建两个集合：PremierSundaes 和 Toppings
model = pyo.ConcreteModel()
model.PremierSundaes = pyo.Set(initialize=['PBC-Banana', 'Very Berry'])
model.Toppings = pyo.Set(model.PremierSundaes)

# 为每个口味定义配料
model.Toppings['PBC-Banana'] = pyo.Set(initialize=['Peanut Butter', 'Chocolate Fudge', 'Banana'])
model.Toppings['Very Berry'] = pyo.Set(initialize=['Strawberries', 'Raspberries', 'Blueberries', 'Crunch-berries'])

# 打印每个口味的配料
for sundae in model.PremierSundaes:
    print(f'The toppings for {sundae} are {model.Toppings[sundae]}')


# Parameters

model.d = pyo.Param(model.N, model.M)
model.P = pyo.Param()


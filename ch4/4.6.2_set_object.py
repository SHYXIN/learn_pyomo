import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.A = pyo.Set(initialize=[1, 2, 3])

print(len(model.A))
print(model.A.data())

# data() 获取数据
model.A = pyo.Set(initialize=[1,2,3])
model.B = pyo.Set(initialize=[3,2,1], ordered=True)
model.B1 = pyo.Set(initialize=[3,2,1])
model.C = pyo.Set(model.A, initialize={1:[1], 2: [1, 2]})

print(type(model.A.data()) is tuple)  # True
print(type(model.B.data()) is tuple)  # True
print(type(model.C.data()) is dict)   # type
print(sorted(model.A.data()))  # [1, 2, 3]

for index in sorted(model.C.data().keys()):
    print(sorted(model.C.data()[index]))
# [1]
# [1, 2]
print(model.C.data().keys())
print(sorted(model.C.data().keys()))

print(model.B.data())

print(model.B1.data())

# operation
model.A = pyo.Set(initialize=[1, 2, 3])

# Test if an element is in the set
print(1 in model.A)  # True

# Test if sets are equal
print([1, 2] == model.A)  # False

# Test if sets are not equal
print([1, 2] != model.A)  # True

# Test if a set is a subset of or equal the set
print([1, 2] <= model.A)  # True

# Test if a set is a subset of the set
print([1, 2] < model.A)  # True

# Test if a set is a superset of the set
print([1, 2, 3] > model.A) # False


# iterate
model.A1 = pyo.Set(initialize=[1,2,3])
model.C1 = pyo.Set(model.A, initialize={1: [1], 2: [1, 2]})

print(sorted(e for e in model.A))  # [1, 2, 3]
for index in model.C:
    print(sorted(e for e in model.C[index]))

# [1]
# [1, 2]

model.A2 = pyo.Set(initialize=[3,2,1],ordered=True)
print(model.A2.first()) # 3
print(model.A2.last())  # 1
print(model.A2.next(2))  # 1
print(model.A2.prev(2)) # 3
print(model.A2.nextw(1))  # 3   wrap 循环
print(model.A2.prevw(3))  # 1
print(model.A2.prevw(2))

model.A = pyo.Set(initialize=[3,2,1], ordered=True)

print(model.A.ord(3))  # 1
print(model.A.ord(1))  # 3
print(model.A[1])  # 3
print(model.A[3])  # 1

def f():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

s = [i for i in f()]
print(s)

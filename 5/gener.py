def multiply_by_five():
    x = None
    while True:
        x = yield x
        x *= 5


g = multiply_by_five()
next(g)
print(g.send(4))
print(g.send("You all awesome python devs"))

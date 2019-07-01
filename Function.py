a = 10

print(id(a))
def something():
    a = 9
    x = globals()['a']
    globals()['a'] = 15
    print(a)
    a=10
    print(id(a))
    print(a)


something()


print(a)
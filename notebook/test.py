i = 1

def test():
    nonlocal i
    i = 2
test()
print(i)

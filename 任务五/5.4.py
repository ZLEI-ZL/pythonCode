def multi(a, *b):
    for n in b:
        a *= n
    return a

a = multi(1, 3, 4, 5)

print(a)

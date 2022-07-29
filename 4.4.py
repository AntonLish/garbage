b = input("enter number: ")
b = int(b)

g = input("enter second number: ")
g = int(g)

def f1(x):
    return x**2

def f2(x):
    return x+1

y = f1(b)
h = f1(g)
z = f2(y)
j = f2(h)
k = z+j-10

print(k*10, " - це ваш результат")


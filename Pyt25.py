def fun(n):
    return 25 * n


def fun1(x, n):
    if n != 0:
        z = x * n
    else:
        z = 1000
    return z


def fun4():
    return "Mina olen fun4"
         

def fun61():
    return "My name is James"
         


print("Ma alustan uuesti")
print("Fun = ", fun(3))
print("Fun1 ", fun1(36, 12))
print(fun61())
print(fun4())
print("Koik koos ",fun(5),"  ",fun1(18,3))
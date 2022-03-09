#problem 3
def maximum(a, b, c):
    if (a>=b) and (a>=c):
        largest = a
    elif (b>=c) and (b>=a):
        largest = b
    else:
        largest= c
    return largest

a = 10
b = 5
c= 3
print(maximum (a, b, c))



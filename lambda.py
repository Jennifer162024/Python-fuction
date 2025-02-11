def math(a,b):
    return lambda x,y: a * x + b * y
def crear_lambda(a, b):
    return lambda x, y: a * x + b * y

import math
def myfunc(a, b):
    return lambda c: (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
my_lambda = myfunc(2,4)
resultado = my_lambda(-6)
print(resultado)

## Crear una función que reciba como parametro a,b
## dentro de la función va a retornar una lambda que tenga los siguientes parametros:
## la lambda recibira c y realizara la formula:-b+RAIZ(b^2 -4ac)/2a

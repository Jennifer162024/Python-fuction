sum = lambda a,b: a+b
res = lambda a,b: a+b
mult = lambda a,b: a+b
sum = lambda a,b: a+b
def res(a,b):
    print(f"la resta de los numeros es:{a-b}")

def mult(a,b):
    print(f"la multiplicacion de los numeros es:{a*b}")

def div(a,b):
    print(f"la division de los numeros es:{a/b}")


##menu

while(True):
    print ("Bienvenido a tu calculadora de confianza")
    x=int(input("Ingres el primer numero"))
    y=int(input("Ingresa el segundo numero"))
    print("Escribe 1:para sumar")
    print("Escribe 2:para restar")
    print("Escribe 3:para multiplicar")
    print("Escribe 4:para dividir")
    print("Escribe 5:para salir")

    response =int(input("Ingresa tu opcion:"))
    if response ==1:
        print((x,y))
    elif response==2:
        print((x,y))
    elif response==3:
        print((x,y))
    elif response ==4:
        div(x,y)
    elif response ==5:
        break
    else:
        print("chistosito va")  
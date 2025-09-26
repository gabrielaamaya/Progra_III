# calculadora
x = float(input("ingrese num1: "))
y = float(input("ingrese num2: "))
operacion = input("Ingrese la operacion, suma, resta, multi, divi: ")

if operacion == "suma":
    print("haga una suma")
elif operacion == "resta":
    print("haga una resta")
elif operacion == "multi":
    print("haga una multiplicacion")
elif operacion == "divi":
    print("haga la division")
else:
    print("no existe eso en mi codigo")
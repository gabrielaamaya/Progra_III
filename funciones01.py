# crear función
def suma_numeros(num1, num2):
    return num1 + num2

# solicitar variables
num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

# imprimir el resultado
print(f"La suma de {num1} + {num2} es {suma_numeros(num1, num2)}")
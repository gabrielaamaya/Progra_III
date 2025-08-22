print("_______________________________")
print("Gabiela Amaya")
print("Codigo: USTRO12324")
print("____________________________________")
# crear función
def evaluar_numero(num):
    if num > 0:
        return "El número es positivo"
    elif num < 0:
        return "El número es negativo"
    else:
        return "El número es 0"

# solicitar número al usuario
num = int(input("Introduce un número: "))

# mostrar resultado
print(evaluar_numero(num))

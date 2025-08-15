# Mini Calculadora

print("=== Calculadora Básica ===")
print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese el número de la operación (1-4): ")

# Captura de los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada
if opcion == "1":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción inválida. Intente de nuevo.")
print ("_________________________________________")
print("Lista - sumar todos")
print("__________________________________________")
#solicitar un numero final de la lista
num1=int(input("Ingrese un numero hasta 100: "))

#crear la lista desdes 1 hasta el $num1
lista = list(range(1, num1+1))

#Calcular la suma
resultado = sum(lista)

#imprimir el resultado
print(f"La suma de la lista hasta {num1} es {resultado}")
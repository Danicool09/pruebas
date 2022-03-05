print("Introduce 2 numeros para operar número: ")
numero1=input("digite el numero 1:")
numero2=input("digite el numero 2:")
print("Selección de operación: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
opcion=input("tipo de operacion:")
if opcion=="1":
    print("La suma de los numeros es:",int(numero1)+int(numero2))
elif opcion=="2":
    print("La resta de los numeros es:",int(numero1)-int(numero2))
elif opcion=="3":
    print("La multiplicación de los numeros es:",int(numero1)*int(numero2))
else:
    print("Opcion no valida")

MaxTamC = 10
A = [0] * MaxTamC
frente= 0
final = 0
contador = 0

# Inicializar la cola
frente = 0
final = 0

respuesta = input("¿Desea agregar elementos a la cola? (s/n): ").lower()

while respuesta == 's' and contador < 10: 
    if (final + 1) % MaxTamC == frente: 
        print("Desbordamiento de la cola") 
        exit(1)
        
    elemento = int(input("Ingrese un elemento para la cola: "))
    final = (final+ 1)% MaxTamC
    A[final]= elemento
    
    contador += 1
    print (f"Elemento (contador) agregado a la cola: {elemento}")
    
    if contador < 10:
        respuesta = input("¿Desea agregar más elementos a la cola? (s/n): ").lower()
    if frente == final:
        print("La cola está vacía.") 
        exit(1)

primerElemento = A[(frente + 1) % MaxTamC] 
print("El primer elemento de la cola es: {primerElemento}")
frente=(frente+1)%MaxTamC
print("elementos de la cola en el orden de ingreso:  ")
i=(frente+1)%MaxTamC
while i!=(final+1)%MaxTamC:
    print(A[i], end="  ") 
    i = (i + 1) % MaxTamC
    i=(i+1)%MaxTamC
print()

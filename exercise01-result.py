listaRegistro = []
continuar = "si"
costototal= 0

while continuar == "si" :
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    costo = float(input("Costo ($0.00): "))
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    listaRegistro.append(registro)
    print("Si desea ingresar los datos de un nuevo cliente: Escriba 0 para continuar, caso contrario ingrese cualquier otro número")
    continuar= input("¿Desea continuar? ")
    costototal = costototal+costo

print("El costo total es: $"+str(costototal))


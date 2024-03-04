from os import system

def menu(): 
    print("---------------------------------------")
    print("MANEJO DE UNA CUENTA DE GASTOS")
    print("---------------------------------------")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("a. Agregar un depósito")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("b. Agregar un gasto") 
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("c. Consultar saldo") 
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("d. Salir")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    try:
        opcion = input("Escriba la opción que desee y presione enter: ")
        return opcion
    except ValueError:
        return opcion

listado_cuenta=[]
datos_cuenta={"fecha":"","tipo_de_transaccion":"","monto":""}

while True:
    system("cls")
    opcion_elegida=menu()
    if opcion_elegida== 1:
        print("ingrese una opcion valida de las qeu se muestran en el menu")
    elif opcion_elegida=="a":
        fecha=input("Ingrese la fecha de la transaccion: ")
        monto=float(input("Ingrese el monto del deposito: "))
        datos_cuenta["fecha"]= fecha
        datos_cuenta["tipo"]= "c"
        datos_cuenta["monto"]= monto
        listado_cuenta.append(datos_cuenta.copy())
        print("---------------------------------------")
        print("Depósito agregado exitosamente :)")
        print("---------------------------------------")
        input("precione enter para continuar...")
        print("---------------------------------------")

    elif opcion_elegida=="b":
        fecha= input("Ingresa la fecha de la transacción: ")
        monto= float(input("Ingresa el monto del gasto: "))
        datos_cuenta["fecha"]=fecha
        datos_cuenta["tipo"]="d"
        datos_cuenta["monto"]=monto
        listado_cuenta.append(datos_cuenta.copy())
        print("---------------------------------------")
        print("Gasto agregado exitosamente :)")
        print("---------------------------------------")
        input("precione enter para continuar...")
        print("---------------------------------------")

    elif opcion_elegida=="c":
        saldo=0
        for gasto in listado_cuenta:
            if gasto["tipo"]=="c":
                saldo+= gasto ["monto"]
            else:
                saldo-= gasto["monto"]
        print("---------------------------------------")        
        print(f"El saldo actual de su cuenta es: {saldo}")
        print("---------------------------------------")
        input("precione enter para continuar...")
        print("---------------------------------------")

    elif opcion_elegida=="d":
        print("---------------------------------------")
        print("¡ADIOS! :D")
        print("---------------------------------------")
        break



        
            



        
name = ""
lastname = ""
age = 0
phone = ""
address = ""
email = ""
opcion = ""

print("bienvenido al sistema de registro de cliente")
print("---------MENU PRINCIPAL---------")
print("1. Registrar cliente")
print("2. ver informacion del cliente")
print("3. borrar informacion del cliente")
print("4. modificar informacion del cliente")
print("5. salir")
print("---------------------------------")

opcion = int(input("selecciona una opcion: "))

match opcion:

    case 1:
        name = input("ingresa el nombre de el cliente: ")
        lastname = input("ingresa el apellido del cliente")
        age = int(input("ingresa la edad de el cliente: "))
        phone = input("ingresa el telefono de el cliente: ")
        address = input("ingresa la direccion del cliente: ")
        email = input("ingresa el correo electronico del cliente: ")

    case 2:
        print("nombre:", name, "apellido:", lastname, "edad:", age, "telefono:", phone, "direccion:", address, "correo:", email)   

    case 3:
        name = ""
        lastname = ""
        age = 0
        phone = ""
        address = ""
        email = ""
        print("informacion del cliente eliminada")
    case 4:
        name = input("ingresa el nuevo nombre del cliente: ")
        lastname = input("ingresa el nuevo apellido del cliente: ")
        age = int(input("ingresa la nueva edad del cliente: "))
        phone = input("ingresa el nuevo telefono de el cliente: ")
        address = input("ingresa la nueva direccion del cliente: ")
        email = input("ingresa el nuevo correo electronico de el cliente: ")

    case 5:
        print("¡hasta luego!")

    
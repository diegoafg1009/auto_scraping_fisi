from classes import *


def menu():
    while True:
        print("Bienvenido")
        print("==========")
        print("1. Iniciar Sesion")
        print("2. Registrarse")
        print("3. Salir")
        option = int(input("Ingrese una opcion: "))
        if option == 1:
            user_name = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contrasenia: ")
            if user_name == "admin" and password == "admin":
                sub_menu()
        elif option == 2:
            print("Opcion sin implementar, las credenciales de ingreso son: admin, admin")
        elif option == 3:
            print("Hasta pronto")
            # input("Presione Enter para continuar")
            break
        else:
            print("Esa opcion no existe, intentelo de nuevo")
            # input("Presione Enter para continuar")


def sub_menu():
    while True:
        print("Auto-Scraping FISI")
        print("==================")
        print("1. Realizar Busqueda")
        print("2. Cerrar Sesion")
        option = int(input("Ingrese una opcion: "))
        if option == 1:
            print("Ingrese los datos de su auto: ")
            search1 = SearchNeoAuto.input_attributes()
            autos = search1.get_autos()
            for auto in autos:
                print(f"Marca: {auto.get_brand()}\n Modelo: {auto.get_model()}\n Anio: {auto.get_year()} \n"
                      f" precio: {auto.get_price()} \n url: {auto.get_url()}")

        elif option == 2:
            print("Cerrando sesión...")
            # input("Presione Enter para continuar")
            break
        else:
            print("Esa opcion no existe, intentelo de nuevo")
            # input("Presione Enter para continuar")


if __name__ == '__main__':
    menu()


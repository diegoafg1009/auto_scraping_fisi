from classes import *


def menu():
    while True:
        print("Bienvenido")
        print("=================")
        print("1. Iniciar Sesion")
        print("2. Registrarse")
        print("3. Salir")
        option = int(input("Ingrese una opcion: "))
        if option == 1:
            user_id = User.login()
            if user_id is not False:
                sub_menu(user_id)
            else:
                print("No existe el usuario")
        elif option == 2:
            # print("Opcion sin implementar, las credenciales de ingreso son: admin, admin")
            print("Ingrese sus datos: ")
            User.register()
        elif option == 3:
            print("Hasta pronto")
            # input("Presione Enter para continuar")
            break
        else:
            print("Esa opcion no existe, intentelo de nuevo")
            # input("Presione Enter para continuar")


def sub_menu(user_id):
    while True:
        print("Auto-Scraping FISI")
        print("=========================================")
        print("1. Realizar Busqueda Neoauto")  # change
        print("2. Realizar Busqueda Kavak")  # change
        print("3. Realizar Busqueda Autopia")
        print("4. Realizar Busqueda en todas las tiendas")
        print("5. Mis favoritos")
        print("6. Modificar datos")
        print("7. Cerrar Sesion")

        option = int(input("Ingrese una opcion: "))
        if option == 1:
            print("Ingrese los datos de su auto: ")
            brand = input("Marca: ")
            model = input("Modelo: ")
            from_year = int(input("Anio inicial: "))
            until_year = int(input("Anio final: "))
            quantity = int(input("Cantidad de resultados por buscador: "))
            search = SearchNeoAuto(brand, model, from_year, until_year, quantity)
            autos = search.get_autos()
            if autos is not None:
                i = 1
                for auto in autos:
                    print(f"ID: [{i}]")
                    print(f"Marca: {auto.get_brand()}\n Modelo: {auto.get_model()}\n Anio: {auto.get_year()} \n"
                          f" precio: {auto.get_price()} \n url: {auto.get_url()}")
                    i += 1
                print(f"Se encontraron {len(autos)} resultados.")
                print("----------------")
                answer = input("¿Desea agregar un auto a sus favoritos?(s/n): ")
                if answer == 's' or answer == 'S':
                    id = int(input('Ingrese el id del auto: '))
                    autos[id - 1].add_favorite()

        elif option == 2:
            print("Ingrese los datos de su auto: ")
            brand = input("Marca: ")
            model = input("Modelo: ")
            from_year = int(input("Anio inicial: "))
            until_year = int(input("Anio final: "))
            quantity = int(input("Cantidad de resultados por buscador: "))
            search = SearchKavak(brand, model, from_year, until_year, quantity)
            autos = search.get_autos()
            if autos is not None:
                i = 1
                for car in autos:
                    print(f"ID: [{i}]")
                    print(f"Marca: {car.get_brand()}\n Modelo: {car.get_model()}\n Anio: {car.get_year()} \n"
                          f" Precio: {car.get_price()} \n url: {car.get_url()}")
                    print("----------------")
                    i += 1
                print(f"Se encontraron {len(autos)} resultados.")
                answer = input("¿Desea agregar un auto a sus favoritos?(s/n): ")
                if answer == 's' or answer == 'S':
                    id = int(input('Ingrese id del auto: '))
                    autos[id - 1].add_favorite()

        elif option == 3:
            autos = []
            print("Ingrese los datos de su auto: ")
            brand = input("Marca: ")
            model = input("Modelo: ")
            from_year = int(input("Anio inicial: "))
            until_year = int(input("Anio final: "))
            quantity = int(input("Cantidad de resultados por buscador: "))

            searchers = [SearchNeoAuto(brand, model, from_year, until_year, quantity),
                         SearchKavak(brand, model, from_year, until_year, quantity)]
            for search in searchers:
                autos.extend(search.get_autos())
            for car in autos:
                print(f"Marca: {car.get_brand()}\n Modelo: {car.get_model()}\n Anio: {car.get_year()} \n"
                      f" Precio: {car.get_price()} \n url: {car.get_url()}")
                print("----------------")
            print(f"Se encontraron {len(autos)} resultados.")

        elif option == 4:
            autos = []
            print("Ingrese los datos de su auto: ")
            brand = input("Marca: ")
            model = input("Modelo: ")
            from_year = int(input("Anio inicial: "))
            until_year = int(input("Anio final: "))
            quantity = int(input("Cantidad de resultados por buscador: "))

            searchers = [SearchNeoAuto(brand, model, from_year, until_year, quantity), SearchKavak(brand, model, from_year, until_year, quantity)]
            for search in searchers:
                autos.extend(search.get_autos())
            for car in autos:
                print(f"Marca: {car.get_brand()}\n Modelo: {car.get_model()}\n Anio: {car.get_year()} \n"
                      f" Precio: {car.get_price()} \n url: {car.get_url()}")

            print(f"Se encontraron {len(autos)} resultados.")
            answer = input("Desea agregar un auto a sus favoritos?(s/n)")
            if answer == 's' or answer == 'S':
                id = int(input('Ingrese el id del auto: '))
                autos[id - 1].add_favorite()

        elif option == 5:
            print("MIS FAVORITOS:")
            favorites = ConfigFile.get_favorites()
            for fav in favorites:
                print("Marca:", fav['brand'])
                print("Modelo:", fav['model'])
                print("Anio:", fav['year'])
                print("Precio:", fav['price'])
                print("Link:", fav['url'])
                print("-------------------------")

        elif option == 6:
            user = ConfigFile.get_user(user_id)
            user = User(user["_User__id"], user["_User__first_name"], user["_User__last_name"], user["_User__user_name"], user["_User__email"], user["_User__password"])
            user.modify_data()
        elif option == 7:
            print("Cerrando sesión...")
            # input("Presione Enter para continuar")
            break
        else:
            print("Esa opcion no existe, intentelo de nuevo")
            # input("Presione Enter para continuar")

if __name__ == '__main__':
    menu()

from classes import *


def show_menu_options():
    print("Bienvenido")
    print("=================")
    print("1. Iniciar sesion")
    print("2. Registrarse")
    print("3. Salir")
    return int(input("Ingrese una opcion: "))


def show_sub_menu():
    print("Auto-Scraping FISI")
    print("=========================================")
    print("1. Realizar busqueda en Neoauto")  # change
    print("2. Realizar busqueda en Kavak")  # change
    print("3. Realizar busqueda en Autopia")
    print("4. Realizar busqueda en todas las tiendas")
    print("5. Mis favoritos")
    print("6. Modificar datos")
    print("7. Cerrar sesion")
    return int(input("Ingrese una opcion: "))


def get_data_cars():
    dictionary = {}
    print("Ingrese los datos de su auto: ")
    dictionary['brand'] = input("Marca: ")
    dictionary['model'] = input("Modelo: ")
    dictionary['from_year'] = int(input("Anio inicial: "))
    dictionary['until_year'] = int(input("Anio final: "))
    dictionary['quantity'] = int(input("Cantidad de resultados por buscador: "))
    return dictionary


def search_neo_auto():
    data_car = get_data_cars()
    search = SearchNeoAuto(data_car['brand'], data_car['model'], data_car['from_year'], data_car['until_year'],
                           data_car['quantity'])
    autos = search.get_autos()
    return autos


def search_kavak():
    data_car = get_data_cars()
    search = SearchKavak(data_car['brand'], data_car['model'], data_car['from_year'], data_car['until_year'],
                         data_car['quantity'])
    autos = search.get_autos()
    return autos


def search_autopia():
    data_car = get_data_cars()
    search = SearchAutopia(data_car['brand'], data_car['model'], data_car['from_year'], data_car['until_year'],
                         data_car['quantity'])
    autos = search.get_autos()
    return autos


def search_all_stores():
    autos = []
    data_car = get_data_cars()
    searchers = [SearchNeoAuto(data_car['brand'], data_car['model'], data_car['from_year'], data_car['until_year'],
                         data_car['quantity']),
                 SearchKavak(data_car['brand'], data_car['model'], data_car['from_year'], data_car['until_year'],
                         data_car['quantity'])]
    for search in searchers:
        autos.extend(search.get_autos())
    return autos


def show_search_results(autos: list):
    if autos is not None:
        i = 1
        for auto in autos:
            print(f"ID: [{i}]")
            print(f"Marca: {auto.get_brand()}\n Modelo: {auto.get_model()}\n Anio: {auto.get_year()} \n"
                  f" Precio: {auto.get_price()} \n Url: {auto.get_url()}")
            i += 1
        print(f"Se encontraron {len(autos)} resultados.")
        print("----------------")


def show_option_add_favorite(autos: list, user_id):
    if autos is not None:
        answer = input("¿Desea agregar un auto a sus favoritos?(s/n): ")
        if answer == 's' or answer == 'S':
            id = int(input('Ingrese el id del auto: '))
            autos[id - 1].add_favorite(user_id)


def show_favorites(user_id):
    favorites = ConfigFile.get_favorites(user_id)
    if len(favorites) == 0:
        print("Usted aun no tiene autos favoritos agregados.")
    else:
        print("MIS FAVORITOS:")
        for fav in favorites:
            print("Marca:", fav['brand'])
            print("Modelo:", fav['model'])
            print("Anio:", fav['year'])
            print("Precio:", fav['price'])
            print("Link:", fav['url'])
            print("-------------------------")


def menu():
    while True:
        option = show_menu_options()
        if option == 1:
            user_id = User.login()
            if user_id is not False:
                sub_menu(user_id)
            else:
                print("No existe el usuario")
        elif option == 2:
            User.register()
        elif option == 3:
            print("Hasta pronto")
            break
        else:
            print("Esa opcion no existe, intentelo de nuevo")


def sub_menu(user_id):
    while True:
        option = show_sub_menu()
        if option == 1:
            cars_neo_auto = search_neo_auto()
            show_search_results(cars_neo_auto)
            show_option_add_favorite(cars_neo_auto, user_id)

        elif option == 2:
            cars_kavak = search_kavak()
            show_search_results(cars_kavak)
            show_option_add_favorite(cars_kavak, user_id)

        elif option == 3:
            cars_autopia = search_autopia()
            show_search_results(cars_autopia)
            show_option_add_favorite(cars_autopia, user_id)

        elif option == 4:
            cars_all_stores = search_all_stores()
            show_search_results(cars_all_stores)
            show_option_add_favorite(cars_all_stores, user_id)

        elif option == 5:
            show_favorites(user_id)

        elif option == 6:
            user = ConfigFile.get_user(user_id)
            user = User(user["_User__id"], user["_User__first_name"], user["_User__last_name"], user["_User__user_name"], user["_User__email"], user["_User__password"])
            user.modify_data()

        elif option == 7:
            print("Cerrando sesión...")
            break
        else:
            print("Esa opcion no existe, intentelo de nuevo")


if __name__ == '__main__':
    menu()

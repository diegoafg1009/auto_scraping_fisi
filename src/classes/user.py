import uuid
from .config_file import ConfigFile


class User:
    def __init__(self, id: str, first_name: str, last_name: str, user_name: str, password: str, email: str):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__password = password
        self.__email = email

    @staticmethod
    def register():
        id = str(uuid.uuid1())
        first_name = input("Ingrese sus nombres: ")
        last_name = input("Ingrese sus apellidos: ")
        user_name = input("Ingrese su nombre de usuario: ")
        email = input("Ingrese su email: ")
        password = input("Ingrese su contrasenia: ")
        new_user = {"_User__id": id, "_User__first_name": first_name, "_User__last_name": last_name, "_User__user_name": user_name, "_User__email": email, "_User__password": password}
        ConfigFile.save_user(new_user)
        
    @staticmethod
    def login():
        user_name = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contrasenia: ")
        users = ConfigFile.get_users()
        for user in users:
            if user["_User__user_name"] == user_name and user["_User__password"] == password:
                return user["_User__id"]
        return False

    def modify_data(self):
        while True:
            print("User name: " + self.get_user_name())
            print("password: ********")
            print("1. Modificar nombre de usuario")
            print("2. Modificar password")
            print("3. Volver al menu anterior")
            option = int(input("Ingrese una opcion: "))
            if option == 1:
                old_user_name = self.__user_name
                user_name = input("Ingrese su nuevo nombre de usuario: ")
                self.set_user_name(user_name)
                if ConfigFile.modify_user(self.__dict__, self.__id, "user_name") is False:
                    self.set_user_name(old_user_name)
            elif option == 2:
                password = input("Ingrese su nueva contrasenia: ")
                self.set_password(password)
                if ConfigFile.modify_user(self.__dict__, self.__id, "password") is False:
                    self.set_user_name(old_user_name)
            elif option == 3:
                print("Volviendo...")
                break

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

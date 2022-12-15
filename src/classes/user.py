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
            print("Nombre: " + self.get_first_name())
            print("Apellido: " + self.get_last_name())
            print("Nombre de usuario: " + self.get_user_name())
            print("Correo electronico: " + self.get_email())
            print("Contrasenia: ********")
            print("1. Modificar nombres")
            print("2. Modificar apellidos")
            print("3. Modificar nombre de usuario")
            print("4. Modificar email")
            print("5. Modificar password")
            print("6. Volver al menu anterior")
            option = int(input("Ingrese una opcion: "))

            if option == 1:
                old_first_name = self.__first_name
                first_name = input("Ingrese su nuevo nombre: ")
                self.set_first_name(first_name)
                if ConfigFile.modify_user(self.__dict__, self.__id, "first_name") is False:
                    self.set_user_name(old_first_name)

            elif option == 2:
                old_last_name = self.__last_name
                last_name = input("Ingrese su nuevo apellido: ")
                self.set_last_name(last_name)
                if ConfigFile.modify_user(self.__dict__, self.__id, "last_name") is False:
                    self.set_user_name(old_last_name)

            elif option == 3:
                old_user_name = self.__user_name
                user_name = input("Ingrese su nuevo nombre de usuario: ")
                self.set_user_name(user_name)
                if ConfigFile.modify_user(self.__dict__, self.__id, "user_name") is False:
                    self.set_user_name(old_user_name)

            elif option == 4:
                old_email = self.__email
                email = input("Ingrese su correo electronico: ")
                self.set_email(email)
                if ConfigFile.modify_user(self.__dict__, self.__id, "email") is False:
                    self.set_email(old_email)

            elif option == 5:
                password = input("Ingrese su nueva contrasenia: ")
                self.set_password(password)
                if ConfigFile.modify_user(self.__dict__, self.__id, "password") is False:
                    self.set_user_name(old_user_name)

            elif option == 6:
                print("Volviendo...")
                break

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

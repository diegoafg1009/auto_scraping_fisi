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
        new_user = {"id": id, "first_name": first_name, "last_name": last_name, "user_name": user_name, "email": email, "password": password}
        ConfigFile.save_user(new_user)
        
    @staticmethod
    def login():
        user_name = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contrasenia: ")
        users = ConfigFile.get_users()
        for user in users:
            if user["user_name"] == user_name and user["password"] == password:
                return True




    def modify_data(self):
        pass


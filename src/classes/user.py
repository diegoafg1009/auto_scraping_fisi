from .config_file import ConfigFile

class User:
    def __init__(self, first_name: str, last_name: str, user_name: str, password: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__password = password
        self.__email = email

    @staticmethod
    def register():
        first_name = input("Ingrese sus nombres: ")
        last_name = input("Ingrese sus apellidos: ")
        user_name = input("Ingrese su nombre de usuario: ")
        email = input("Ingrese su email: ")
        password = input("Ingrese su contrasenia: ")
        
        newUser = {"name": first_name, "last_name": last_name, "user_name": user_name, "email": email, "password": password}
        fileUserName = "usuario.json"
        ConfigFile.save_user(newUser, fileUserName)
        

    def login(self):
        user_name = input()
        contrasenia = input()


    def modify_data(self):
        pass


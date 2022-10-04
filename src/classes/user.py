class User:
    def __init__(self, first_name: str, last_name: str, user_name: str, password: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__password = password
        self.__email = email

    @classmethod
    def register(cls):
        first_name = input("Ingrese sus nombres: ")
        last_name = input("Ingrese sus apellidos: ")
        user_name = input("Ingrese su contrasenia: ")
        email = input("Ingrese su email: ")
        cls(first_name, last_name, user_name, email)

    def login(self):
        user_name = input()
        contrasenia = input()


    def modify_data(self):
        pass


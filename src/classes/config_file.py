import json


class ConfigFile:
    USER_PATH = "usuario.json"
    FAVORITE_PATH = "favoritos.json"

    @staticmethod
    def save_user(new_json_user):
        with open(ConfigFile.USER_PATH, 'r+') as file:
            already_exist = False
            users = json.load(file)
            for user in users:
                if user["user_name"] == new_json_user["user_name"]:
                    already_exist = True
                    print("Lo sentimos, el nombre de usuario ingresado ya existe. No se pudo registrar")
                    break
                elif user["email"] == new_json_user["email"]:
                    already_exist = True
                    print("Lo sentimos, el email ingresado ya se encuentra en uso. No se pudo registrar")
                    break
            if not already_exist:
                users.append(new_json_user)
                file.seek(0)
                json.dump(users, file, indent=4)
                print("Felicidades, se registro existosamente")

    @staticmethod
    def save_favorite(new_json_favorite):
        with open(ConfigFile.FAVORITE_PATH, 'r+') as file:
            already_exist = False
            favorites = json.load(file)
            for favorite in favorites:
                if favorite["url"] == new_json_favorite["url"]:
                    already_exist = True
                    print("El auto ya se encuentra en sus favoritos")
                    break
            if not already_exist:
                favorites.append(new_json_favorite)
                file.seek(0) #(offset, from_what)
                json.dump(favorites, file, indent=4)
                print("Se agregó a sus favoritos correctamente!")



    @staticmethod
    def get_users():
        with open(ConfigFile.USER_PATH, 'r') as file:
            users = json.load(file)
        return users

    @staticmethod
    def get_favorites():
        with open(ConfigFile.FAVORITE_PATH, 'r') as file:
            favorites = json.load(file)
        return favorites


    def get_info_user(self, fileName: str):
        pass

    def save_info_auto(self, filename):
        pass

    def get_info_auto(self, fileName):
        pass
    
    

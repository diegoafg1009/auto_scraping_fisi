import json


class ConfigFile:
    USER_PATH = "data_persistence/usuario.json"
    FAVORITE_PATH = "data_persistence/favoritos.json"

    @staticmethod
    def save_user(new_json_user):
        with open(ConfigFile.USER_PATH, 'r+') as file:
            already_exist = False
            users = json.load(file)
            for user in users:
                if user["_User__user_name"] == new_json_user["_User__user_name"]:
                    already_exist = True
                    print("Lo sentimos, el nombre de usuario ingresado ya existe. No se pudo registrar")
                    break
                elif user["_User__email"] == new_json_user["_User__email"]:
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

    @staticmethod
    def get_user(id):
        users = ConfigFile.get_users()
        for user in users:
            if user["_User__id"] == id:
                return user

    @staticmethod
    def modify_user(json_user, id, key):
        i = 0
        with open(ConfigFile.USER_PATH, 'r+') as file:
            users = json.load(file)
            if key == "user_name":
                for user in users:
                    if user["_User__user_name"] == json_user["_User__user_name"]:
                        print("Lo sentimos, el nombre de usuario ingresado ya existe. No se pudo modificar")
                        return False
                    elif user["_User__id"] == id:
                        index = i
                    i = i + 1
            elif key == "email":
                for user in users:
                    if user["_User__email"] == json_user["_User__email"]:
                        print("Lo sentimos, el email ingresado ya se encuentra en uso. No se pudo modificar")
                        return False
                    elif user["_User__id"] == id:
                        index = i
                    i = i + 1
            else:
                for user in users:
                    if user["_User__id"] == id:
                        index = i
                    i = i + 1
            users[index] = json_user
            file.seek(0)
            json.dump(users, file, indent=4)
            print("Felicidades, se modifico existosamente")
            return True

    
    

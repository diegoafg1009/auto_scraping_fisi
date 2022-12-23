import json


class ConfigFile:
    USER_PATH = "data_persistence/users.json"
    FAVORITE_PATH = "data_persistence/favorites.json"
    USERS_FAVORITES_PATH = "data_persistence/users_favorites.json"

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
    def save_favorite(new_json_favorite, user_id):
        with open(ConfigFile.FAVORITE_PATH, 'r+') as favorites_file:
            already_exist_in_favorites = False
            favorites = json.load(favorites_file)
            for favorite in favorites:
                if favorite["url"] == new_json_favorite["url"]:
                    already_exist_in_favorites = True
                    favorite_id = favorite["id"]
                    break
            if not already_exist_in_favorites:
                favorites.append(new_json_favorite)
                favorites_file.seek(0)
                json.dump(favorites, favorites_file, indent=4)
        with open(ConfigFile.USERS_FAVORITES_PATH, 'r+') as users_favorites_file:
            already_exist_in_users_favorites = False
            users_favorites = json.load(users_favorites_file)
            if not already_exist_in_favorites:
                users_favorites.append({"user_id": str(user_id), "favorite_id": new_json_favorite["id"]})
                users_favorites_file.seek(0)
                json.dump(users_favorites, users_favorites_file, indent=4)
                print("Se agrego existosamente el auto a sus favoritos")
            else:
                for uf in users_favorites:
                    if uf["user_id"] == user_id and uf["favorite_id"] == favorite_id:
                        already_exist_in_users_favorites = True
                        print("El auto ya se encuentra en sus favoritos")
                        break
                if not already_exist_in_users_favorites:
                    users_favorites.append({"user_id": str(user_id), "favorite_id": str(favorite_id)})
                    users_favorites_file.seek(0)
                    json.dump(users_favorites, users_favorites_file, indent=4)
                    print("Se agrego existosamente el auto a sus favoritos")

    @staticmethod
    def get_users():
        with open(ConfigFile.USER_PATH, 'r') as file:
            users = json.load(file)
        return users

    @staticmethod
    def get_favorites(user_id):
        with open(ConfigFile.USERS_FAVORITES_PATH, "r") as users_favorites_file:
            users_favorites = json.load(users_favorites_file)
            favorites_id = []
            for uf in users_favorites:
                if uf["user_id"] == user_id:
                    favorites_id.append(uf["favorite_id"])
        with open(ConfigFile.FAVORITE_PATH, 'r') as favorites_file:
            expected_results = len(favorites_id)
            all_favorites = json.load(favorites_file)
            cars = []
            i = 0
            for favorite in all_favorites:
                if favorite["id"] in favorites_id:
                    cars.append(favorite)
                    i = i + 1
                if i == expected_results:
                    break
        return cars

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

    
    

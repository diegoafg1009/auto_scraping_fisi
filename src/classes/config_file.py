import json

class ConfigFile:
    def __int__(self):
        __path = ""
    @staticmethod
    def save_user(newJsonUser, fileName):
        with open(fileName, 'r+') as file:
            newJson = json.load(file)
            newJson["user_details"].append(newJsonUser)
            file.seek(0)
            json.dump(newJson, file, indent=4)

    def get_info_user(self, fileName: str):
        pass

    def save_info_auto(self, filename):
        pass

    def get_info_auto(self, fileName):
        pass
    
    

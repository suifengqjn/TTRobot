import os
import json
class SingletonCon():

    toutiao_cookie_list = None
    config = None
    article = None
    img = None
    def __init__(self):
        self.__readConfig()

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(SingletonCon, "_instance"):
            SingletonCon._instance = SingletonCon(*args, **kwargs)
        return SingletonCon._instance

    def __readConfig(self):
        cur_path = os.getcwd()
        cookie_path = cur_path + "/source/toutiao_cookie.json"
        print(cookie_path)
        with open(cookie_path, 'r') as f:
            data = json.load(f)
            print("single __readConfig",data)
            self.toutiao_cookie_list = data

        config_path = cur_path + "/source/config.json"
        with open(config_path, 'r') as f:
            data = json.load(f)
            print("single __readConfig",data)
            self.config = data

        self.article = self.config["article"]
        self.img = self.config["img"]

    @property
    def cookieString(self):
        res = ''
        for d in self.toutiao_cookie_list:
            if 'name' in d and 'value' in d :
                temp = d["name"] + "=" + d["value"]
                res += repr(temp)
                res += ";"

        res = res.rstrip(";")
        return res



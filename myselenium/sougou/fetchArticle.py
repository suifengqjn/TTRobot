from myselenium.sougou import article, keyWords
import random
from common import kvStore
from projectCon import global_con



class Fetch():
    word_index = 0

    title_limit = global_con.SingletonCon.instance().article["title_limit"]
    image_limit = global_con.SingletonCon.instance().img["image_limit"]
    txt_limit = global_con.SingletonCon.instance().article["content_limit"]
    days_limit = global_con.SingletonCon.instance().article["days_limit"]

    def __init__(self):
        super().__init__()

    def img_txt_count(self, s) -> (int, int, list):
        if '||' not in s:
            return 0, 0, []
        arr = s.split('||')
        t_count = 0
        i_count = 0
        res_arr = []
        for a in arr:
            if a.startswith("pp--"):
                t_count += len(a) - 4
                res_arr.append(a[4:])
            elif a.startswith("im--"):
                i_count += 1
                res_arr.append(a[4:])


        with open("./art.txt", "a+") as f:
            f.write("==============================\n")
            print("==============================")
            for a in res_arr:
                print(a)
                f.writelines(a)
                f.writelines("\n")
            print("==============================")
            f.write("==============================\n")

        return (t_count, i_count, res_arr)

    def exist(self, md5) -> bool:
        v = kvStore.get(md5)
        if v != None:
            return True
        return False

    def check_article(self, dict) -> bool:

        print("check_article",type(dict), dict)
        if dict == None or "md5" not in dict:
            return False

        md5 = dict["md5"]
        if kvStore.get(md5) != None:
            return False
        title = dict["title"]
        if len(title) < self.title_limit:
            return False

        content = dict["content"]
        tc, ic, con = self.img_txt_count(content)
        if tc < self.txt_limit or ic < self.image_limit:
            return False

        return True

    def format_article(self, dict):

        v = self.img_txt_count(dict["content"])

        dict["content"] = v[2]

        return dict

    def fetch_article(self) -> dict:
        words = keyWords.fetch_keywords()
        if self.word_index >= len(words) - 1:
            self.word_index = 0

        self.word_index = random.randint(0, len(words)-1)
        word = words[self.word_index]

        dict = article.fetch_article_with_selector(query=word,days_limit=self.days_limit, func=self.check_article)
        print("---", dict)
        if dict != None and "md5" in dict:
            kvStore.set(dict["md5"], "1")
        self.word_index += 1
        return dict


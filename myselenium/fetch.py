
from myselenium.fetch import keyWords
from myselenium.fetch import article
import random
from common import kvStore

title_limit = 10
image_limit = 6
txt_limit = 400

def img_txt_count(s) -> (int, int, list):
    arr = s.spit('||')
    t_count = 0
    i_count = 0
    res_arr = []
    for a in arr :
        if s.startswith("pp--"):
            t_count += len(a) - 4
            res_arr.append(a[4:])
        elif s.startswith("im__"):
            i_count += 1
            res_arr.append(a[4:])
    return (t_count, i_count, res_arr)

def exist(md5)->bool:
    v = kvStore.get(md5)
    if v != None:
        return True
    return False

def fetch_articles() -> dict:
    words = keyWords.fetch_keywords()
    index = random.randint(0, len(words))
    word = words[index]

    articles = article.fetch_article(word, None)

    for ar in articles:
        dict = ar.__dict__

        md5 = dict["md5"]
        if kvStore.get(md5) != None :
            continue
        title = dict["title"]
        if len(title) < title_limit:
            continue

        content = dict["content"]
        tc, ic, con = img_txt_count(content)
        if tc < txt_limit or ic < image_limit:
            continue

        param = {}
        param["title"] = title
        param["content"] = con
        param["md5"] = dict["md5"]
        param["cover_image"] = dict["cover_image"]

        kvStore.set(md5,"1")

        return param




from myselenium.fetch import keyWords
from myselenium.fetch import article
import random

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


def fetch_articles() -> dict:
    words = keyWords.fetch_keywords()
    index = random.randint(0, len(words))
    word = words[index]

    articles = article.fetch_article(word, None)

    for ar in articles:
        dict = ar.__dict__
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

        return param



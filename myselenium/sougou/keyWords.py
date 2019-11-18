
import requests
from common import kvStore
index = 0
def getRandomKeyWords():

    words = fetch_keywords()
    global  index

    v = kvStore.get("word_index")
    if v != None:
        index = v


    print(index)
    if index >= len(words):
        index = -1

    while True:
        if index == len(words):
            word = "最新电影推荐"
            break
        word = words[index]
        if kvStore.get(word) != None:
            index += 1
        else:
            break

    index += 1
    kvStore.set(word, "1")
    kvStore.set("word_index", index)
    return word



def fetch_keywords():

    url = "http://106.12.220.252:8765/hot_words"
    response = requests.get(url)
    data = response.json()
    if data != None and data["code"] == 1:
        return data["data"]
    else:
        return [
            "2019高分喜剧电影",
            "2019高分科幻电影",
            "2019高分国产剧",
            "2019高分日韩剧",
            "2019高分欧美剧",
            "2019高分战争电影",
            "2019高分悬疑电影",
             "2019高分动作电影"]



if __name__ == "__main__":
    for i in range(1):
        print(getRandomKeyWords())

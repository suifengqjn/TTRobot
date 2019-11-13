
import threading

queryList = []

def time_fetch_keyword():
    fetch_keywords()
    global fetch_keyword_timer
    fetch_keyword_timer = threading.Timer(60*60*8, time_fetch_keyword)#
    fetch_keyword_timer.start()

def fetch_keywords():
    return ["11月电影推荐"]
    return [
            "2019高分喜剧电影",
            "2019高分科幻电影",
            "2019高分国产剧",
            "2019高分日韩剧",
            "2019高分欧美剧",
            "2019高分战争电影",
            "2019高分悬疑电影",
             "2019高分动作电影"]

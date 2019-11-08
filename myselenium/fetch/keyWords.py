
import threading

queryList = []

def time_fetch_keyword():
    fetch_keywords()
    global fetch_keyword_timer
    fetch_keyword_timer = threading.Timer(60*60*8, time_fetch_keyword)#
    fetch_keyword_timer.start()

def fetch_keywords():
    return ["2019高分动作电影","2019高分悬疑电影"]

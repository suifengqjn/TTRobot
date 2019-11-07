
import threading

queryList = []

def time_fetch_keyword():
    fetch_keywords()
    global fetch_keyword_timer
    fetch_keyword_timer = threading.Timer(60*60*8, time_fetch_keyword)#
    fetch_keyword_timer.start()

def fetch_keywords():
    return ["哪咤电影影评","蔡依林阿信跳舞"]
    pass
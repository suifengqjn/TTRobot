import datetime

def isNight()->bool:
    now = datetime.datetime.now()
    if now.hour > 22 or now.hour < 6:
        return True
    return False
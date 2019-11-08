import hashlib

def Md5(s):
    return hashlib.md5(s.encode("utf8")).hexdigest()
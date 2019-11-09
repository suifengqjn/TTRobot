import hashlib
import difflib

def Md5(s):
    return hashlib.md5(s.encode("utf8")).hexdigest()




#判断相似度的方法，用到了difflib库
def get_string_equal_rate(str1, str2):
   return difflib.SequenceMatcher(None, str1, str2).quick_ratio()
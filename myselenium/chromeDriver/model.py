import hashlib
class wx_article:
    keyword = ""
    title = ""
    content = ""
    cover_image = ""
    md5 = ""


    def getMd5(self, s):

        return hashlib.md5(s.encode("utf8")).hexdigest()


if __name__ == "__main__":
    wx = wx_article()
    m = wx.getMd5("aaa")
    print(m, type(m))
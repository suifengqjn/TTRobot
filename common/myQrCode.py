import zxing



def isQrCodeImg(img)->bool:
    reader = zxing.BarCodeReader()
    res = reader.decode(img)
    if res == None:
        return False
    return True


def image_detect():
    reader = zxing.BarCodeReader()
    res = reader.decode("/Users/qianjianeng/Desktop/1.png")
    print("result",res.type, res.points)

    res = reader.decode("/Users/qianjianeng/Desktop/2.png")
    if res == None:
        print("none")
    else:
        print("result", res.type, res.points)


    url = "https://ask.qcloudimg.com/http-save/yehe-1557172/avyffe4grc.png?imageView2/2/w/1620"
    res = reader.decode(url)
    print(res)

if __name__ == "__main__":
    v = isQrCodeImg("https://mmbiz.qpic.cn/mmbiz_jpg/ggI6C4WmicXiaH6dWTv86mcRRSXOfsKRl9Djll1tjQrtovpwzWydbEO0PMHErCegxiaialabIIYAJBIcNEHicFMby8g/640?wx_fmt=jpeg")

    print(v)
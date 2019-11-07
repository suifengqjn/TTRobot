from urllib import request
from bs4 import BeautifulSoup as BS
import re


def get_duanzi()-> dict:

    for i in range(1, 51):
        res = __getPageInfo("http://www.budejie.com/pic/" + str(i))
        d = {}
        for r in res:
            if len(r["mark"]) > 15 and "img" in r :
                d = r
                break

        return d




def __getPageInfo(url):
    cnt = 0
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    html = request.Request(url, headers=headers)
    html = request.urlopen(html)
    bsObj = BS(html, "lxml")

    itemList = bsObj.findAll("li")
    # print(itemList)
    data = {}
    print("------------------------")
    res = []
    for item in itemList:
        for tmp1 in item.findAll("div", {"class": "j-list-user"}):
            # print("tmp1 {}".format(tmp1))
            dict = {}
            try:
                writer = tmp1.find("a", {"class": "u-user-name"})
                userId = writer.attrs['href']
                # print("type is {} content is {}".format(type(userId), re.findall(r"-(\d+).html", userId)))
                data['userId'] = re.findall(r"-(\d+).html", userId)[0]
                data['writer'] = writer.get_text()
                data['pub_time'] = tmp1.find("span", {"class": "u-time f-ib f-fr"}).get_text()

                data['mark'] = item.find("div", {"class": "j-r-list-c-desc"}).find("a").get_text()

                data['agreeNum'] = item.find("li", {"class": "j-r-list-tool-l-up"}).find("span").get_text()
                data['disagreeNum'] = item.find("li", {"class": "j-r-list-tool-l-down"}).find("span").get_text()

                data['markNum'] = item.find("span", {"class": "comment-counts"}).get_text()

                data['shareNum'] = item.find("div", {"class": "j-r-list-tool-ct-share-c"}).find("span").get_text()
                data['shareNum'] = re.findall("(\d)+", data['shareNum'])[0]
                # picUrl = item.find("img", {"src":re.compile(r"[]+\.(jpg|png|gift)")})
                # print("___- {}".format("\[^]+\.(jpg\|png\|gift)"))
                picUrl = item.find("div", {"class": "j-r-list-c-img"})
                data['portrait'] = item.find("div", {"class": "j-list-user"}).img.attrs['data-original']

                print("作者：{}, ID:{} ,发表时间: {}".format(data['writer'], data['userId'], data['pub_time']))
                print("他的头像是: {}".format(data['portrait']))
                print("说了: {}".format(data['mark']))
                print("支持的人数有{}人，反对的人数有{}人".format(data['agreeNum'], data["disagreeNum"]))
                print("有{}人参与了评论,{}人将它分享了出去".format(data["markNum"], data["shareNum"]))
                dict['mark'] = data['mark']
                dict['up'] = data['agreeNum']


                if (picUrl is not None):
                    # picUrl.find(re.compile("<img [A-Za-z0-9\.\\\\/]+ >"))
                    data["picUrl"] = picUrl.img.attrs["data-original"]

                    if (picUrl is not None):
                        print("他还发表了图片: {}".format(data["picUrl"]))
                        dict["img"] = data["picUrl"]
                print("")
                res.append(dict)
                cnt += 1
            except Exception as e:
                print(e)


    print("在URL= {}，爬取了 {} 条信息\n".format(url, cnt))
    return res



if __name__ == '__main__':


    print(get_duanzi())
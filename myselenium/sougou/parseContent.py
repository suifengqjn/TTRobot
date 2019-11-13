from myselenium.chromeDriver import chrome
from myselenium.sougou import bsoup
from common import util

class Sougou:
    def __init__(self):
        pass

    # 获取文章详情
    def GetPageContent(self, chr:chrome.ChromeDrive, main_window, link_title) :

        handles = chr.driver.window_handles
        for h in handles:
            if h != main_window:
                chr.driver.switch_to.window(h)
                break
        title = chr.driver.title
        if len(title) == 0:
            title = link_title


        # title filter

        print("current title", title)
        if len(title) == 0:
            return None

        ele = chr.driver.find_element_by_xpath('//div[@id="js_content"]')
        if ele != None:
            return self.__dealContent(ele, title)

        ele = chr.driver.find_element_by_xpath('//div[@class="rich_media_content"]')
        if ele != None:
            self.__dealContent(ele, title)





        # try:
        #     ele = chrome.driver.find_element_by_xpath('//div[@id="js_content"]')
        #     return self.__dealContent(ele, title)
        # except:
        #     print("no find js_content")
    # def __find_rich_media_content(self, chr, title):
    #     try:
    #         ele = chr.driver.find_element_by_xpath('//div[@class="rich_media_content"]')
    #         return self.__dealContent(ele, title)
    #     except Exception:
    #         pass
    #     return model.wx_article()
    # def __find_js_content(self, chr, title):
    #     try:
    #         ele = chr.driver.find_element_by_xpath(r'//[@id="js_content"]')
    #         return self.__dealContent(ele, title)
    #     except Exception:
    #         pass
    #     return model.wx_article()
    #
    # def __find_class_media_content(self, chr, title:str):
    #     try:
    #         ele = chr.driver.find_element_by_class_name('rich_media_content')
    #         return self.__dealContent(ele, title)
    #     except Exception:
    #         pass
    #     return model.wx_article()

    def __dealContent(self, element,title):

        print("-----deal content")
        #pArr = []

        #print(print(element.get_attribute('innerHTML')))
        #ps = element.find_element_by_css_selector("p")
        html = element.get_attribute('innerHTML')
        content, cover_img = bsoup.ParseEle(html)

        res = {}
        if len(title) > 0:
            res["title"] = title
        if len(content) > 0:
            res["content"] = content
        if len(cover_img) > 0:
            res["cover_image"] = cover_img
        res["md5"] = util.Md5(content)

        return res

    # def __formatHtml(self, arr):
    #
    #     res = []
    #     for str in arr:
    #         if str.startswith("http"):
    #             res.append(self.__formatImg(str))
    #             # htmlStr += self.__formatImg(str)
    #         elif len(str)>1:
    #             res.append(self.__formatP(str))
    #             # htmlStr += self.__formatP(str)
    #
    #     return "||".join(res)
    #     #return "<div>{}</div>".format(htmlStr)
    #
    # def __formatP(self, str):
    #     return "pp--{}".format(str)
    #     #return "<p>{}</p>\n".format(str)
    # def __formatImg(self, str):
    #     return "im--{}".format(str)
    #     #return "<div class=\"pgc-img\"><img class=\"\" src=\"{}\" data-ic=\"false\" data-ic-uri=\"\" data-story_id=\"\" data-image_ids=\"[]\" image_type=\"1\" mime_type=\"image/jpeg\"></div>\n".format(str)

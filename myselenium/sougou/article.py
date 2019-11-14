
import time

from myselenium.chromeDriver import chrome
from myselenium.sougou import parseContent, filter
from urllib import parse
from datetime import datetime
import random

def fetch_article_with_selector(query,days_limit, func):
    chr = chrome.ChromeDrive()
    # 首页句柄
    mainHandle = chr.driver.current_window_handle
    article = None
    for index in range(1, 10):
        url = get_page_urls(query, index)
        print("------", url)
        article = get_article_with_url_by_selector(url, chr, mainHandle,days_limit func)
        if article != None:
            break

    chr.driver.quit()
    return article

def fetch_articles(query, sql):

    chr = chrome.ChromeDrive()
    # 首页句柄
    mainHandle = chr.driver.current_window_handle
    res = []
    for index in range(1, 10):
        url = get_page_urls(query, index)
        print("------",url)
        arr = get_articles_with_url(url, chr,mainHandle)
        if sql != None:
            sql.insert_articles(arr)
        res += arr

    chr.driver.quit()
    return res

def get_page_urls(query, page_index):
    query = parse.quote(query)
    if page_index == 1:
        url = "https://weixin.sogou.com/weixin?type=2&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(query)
        return url
    else:
        str = "https://weixin.sogou.com/weixin?query=" + query

        return "{}&_sug_type_=&s_from=input&_sug_=n&type=2&page={}&ie=utf8".format(str, page_index)

# 获取一个列表页面的所有文章
def get_articles_with_url(url,chr,mainHandle):
    chr.driver.get(url)
    time.sleep(2)

    divs = chr.driver.find_elements_by_xpath("//div[@class=\"txt-box\"]")

    res = []
    sg = parseContent.Sougou()
    for div in divs:
        # print(divs[i].get_attribute("href"))
        # print(divs[i].text)
        #
        # print(div.get_attribute('innerHTML'))
        time.sleep(3)
        #
        # print("a title")
        #
        # print(divs[i].find_element_by_tag_name("h3").text)

        try:
            link_title = div.find_element_by_tag_name("h3").text
            # a = divs[i].find_element_by_tag_name("a")
            # url = a.get_attribute("href")
            # print(url)

            link = chr.driver.find_element_by_link_text(link_title)
            print("link title", link_title)
            link.click()
            time.sleep(random.randint(1,5))

            content = sg.GetPageContent(chr, mainHandle,link_title)
            if len(content.title) > 6 and len(content.content) > 10:
                res.append(content)

            time.sleep(random.randint(2,8))
        except Exception:
            print('element does not exist')

        finally:
            chr.CloseOtherWindow(mainHandle)



    return res


# 获取一个列表页面的满足条件文章
def get_article_with_url_by_selector(url, chr, mainHandle, dayslimit, func):
    chr.driver.get(url)
    time.sleep(2)

    divs = chr.driver.find_elements_by_xpath("//div[@class=\"txt-box\"]")

    content = None
    sg = parseContent.Sougou()
    for div in divs:

        time.sleep(3)
        content = None
        skip = False
        try:
            # 获取时间
            time_txt = div.find_element_by_class_name("s2").text
            if "-" in time_txt:
                try:
                    t = datetime.strptime(time_txt, '%Y-%m-%d')
                    cha = (datetime.now() - t).days
                    print("time", cha)
                    if cha > dayslimit:
                        skip = True
                    else:
                        skip = False
                except Exception:
                    skip = False


            if skip == True:
                continue

            link_title = div.find_element_by_tag_name("h3").text

            if filter.title_filter_pass(link_title) == False:
                continue

            link = chr.driver.find_element_by_link_text(link_title)
            print("link title", link_title)
            link.click()
            time.sleep(random.randint(1, 5))

            content = sg.GetPageContent(chr, mainHandle, link_title)

            time.sleep(random.randint(2, 8))
        except:
            print('element does not exist')

        finally:
            chr.CloseOtherWindow(mainHandle)

        if func(content) == True:
            break

    return content

from myselenium.chromeDriver import chrome
import time
from projectCon import global_con
from bs4 import BeautifulSoup
from common import util
baidu = "http://www.baidu.com"

# 搜索头条是否存在类似的文章
# https://www.toutiao.com/search/?keyword=2019%E6%81%90%E6%80%96%E7%89%87%E6%8E%92%E8%A1%8C%E6%A6%9C%E5%89%8D%E5%8D%81%E5%90%8D%E8%B1%86%E7%93%A3%20%E6%9C%80%E6%96%B0%E9%AB%98%E5%88%86%E6%81%90%E6%80%96%E7%94%B5%E5%BD%B1%E6%8E%A8%E8%8D%90

def __get_search_url(word):

    return "https://www.toutiao.com/search/?keyword=" + word




def search_keyword(word, similar)->bool:

    chr = chrome.ChromeDrive()
    chr.driver.get(baidu)
    time.sleep(2)

    con = global_con.SingletonCon.instance()
    for c in con.toutiao_cookie_list:
        chr.driver.add_cookie(c)

    time.sleep(1)
    chr.driver.get(__get_search_url(word))

    #等待网页加载完毕
    time.sleep(10)

    # # 向下滚动
    # chr.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(5)
    html = chr.driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.select('div[class="title-box"]')

    for div in divs:
        title = div.get_text()
        print(title)

        sili = util.get_string_equal_rate(title, word)
        if sili > similar:
            chr.driver.quit()
            return True
        print(sili)

    chr.driver.quit()
    return False





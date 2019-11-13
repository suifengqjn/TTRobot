
from component.toutiao import TTBot
from myselenium.sougou import fetchArticle
from myselenium.search import toutiao
import random
import time
import datetime

from task import bgTask


def publishArt(account):
    print("art...")
    fe = fetchArticle.Fetch()
    while True:
        art_dic = fe.fetch_article()
        if art_dic == None:
            continue
        art_dic = fe.format_article(art_dic)

        title = art_dic["title"]
        if toutiao.search_keyword(title, 0.8) == False:
            content_arr = art_dic["content"]
            coverImage = art_dic["cover_image"]
            con = account.format_content(content_arr)
            account.post_article(title=title,
                                 content=con,
                                 run_ad=True,
                                 cover_img=coverImage)
            break




def pub_video():
    print("pub video")


if __name__ == "__main__":
    print("tt robot running...")

    bot = TTBot()
    account = bot.account

    print(account.name)
    print(account._account_info)
    print(account.media_info)


    # 后台任务
    bg = bgTask.BgTask(account)
    bg.run()

    index = 1
    while True:

        now = datetime.datetime.now()
        if now.hour > 23 or now.hour < 6:
            continue

        if index == 1:
            publishArt(account)
        elif index == 2:
            pub_video()

        index += 1

        if index > 2:
            index = 1

        r = random.randint(30, 60)
        time.sleep(r * 60)



    # media_id = '6754524947554501134'
    # comment_content = '阅读量只有1'
    #
    # res = account.post_comment(comment_content, media_id)
    # print(res)
    #
    # comments = account.get_comments_of_media('6689315272605565452')
    # print(comments)


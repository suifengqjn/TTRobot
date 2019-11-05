
from component.toutiao import TTBot

def publishArt(account):
    arr = [
        "今天（11月3日）下午，根据丹阳市人民法院公告显示，锤子科技罗永浩被执行限制消费令。",

        "其实，这不是第一例锤子科技（北京）股份有限公司成被告，经查询中国裁判文书网，锤子科技（北京）股份有限公司及其下属企业北京锤子数码科技有限公司，自今年以来，已因买卖合同纠纷被多家公司告到法院。",

        "这里面，大多是这些公司向锤子科技或者锤子数码两家公司提供设备，但这些公司长期没有收到货款，每一笔其实金额都不是很大，有70多万，有170多万等。",

        "其实，随着官司的增多，罗永浩并不是第一次收到法院发出的限制消费令。",

        "https://mmbiz.qpic.cn/mmbiz_jpg/GQLyYbCNme1XNQm7xpjf1ljSgiaDZaGaIIwicJDNbCqXehibR7yAaqG79prChbdh5jcAkVZtuQnN5mpmlDzPj9icDA/640?wx_fmt=jpeg"
    ]

    con = account.format_content(arr)
    coverImage = r'https://mmbiz.qpic.cn/mmbiz_png/rrTMEWXicvaRhmRmmuuXaE1HQqYP89GvIc3dZ1iaA66A7axibYhoebYGe4icic8jUm3vB2xLKwyicX0aMVTKHicpIIrkw/640?wx_fmt=png'
    print(con)
    account.post_article(title='2019影视资源免费分享',
                         content=con,
                         run_ad=True,
                         cover_img=coverImage)


if __name__ == "__main__":
    print("run")

    bot = TTBot()
    account = bot.account
    print(account.name)
    print(account._account_info)
    print(account.media_info)

    publishArt(account)
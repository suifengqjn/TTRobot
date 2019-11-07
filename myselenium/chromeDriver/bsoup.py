# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from myselenium.chromeDriver import filter
import re
def ParseEle(html: str) ->(str, str):

    print("----", "parse")
    soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf8')
    p_set = soup.find_all("p")

    arr = []
    for p in p_set:
        txt = __trim(p.get_text())
        if len(txt) > 5:
            arr.append(txt)
        # print(txt)
        p_html = repr(p)
        if p_html.find("<img") > 0:
            temp_soup = BeautifulSoup(p_html, 'html.parser', from_encoding = 'utf8')
            img = temp_soup.find("img")
            if img.has_attr("data-src"):
                arr.append(img.get("data-src"))

    new_arr, cover_image = __filter(arr)
    res = __formatHtml(new_arr)
    return res, cover_image



    # t_list = soup.find_all(re.compile("(p|img)"))
    # for item in t_list:
    #     print(item.get_text())
    #     if item.has_attr("data-src"):
    #         print(item.get("data-src"))

def __filter(arr):

    firstImage = False
    new_arr = []
    stop = False
    coverImg  = None
    img_arr = []
    for index in range(len(arr)):

        if stop:
            break

        s = arr[index]
        if s.startswith("http"):
            if firstImage == True:
                new_arr.append(s)
                img_arr.append(s)
            firstImage = True
        else:
            if s not in filter.filter_words:
                new_arr.append(s)

            if index >= len(arr) * 9 / 10:
                if s in filter.filter_words:
                    stop = True

    img_count = len(img_arr)
    if img_count >= 2 :
        last_img = img_arr[img_count - 1]

        delIndex = 0
        for i in range(len(new_arr)):
            if last_img == new_arr[i]:
                delIndex = i
                break
        del new_arr[delIndex]


    coverImg = img_arr[int((len(img_arr) - 1)/2)]


    return (new_arr, coverImg)

def __formatHtml(arr) -> str:

    res = []
    for s in arr:
        if s.startswith("http"):
            res.append(__formatImg(s))
            # htmlStr += self.__formatImg(str)
        elif len(s)>1:
            res.append(__formatP(s))
            # htmlStr += self.__formatP(str)


    return "||".join(res)
    #return "<div>{}</div>".format(htmlStr)

def __formatP(s):
    return "pp--{}".format(s)
    #return "<p>{}</p>\n".format(str)
def __formatImg(s):
    return "im--{}".format(s)
def __trim(s):
    s = s.lstrip()
    s = s.rstrip()
    return s


if __name__ == "__main__":
    str = u"""
    <section data-mpa-powered-by="yiban.io">
    <section class="" data-support="96编辑器" data-style-id="22992">
        <section style="margin-top: 10px;margin-bottom: 10px;">
            <section style="width:80%;margin-left:auto;margin-right:auto;" data-width="80%"><img class=" __bg_gif" data-ratio="0.19611650485436893" data-src="https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgtMSXq3ZxQyDdcdvfOTYghZEeSR3zLZ9EZCGrZ2qNE7T04beY7jTWhBmRpwyxgVR5eia1CwOXG7mw/640?wx_fmt=gif" data-type="gif" data-w="515" data-width="100%" style="vertical-align: top; width: 100% !important; height: auto !important; visibility: visible !important;" _width="100%" src="https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgtMSXq3ZxQyDdcdvfOTYghZEeSR3zLZ9EZCGrZ2qNE7T04beY7jTWhBmRpwyxgVR5eia1CwOXG7mw/640?wx_fmt=gif&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1" data-order="0" data-fail="0"></section>
        </section>
    </section>
    <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<img class=" __bg_gif" data-ratio="0.029513888888888888" data-src="https://mmbiz.qpic.cn/mmbiz/yqVAqoZvDibHW4ynpBjRrolMxOZtKTiaYgGib3Z1r7qO6vXvLcXPmzYxbdQeJ8vcQcICOj6WbeuYRM3kdvBzehtkA/640?wx_fmt=gif" data-type="gif" data-w="1152" style="padding-top: 10px; padding-bottom: 10px; width: 677px !important; height: auto !important; visibility: visible !important;" _width="677px" src="https://mmbiz.qpic.cn/mmbiz/yqVAqoZvDibHW4ynpBjRrolMxOZtKTiaYgGib3Z1r7qO6vXvLcXPmzYxbdQeJ8vcQcICOj6WbeuYRM3kdvBzehtkA/640?wx_fmt=gif&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1" data-order="1" data-fail="0"><br></p>
    <p><br style="text-align: left;"></p>
</section>
<section>
    <section style="margin: 10px 20px;text-align: center;">
        <section style="margin-right: auto;margin-left: auto;width: 200px;height: 200px;border-style: solid;border-width: 1px;border-color: #b70b0a;padding: 3px;border-radius: 50%;box-sizing: border-box;">
            <section style="width: 200px;height: 200px;border-style: solid;border-width: 1px;border-color: #b70b0a;padding: 5px 3px;border-radius: 50%;box-sizing: border-box;">
                <p style="text-shadow: rgb(221, 205, 205) 3px 3px 1px;-webkit-text-stroke: 1px rgb(133, 133, 133);white-space: normal;box-sizing: border-box;text-align: left;"><strong><span style="letter-spacing:4px;font-size: 32px;color: #d92142;">&nbsp; &nbsp; 哪吒<br></span></strong></p>
                <section style="display: inline-block;margin-right: auto;margin-left: auto;width:1em;"><strong><img data-src="https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaKhMsMaVnDCANQowkLnx4SvTugIJpXo8rqsXDMvaj7Em080GhMD6kwA7ZKyluvoXbpZicQ0j7vhuw/640?wx_fmt=gif" data-type="gif" class=" __bg_gif" data-ratio="1.0307692307692307" data-w="130" _width="130px" src="https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaKhMsMaVnDCANQowkLnx4SvTugIJpXo8rqsXDMvaj7Em080GhMD6kwA7ZKyluvoXbpZicQ0j7vhuw/640?wx_fmt=gif&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1" style="width: 130px !important; height: auto !important; visibility: visible !important;" data-order="2" data-fail="0"></strong></section>
                <p><img class="img_loading" data-ratio="0.915" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mk4JAsbTX6eaH5vic8jCog6oBjg6L0BoPY3z6ibzuDfmfEFV3FpWuHeibbyjRGPwuia8g0mpeyKvflZw/640?wx_fmt=jpeg" data-type="jpeg" data-w="600" data-width="58%" style="width: 106.72px !important; height: 97.6488px !important; visibility: visible !important;" _width="58%" src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mk4JAsbTX6eaH5vic8jCog6oBjg6L0BoPY3z6ibzuDfmfEFV3FpWuHeibbyjRGPwuia8g0mpeyKvflZw/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1" crossorigin="anonymous"></p>
                <p><img data-src="https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgIVHtxUiaLia2BrtY0JdZrUtic14XuJABJtia5o7k5DCrvfic0GliaYZQl15Pfib0HHOz1Mia0ibQorpVQr3w/640?wx_fmt=gif" style="vertical-align: middle; box-sizing: border-box; width: 100% !important; height: auto !important; visibility: visible !important;" data-width="100%" data-type="gif" class=" __bg_gif" data-ratio="0.16666666666666666" data-w="480" _width="100%" src="https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgIVHtxUiaLia2BrtY0JdZrUtic14XuJABJtia5o7k5DCrvfic0GliaYZQl15Pfib0HHOz1Mia0ibQorpVQr3w/640?wx_fmt=gif&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1" data-order="3" data-fail="0"></p>
            </section>
        </section>
    </section>
</section>
<section style="margin:50px 10px;"></section>
<section style="margin:30px 10px;">
    <section style="margin-top: 10px;margin-bottom: 10px;">
        <section style="border-bottom: 2px dotted #d92142;border-left: 2px dotted #d92142;border-right: 2px dotted #d92142;border-top-width: 2px;border-top-color: #d92142;padding: 5px;box-sizing: border-box;">
            <section style="background-color: #ffeceb;padding: 15px;box-sizing: border-box;">
                <p style="letter-spacing: 2px;"><span style="font-size: 14px;color: #d92142;"></span></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">9月<span style="font-family: Calibri;">7</span>日晚<span style="font-family: Calibri;">9</span>点<span style="font-family: Calibri;">20</span>分，终于看了《哪吒之魔童降世》。此时，该片热映<span style="font-family: Calibri;">1</span>月有余。全国票房已达<span style="font-family: Calibri;">49</span>亿。</span></p>
                <p style="text-align: left;"><span style="font-size: 15px;"><span style="font-family: 宋体;">观后评分（5分制）：画面特效</span><span style="font-family: Calibri;">4</span><span style="font-family: 宋体;">分，剧情</span><span style="font-family: Calibri;">2</span><span style="font-family: 宋体;">分，创意</span><span style="font-family: Calibri;">4</span><span style="font-family: 宋体;">分。剧情不及格。综合</span><span style="font-family: Calibri;">3.3</span><span style="font-family: 宋体;">分。</span><br></span></p>
                <p><br></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">也就是说，饺子导演仍然脱离不了“讲不好一个故事”的中国影视的顽疾。</span></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">为什么讲不好一个故事，窃以为就是“前后逻辑不牢，整体剧情顾此失彼，不合常理不合人性，经不住推敲。”故事内核的薄弱，再好的特技，都只是绚丽的肥皂泡。用散文比较，就是堆砌再多的华丽辞藻，也掩盖不住作者的观念错乱。</span></p>
                <p><br></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">好吧，开始飙车。</span></p>
            </section>
        </section>
    </section>
</section>
<section style="margin: 30px 10px;">
    <section style="text-align: center;margin-top: 10px;margin-bottom: 10px;">
        <section style="display:inline-block;">
            <section style="margin-top: -2px;padding-top: 4px;padding-bottom: 4px;border-top: 1px solid #e8b3b0;color: #b50303;box-sizing: border-box;"><img class="img_loading" data-ratio="0.4185185185185185" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mk4JAsbTX6eaH5vic8jCog6d7XIPcSuBzcYibzXC0IiciaWuRtrZVBp6iaW8uOMDYhPvHQQTcSYrenvsg/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" _width="677px" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" style="width: 657px !important; height: 274.967px !important;" crossorigin="anonymous"></section>
            <section>
                <section style="text-align: center;margin-top: 10px;margin-bottom: 10px;margin-right:10px;">
                    <section style="display: inline-block;">
                        <section style="display:flex;z-index:99;">
                            <section style="width: 30px;height: 42px;font-size: 16px;display:inline-block;line-height:40px;color:#fdefd6;background:#d54d47;margin-bottom:-4.5px;">
                                <section style="width: 30px;height: 30px;font-size: 18px;display: inline-block;line-height: 30px;border-width: 1px;border-style: solid;border-color: #fdefd6;background-image: initial;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;box-sizing: border-box;">
                                    <p style="text-align: left;"><span style="font-size: 15px;"></span></p>
                                </section>
                            </section>
                        </section>
                        <section style="border-left: 1px solid #fdefd6;border-bottom: 1px solid #fdefd6;padding-left: 25px;margin-top: -20px;margin-left: 15px;box-sizing: border-box;">
                            <section sytle="color:#3f3f3f;font-size:16px;line-height:1.5em;">
                                <p style="text-align: left;margin-bottom: 10px;letter-spacing: 2px;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp;首先从踢毽子说起。</span></p>
                                <p style="text-align: left;margin-bottom: 10px;letter-spacing: 2px;"><span style="color:#fdefd6;"><span style="font-size: 14px;">&nbsp; &nbsp;</span></span><span style="font-family: 宋体;font-size: 15px;"> 哪吒踢毽子，为什么不能控制住“发射”力度：哪吒可以可以轻轻地在脚尖、头顶来颠鸡毛毽子，就说明他可以控制力度；然而，一旦“传球”，就连最亲爱的妈妈也不放过？编剧和导演你在搞笑吧？是的，导演在搞笑：把一个人一个大脚踢进墙内，是有点夸张和搞笑。如果老鼠把老猫一脚踢飞，我会微微一笑，周星驰一脚把足球踢到外太空我也能接受，可是，把最爱你的妈妈踢进高墙，我实在笑不出来。这一脚，踢中了我们中国人的核心价值观：对父母的孝。中华文化几千年，对父母的尊重，可以说是一个人从出生那天起就被熏陶，不容冒犯。</span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 饺子导演，一脚提出了两个问题：一是不符合他虚构的魔幻世界的运行逻辑，二是冒犯了现实世界的中国孝文化。<br></span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 踢毽子，是这部电影的一个非常关键的支撑元素和情节，几乎可以说踢毽子支撑了塑造哪吒世界观的半壁江山。我记得出现了四次。第一次是跟妈妈踢，第二次是跟邻居小孩踢，第三次是跟敖丙踢。第四次是哪吒说很遗憾没有踢他爸。<br></span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 仅此一条故事线，整部电影的逻辑基础和上层框架就摇晃起来，只差倒掉。这部电影的主题是关于偏见的。哪吒所受的偏见是什么？众人认为他是妖怪，是魔丸，是偏见吗？是吗？不算是。<br></span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 在众人认为他是妖怪之前，我们观众就知道他确实是有妖怪的基因，而且，在出生那天，陈塘关的乡亲们就眼见为实的看到哪吒是什么东西了。那么，无论从基因还是实证上，观众和电影世界里的人们，已经有证据证明他是有必要提防的异类。而他确实是异类，这算偏见吗？这不是偏见，是被事实所证实为真的情况：跟妈妈踢毽子，都可以差点踢死妈妈，如果踢那个小女孩，后果呢？<br></span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 如果哪吒出腿就可以要人命，那么所有陈塘关的柔弱人类，不回避他，正常吗？就算海里的妖怪夜叉，作恶也只是吃一只小动物，反倒显得像熊出没里的熊二一样可爱，而哪吒仅凭踢毽子的属性和技能，就是致命的，哪个更像妖怪？<br></span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 经以上分析，电影主题（偏见）的逻辑基础几乎就要塌方了。</span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 而为什么会这样呢？是人物塑造失败的结果。</span></p>
                                <p style="text-align: left;"><br></p>
                                <p style="text-align: left;margin-bottom: 10px;letter-spacing: 2px;"><span style="color: #fdefd6;font-size: 15px;"></span></p>
                                <p><img class="img_loading" data-ratio="0.4185185185185185" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mk4JAsbTX6eaH5vic8jCog6qibmzmATxgBmcnd6kcJbu4rMNq89uLxhMzBqyK16VKDnfzicNkbaYNuQ/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" _width="677px" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" style="width: 606px !important; height: 253.622px !important;" crossorigin="anonymous"></p>
                                <p><br></p>
                                <p><br></p>
                            </section>
                        </section>
                    </section>
                </section>
                <section style="margin-top:-30px;">
                    <section style="text-align: right;margin: 10px 5px;">
                        <section style="display: inline-block;text-align: center;">
                            <section style="width: 30px;height: 42px;font-size: 16px;display:inline-block;line-height:40px;color:#fdefd6;background:#d54d47;margin-bottom:-4.5px;">
                                <section style="width: 30px;height: 30px;font-size: 18px;display: inline-block;line-height: 30px;border-width: 1px;border-style: solid;border-color: #fdefd6;background-image: initial;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;box-sizing: border-box;">
                                    <p style="text-align: left;"><span style="font-size: 15px;">2</span></p>
                                </section>
                            </section>
                        </section>
                        <section style="border-right: 1px solid #fdefd6;border-bottom: 1px solid #fdefd6;padding-right: 25px;margin-top: -20px;margin-right: 15px;padding-top: 30px;padding-left: 10px;box-sizing: border-box;">
                            <section sytle="color:#3f3f3f;font-size:16px;line-height:1.5em;">
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 无论从写虚构作品的人物塑造，还是从社会心理学上看了解一个陌生人，基本思维主要都是这样：这个人外貌和谈吐是什么样子？他的脾气性格是什么样的？</span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 这两点，也就是外在和内在，基本可以粗浅概括一个人。社会心理学告诉我们，人们总在第一次相遇，就会根据他的衣着、举止、言谈，结合自己的阅历，去界定一个人，贴标签。而，所谓偏见，就是这个时候产生。通俗成功学老是教导大众要注意维护自己的“第一印象”，就是这个意思。</span></p>
                                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 然而，这部电影塑造的哪吒呢？我不想浪费时间说电影故事发生的原点的魔丸的来源是多么脆弱无趣，就说本剧最最最重要的人物的塑造是多么失败。</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;"><span style="font-family: 宋体;">虚构作品塑造主人公，看看《疯狂动物城》，就可以知道：小兔子要当警察维护正义的梦想，是怎么来的：被人欺负。《疯狂动物城》没有采用倒叙、闪回的手法（倒叙手法在中国影视剧中真是滥用错用，这个话题找时间再吐槽），而是扎扎实实地叙述，让我</span><span style="font-family: 宋体;">们知道小兔子的初心。而《哪吒之魔童降世》在塑造哪吒个性形成却用了闪回——用回忆的手法再现内心的信念和憋屈。我觉得这个闪回真的是很拙劣，败笔从此产生。为什么这么说？</span></span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">&nbsp; &nbsp; 在哪吒出生后，我们期待什么？我们想看这颗炸弹是怎么一步步融入这个人间社会的！这本该是全剧最精彩的基础部分，本该是哪吒信念形成的最重要时期，也是整部电影电影主题“偏见”构建的最重要的基础，但是，导演做了什么？带我们上天堂看风景！然后，天上一日地下一年，在缺失父爱的环境下，哪吒在人间“突然”变成了一个玩世不恭的问题少年！这里我已经没力气吐槽编剧对人间人类的生长逻辑规律的抛弃，也不想抱怨哪吒爸不陪儿子踢毽子对儿子成长陪伴的放弃，就说1岁的哪吒的心理：……我还真还看不出哪吒有什么具体信念。我看到导演呈现的是一个万念俱灰、玩世不恭而又寻求被关注的问题少年。唉，我们去天上看了一下下云景和孤门，导演你就给我们捏了个奇怪的哪吒出来。</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">&nbsp; &nbsp; 好吧，那我就忍了这个哪吒。因为我们可是随着猪骑士去了一两分钟天堂。但是，我很想知道：哪吒是经历了什么，让他成长为这个吊儿郎当的大神？难道魔丸就是这个尿性？魔性不是被压住了吗？不是算正常人了吗？</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">&nbsp; &nbsp; 导演暗示这个“问题哪吒”是人类偏见毁了他：陈塘关小孩子们认为他是妖怪，都不跟他玩，甚至用鸡蛋砸他、欺负他，然后，他就变坏了。是偏见造成了这个愤世嫉俗的问题哪吒。这是编剧兼导演的逻辑。很简单。因为偏见，所以愤世嫉俗。</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">&nbsp; &nbsp; 但是，在电影的魔幻世界里的人生观、价值观形成的1岁期间，我们可以知道哪吒缺失父亲的言传身教，但是还有母亲啊！母亲作为一个连性命都可以置之度外陪伴孩子的人，作为一个最了解天劫内幕的人，为什么还要灌输给哪吒是由于陈塘关的人们有偏见，才这样对他的？这不是给孩子一个错误的世界观吗？电影中对哪吒信念形成阶段的粗描淡写的不作为，导致了一场根基不稳的闹剧。</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">&nbsp; &nbsp; 郭德纲认为说相声一半是心理学，而电影呢？至少一半也是心理学。偏见，就是一个心理学范畴的概念。什么叫偏见？偏见是认知谬误，是人类大脑对事物的以偏概全的错误认知。电影里人们对哪吒的所谓偏见是什么？“你是妖怪，不跟你玩”。上文叙说了，哪吒是魔丸转世，确实是妖怪，这不算世俗偏见——而且陈塘关人民身处魔界，还时常被妖怪夜叉骚扰，对妖怪心存恐惧，闻之色变。你辩解说哪吒魔性已经被压制住，不算妖怪，是你们有偏见！可是，导演你让哪吒跟亲爱的妈妈踢毽子，就说明，哪吒魔性犹存，用敖丙的话说哪吒不是一般孩童，请勿靠近！你让陈塘关的老百姓、娘娘腔怎么承受得了那时速100码的毽子？</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">&nbsp; &nbsp; 所以，导演饺子，塑造哪吒的脾气性格宣告失败。哪吒的脾气性格，归咎不到世俗偏见。观众看不到有说服力的理由，基本就可以宣告作者塑造人物失败。</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">&nbsp; &nbsp; 主人公都塑造失败，其他人物，就不想说了。</span></p>
                                <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">人物塑造失败，最严重结果就是导致构建整部电影大厦的剧情结构的上梁不正下梁歪斜。为什么这么说？</span></p>
                                <p style="text-align: left;margin-bottom: 10px;letter-spacing: 2px;"><span style="font-size: 15px;font-family: 宋体;">一”假期。</span><br></p>
                                <p style="text-align: justify;margin-bottom: 10px;letter-spacing: 2px;"><span style="font-size: 15px;font-family: 宋体;"><img class="img_loading" data-cropselx1="0" data-cropselx2="493" data-cropsely1="0" data-cropsely2="206" data-ratio="0.5628517823639775" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mk4JAsbTX6eaH5vic8jCog6bHGyZ8z34y3rswoILlE16buibW2j9c0qH5iao5aOkiazpcFVibTyU0RhpQ/640?wx_fmt=jpeg" data-type="jpeg" data-w="533" style="width: 493px !important; height: 277.486px !important;" _width="493px" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" crossorigin="anonymous"></span></p>
                                <p style="text-align: justify;margin-bottom: 10px;letter-spacing: 2px;"><span style="font-size: 15px;font-family: 宋体;"><br></span></p>
                                <p style="text-align: left;margin-bottom: 10px;letter-spacing: 2px;"><br></p>
                            </section>
                        </section>
                    </section>
                </section>
                <section style="margin-top:-30px;">
                    <section style="text-align: center;margin-top: 10px;margin-bottom: 10px;margin-right:10px;">
                        <section style="display: inline-block;">
                            <section style="display:flex;z-index:99;">
                                <section style="width: 30px;height: 42px;font-size: 16px;display:inline-block;line-height:40px;color:#fdefd6;background:#d54d47;margin-bottom:-4.5px;">
                                    <section style="width: 30px;height: 30px;font-size: 18px;display: inline-block;line-height: 30px;border-width: 1px;border-style: solid;border-color: #fdefd6;background-image: initial;background-position: initial;background-size: initial;background-repeat: initial;background-attachment: initial;background-origin: initial;background-clip: initial;box-sizing: border-box;">
                                        <p style="text-align: left;"><span style="font-size: 15px;font-family: 宋体;">3</span></p>
                                    </section>
                                </section>
                            </section>
                            <section style="border-left: 1px solid #fdefd6;border-bottom: 1px solid #fdefd6;padding-left: 25px;margin-top: -20px;margin-left: 15px;padding-top: 30px;box-sizing: border-box;"></section>
                        </section>
                    </section>
                </section>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 人物性格生发于过往经历；而剧情，又生发于主人公的脾气性格。因为，主人公的脾气性格，无论好坏，决定他在未来剧情中会怎么应对各种外在挑战，如何展现人物弧光。如果主人公的脾气性格塑造不成功，那么后来的剧情构建，就是在跟随编剧的脾气性格和剧情需要，而不是剧中人的脾气性格，这就直接挑战了观众的生活常识和直觉。</span></p>
                <p style="text-align: left;"><span style="font-size: 15px;"><span style="font-family: 宋体;font-size: 20px;"><span style="font-size: 15px;">&nbsp; &nbsp; 对</span></span></span><span style="font-family: 宋体;font-size: 15px;">于哪吒的性格和信念的塑造，电影中交代得潦草和生硬，我忍了……好吧，那我就假设哪吒受到了不公正待遇，是世俗偏见冤枉他让他在人间受尽白眼，甚至怀疑人生。然后，哪吒为了证明自己是好人，是一心为老百姓创造价值的人，于是，在师父交给他更多技能后，就急切地去证明自己，想破除“偏见”。但是，因为编剧想要让偏见继续，就设计了哪吒的英勇行为反而被人们误会的桥段。先不说编剧这样继续塑造偏见的手法是否必要，其实这时剧情开始按编剧的需求转折：引出龙太子敖丙，引出幕后的另一股黑老大（除了魔丸这个魔咒之外的对抗势力）：龙王的阴谋。此时，剧情开始开挂，脱离一直叙述的主题：偏见。开始进入另一个主题：与另一个邪恶的抗争。这个才是哪吒的真正对手吗？而不是偏见？一直塑造的偏见之恶呢？</span></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 当编剧忘记了世俗的偏见后、龙王阴谋得以呈现，终于把剧情带入探讨“命运”主题模式。这有利于让哪吒喊出“我命由我不由天”。</span></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 在生日宴上，哪吒才得知自己的命是怎么回事。然后呢？他突然明白了什么？是父母的欺骗？还是世俗的偏见？哪吒这时应该突然明白了自己的命原来如此。然后，他应该明白人世间的真情，也明白了——他早该明白人们所谓偏见是合理的。自己的命，才是偏见之源。</span></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 后来，剧情处于失控状态。魔性控制了哪吒。那魔性为什么要杀害人类呢？没有理由。唯一的理由就是魔性很坏。</span></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">然后呢？哪吒莫名其妙地能够解锁那个控制魔性的项圈的性能，恢复人性而又可以压制魔性，——然后，突然可以有对抗龙族的力量，然后喊出我命由我不由天，然后有可以对抗天劫的力量……等一下，魔丸到底是什么？天劫到底要消灭魔丸还是哪吒肉体？魔丸开始不是被锁在莲花搭里？为什么上天使者猪骑士不在魔丸投胎转世这个时候就毁了魔丸，免得这一连串伤天害理的事故？！</span></p>
                <p style="text-align: left;"><span style="font-family: 宋体;font-size: 15px;">&nbsp; &nbsp; 这一波操作，十足的是根据编剧需要哪吒做什么哪吒就做什么，剧情需要什么技能就调取什么技能，而与先前塑造得很薄弱的人性偏见没有多大关系，与先前跟猪骑士练就的技能也没多大关系。</span></p>
                <p><span style="font-family: 宋体;font-size: 15px;"><br></span></p>
                <p><br></p>
                <p><img class="img_loading" data-ratio="0.562037037037037" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mk4JAsbTX6eaH5vic8jCog6Ig22lN61qyxr34YKY4ve2FMPWbSE78DbmfAMVMDNrvpRF6wxmVL3fA/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" _width="677px" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" style="width: 657px !important; height: 369.258px !important;" crossorigin="anonymous"></p>
            </section>
            <section class="">
                <p><br></p>
                <section style="display:flex;align-items:center;margin-right:-28px;width:28px;">
                    <section style="width:15px;height:1px;margin-right:-4px;color:#ffffff;background:#c7000b;"></section>
                    <section style="width: 10px;height: 10px;border-width: 1px;border-style: solid;border-color: #c7000b;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);-ms-transform: rotate(45deg);-o-transform: rotate(45deg);"></section>
                    <section style="width:7px;height:7px;color:#ffffff;background:#c7000b;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);-ms-transform: rotate(45deg);-o-transform: rotate(45deg);"></section>
                </section>
                <p><br></p>
                <section style="border-style: solid;border-width: 1px;border-color: rgb(199, 0, 11);padding: 15px;box-sizing: border-box;">
                    <p style="letter-spacing: 2px;"><span style="font-size: 14px;"></span></p>
                    <p style="text-align: center;"><span style="font-family: 宋体;font-size: 15px;background-color: #ffacaa;">那么，这是什么电影？哪吒在对抗什么？偏见？命运？青少年教育题材？主题到底是什么？</span></p>
                    <p style="text-align: center;"><span style="font-family: 宋体;font-size: 15px;background-color: #ffacaa;">没有一个好故事，再好的特效和画面，都不是一部及格的电影。</span></p>
                    <p style="text-align: center;"><span style="font-family: 宋体;font-size: 15px;background-color: #ffacaa;">所以，我对这部动漫的评价，是这样的：3.3分。</span></p>
                    <p style="text-align: center;"><br></p>
                    <p style="text-align: center;"><span style="font-family: 宋体;font-size: 15px;background-color: #ffacaa;">好吧，说优点</span></p>
                    <p style="text-align: center;"><span style="font-family: 宋体;font-size: 15px;background-color: #ffacaa;">中国动漫的画面和特技，已经跻身世界了。</span></p>
                    <p style="text-align: center;"><span style="font-family: 宋体;font-size: 15px;background-color: #ffacaa;">可打4.0分（5分制）</span></p>
                    <p style="text-align: center;"><span style="font-family: 宋体;font-size: 15px;background-color: #ffacaa;">此外，那个彪形大汉的女性动作和声音，雷到我的笑点了。</span></p>
                    <p style="letter-spacing: 2px;"><span style="font-size: 14px;background-color: #ffacaa;"></span></p>
                    <p style="letter-spacing: 2px;"><br></p>
                </section>
                <section style="margin-top:-10px;">
                    <section style="display:inline-block;">
                        <section style="display:flex;align-items:center;width:28px;">
                            <section style="width:7px;height:7px;color:#ffffff;background:#c7000b;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);-ms-transform: rotate(45deg);-o-transform: rotate(45deg);"></section>
                        </section>
                    </section>
                </section>
                <p><br></p>
            </section>
            <section class="">
                <p style="text-align: center;"><img class="rich_pages img_loading" data-ratio="0.4185185185185185" data-s="300,640" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mk4JAsbTX6eaH5vic8jCog6uQJs3MiaG7kRiaxKCyiaicBtzYrnQC4ZibSNoibKTibT5PGEzdzTGLgJJkibpw/640?wx_fmt=jpeg" data-type="jpeg" data-w="1080" style="width: 657px !important; height: 274.967px !important;" _width="677px" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" crossorigin="anonymous"></p>
                <p><br></p>
                <p style="white-space: normal;font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);"><span style="font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif;letter-spacing: 0.544px;font-size: 14px;">&nbsp; 作者：<span style="letter-spacing: 0.544px;">睂景&nbsp;&nbsp;</span></span></p>
                <p style="white-space: normal;font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);"><span style="font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif;letter-spacing: 0.544px;font-size: 14px;">编辑：静物情绪</span></p>
                <p style="white-space: normal;font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);"><br></p>
                <p style="white-space: normal;"><span style="color: rgb(0, 82, 255);font-size: 14px;">往期精选：</span></p>
                <p style="white-space: normal;"><br></p>
                <p style="white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzU2NjQ4MTI0MQ==&amp;mid=2247485320&amp;idx=1&amp;sn=1d42ba2d093f078ba150b70a23afd179&amp;chksm=fcaa9fbecbdd16a853f0a12faabec8d180ba5926791355563571ccf704de575cfd9f7d3fe2b5&amp;scene=21#wechat_redirect" target="_blank" data-itemshowtype="0" data-linktype="2"><span style="font-size: 14px;">【摄影】我遇到的一位小女孩</span></a><br></p>
                <p style="white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzU2NjQ4MTI0MQ==&amp;mid=2247485293&amp;idx=1&amp;sn=c6cf4b83f00cb0ef33bb277020aeb833&amp;chksm=fcaa9f5bcbdd164de30ddbbcbd3efb5146f20c3fd8c8d94bdef719d97df32b677892e7d67876&amp;scene=21#wechat_redirect" target="_blank" data-itemshowtype="0" data-linktype="2"><span style="font-size: 14px;">【中秋特稿】在果敢过团圆节</span></a><br></p>
                <p style="white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzU2NjQ4MTI0MQ==&amp;mid=2247485293&amp;idx=2&amp;sn=d8b86076bf89c949122b7c7a93223a33&amp;chksm=fcaa9f5bcbdd164d7b8cfdc2575c1ded450d3d7e24e3624912f80a715604b2b40d99d7f2987d&amp;scene=21#wechat_redirect" target="_blank" data-itemshowtype="0" data-linktype="2"><span style="font-size: 14px;">【摄影】收获古镇里的秋</span></a><br></p>
                <p style="white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzU2NjQ4MTI0MQ==&amp;mid=2247485320&amp;idx=2&amp;sn=955e50e06ddb5537c7da451d1af56eda&amp;chksm=fcaa9fbecbdd16a8ab2dc6a9b9e4a6f4631f6684f69d49e0e8ecad49e0fcf65db0c5b0179a0d&amp;scene=21#wechat_redirect" target="_blank" data-itemshowtype="0" data-linktype="2"><span style="font-size: 14px;">【诗歌】终有一天</span></a><br></p>
                <p style="white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzU2NjQ4MTI0MQ==&amp;mid=2247485261&amp;idx=1&amp;sn=853f7862a58700051e27b3b6955c3361&amp;chksm=fcaa9f7bcbdd166d7f9d3c81453091c23b81d73676aee4c1d330365efdd8f6140f0537905b67&amp;scene=21#wechat_redirect" target="_blank" data-itemshowtype="0" data-linktype="2"><span style="font-size: 14px;">【火狐狸的音乐杂志】这佛塔，已披上时间的斑驳……</span></a><br></p>
                <p style="white-space: normal;"><a href="http://mp.weixin.qq.com/s?__biz=MzU2NjQ4MTI0MQ==&amp;mid=2247485247&amp;idx=1&amp;sn=cd8c6c9518bebe470567c45f651c0a29&amp;chksm=fcaa9f09cbdd161f14d0075389d3d1b51275697b4dc0ed7241b21e9dc2b94830f2b3277ec19b&amp;scene=21#wechat_redirect" target="_blank" data-itemshowtype="0" data-linktype="2"><span style="font-size: 14px;">【特稿】碎梦——我在泰国当老师的那些日子</span></a></p>
                <p style="white-space: normal;font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);"><br></p>
                <section class="" style="white-space: normal;">
                    <section style="margin-top: 30px;margin-bottom: 10px;text-align: center;">
                        <section data-width="95%" style="padding: 5px;display: inline-block;width: 528.188px;vertical-align: top;box-shadow: rgb(185, 185, 185) 1.41421px 1.41421px 6px;">
                            <section>
                                <section style="margin-top: -20px;margin-bottom: 5px;">
                                    <section style="vertical-align: middle;display: inline-block;box-shadow: rgb(0, 0, 0) 0px 0px 0px;overflow: hidden !important;"><img data-src="https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjvXFPQy1nYURBPwtRIhAWf6KrPsxdqoIx6ufwHic7icMaspxWoeMOFicT0l7FrTdt8olehy6WDS7PDg/640?wx_fmt=png" data-type="png" class="" data-ratio="0.06041666666666667" data-w="480" style="vertical-align: middle; width: 480px !important; height: 29px !important;" _width="auto" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" crossorigin="anonymous"></section>
                                </section>
                            </section>
                            <section>
                                <section style="margin-top: 10px;margin-bottom: 10px;">
                                    <section data-width="38%" style="padding-left: 10px;display: inline-block;vertical-align: middle;width: 196.906px;box-shadow: rgb(0, 0, 0) 0px 0px 0px;">
                                        <section>
                                            <section>
                                                <section style="vertical-align: middle;display: inline-block;box-shadow: rgb(0, 0, 0) 0px 0px 0px;border-style: solid;border-width: 2px;border-radius: 0px;border-color: rgb(62, 62, 62);overflow: hidden !important;"><img class="img_loading" data-copyright="0" data-cropselx1="0" data-cropselx2="183" data-cropsely1="0" data-cropsely2="183" data-ratio="1" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/TCTnPIicD52mRkdvgV9e5XKV87FbJyeB8T1TlIUtKjV5ewmFjLJBacuicADG24bN43X6RkK7qBqNthpUD8jibb8Mg/640?wx_fmt=jpeg" data-type="jpeg" data-w="1280" style="vertical-align: middle; width: 183px !important; height: 183px !important;" _width="183px" src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==" crossorigin="anonymous"></section>
                                            </section>
                                        </section>
                                    </section>
                                    <section data-width="61.8%" style="display: inline-block;vertical-align: middle;width: 320.234px;border-style: groove;border-width: 0px;border-radius: 0px;border-color: rgb(62, 62, 62);">
                                        <section>
                                            <section>
                                                <section style="font-size: 12px;">
                                                    <p><span style="font-size: 15px;"><strong>扫码关注 文艺大锅菜</strong></span><br></p>
                                                    <p><span style="font-size: 15px;"><strong><span style="font-family: Optima-Regular, PingFangTC-light;">推介文艺人事 品味世间百态</span></strong></span></p>
                                                </section>
                                            </section>
                                        </section>
                                        <section>
                                            <section style="margin-top: 10px;margin-bottom: 10px;font-size: 10px;">
                                                <section style="padding: 5px;display: inline-block;box-shadow: rgb(13, 0, 21) 0px 0px 0px inset;border-style: solid;border-width: 1px;border-radius: 10%;border-color: rgb(66, 66, 66);background-color: rgb(240, 235, 69);">
                                                    <section>
                                                        <section>
                                                            <section style="padding-right: 8px;padding-left: 8px;text-align: left;color: rgb(13, 0, 21);">
                                                                <p><span style="font-size: 16px;"><strong><span style="font-family: Optima-Regular, PingFangTC-light;">投稿邮箱 wydgcwy@163.com</span></strong></span></p>
                                                            </section>
                                                        </section>
                                                    </section>
                                                </section>
                                            </section>
                                        </section>
                                    </section>
                                </section>
                            </section>
                        </section>
                    </section>
                </section>
                <p><br></p>
            </section>
        </section>
    </section>
</section>
    """
    ParseEle(str)
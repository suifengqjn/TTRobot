import threading
import time
from util import util
from myselenium import baisi
import random
# 微头条
class Wtt(threading.Thread):
    def __init__(self, name, account):
        super().__init__(name=name)
        self.account = account

    def run(self):

        while True:
            if util.isNight():
                continue

            param = baisi.get_duanzi()

            image_path = '/Users/qianjianeng/Desktop/123.gif'
            # image_list = [r'C://pictures/test01.jpg', r'C://pictures/test02.jpg']
            weitt_content = param["mark"]
            # # 发布内容中只有一张图片
            self.account.post_weitt(weitt_content, image=None)
            # 发布内容中包含有两种或以上的图片
            #self.account.post_weitt(weitt_content, image=image_list)

            print("pub wtt", param)

            time.sleep(60 * random.randint(50, 90))

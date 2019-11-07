import threading
import time
from util import util
# 微头条
class Wtt(threading.Thread):
    def __init__(self, name, account):
        super().__init__(name=name)
        self.account = account

    def run(self):

        while True:
            if util.isNight():
                continue

            # image_path = r'C://pictures/test.jpg'
            # image_list = [r'C://pictures/test01.jpg', r'C://pictures/test02.jpg']
            # weitt_content = '这是一个测试用微头条.[posted by TTBot]'
            # # 发布内容中只有一张图片
            # self.account.post_weitt(weitt_content, image=image_path)
            # 发布内容中包含有两种或以上的图片
            #self.account.post_weitt(weitt_content, image=image_list)

            print("pub wtt")

            time.sleep(30)

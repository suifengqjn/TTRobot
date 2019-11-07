
from task import wtt
class BgTask():

    def __init__(self, account):
        self.account = account
    def run(self):

        wt = wtt.Wtt("wtt", self.account)
        wt.start()

        print("run")
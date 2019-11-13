from myselenium.database import mySqlTool
import time

def ptint():
    print(time.time())

if __name__ == "__main__":



    sql = mySqlTool.MySqlTool(host="106.12.220.252",user="qjn",password="BAIDUYUNqjn19920314*!", database="wechat_api")


    sql.turncate()
    # return
    # title = "中国"
    # content = "bbb"
    # md5 = "1234"
    # sql_str = 'insert ignore into wx_article (url,title,content,md5) values("%s","%s","%s","%s")' % ("",title, content, md5)
    #
    #
    # print(sql_str)
    # sql.exec(sql_str)

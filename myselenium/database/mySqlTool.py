
import pymysql
from myselenium.chromeDriver import model
import json
class MySqlTool():

    def __init__(self, host,user,password,database, charset="utf8mb4", port=3306):
        self.host= host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

        self.ping()
        self.close()

    def __connect(self):
        return pymysql.connect(host=self.host,
                        port=self.port,
                        user=self.user,
                        password=self.password,
                        database=self.database,
                        charset=self.charset)

    def ping(self):
        try:
            self.conn = self.__connect()
        except pymysql.Error as e:
            print('连接数据库失败',e)

    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print(e)

    def exec(self, sql_str):

        con = self.__connect()
        cur = con.cursor()
        try:
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
            raise
        finally:
            cur.close()
            con.close()

    def execMany(self, sql):
        self.conn = self.__connect()
        return self.conn.cursor().executemany(sql)

    def turncate(self):
        return self.exec("turncate wx_article")

    def query(self, sql_str):
        con = self.__connect()
        cur = con.cursor()
        cur.execute(sql_str)
        rows = cur.fetchall()
        cur.close()
        con.close()
        print(rows)
        return rows[0][0]
    def insert_articles(self,articles):
        for ar in articles:
            dict = ar.__dict__
            # artiJson = json.dumps(dict)
            title = dict["title"]
            content = dict["content"]
            cover_image = dict["cover_image"]
            md5 = dict["md5"]
            self.insert_article(title, title, content, cover_image, md5)

    def insert_article(self,key_word, title, content,cover_img,md5):
        sql_str = 'insert ignore into wx_article (key_word,title,content,cover_img,md5) values("%s","%s","%s","%s","%s")' % (key_word, title, content, cover_img,md5)
        self.exec(sql_str)
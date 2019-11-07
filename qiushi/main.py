from qiushi import qiushibaike

if __name__ == "__main__":
    sp = qiushibaike.QiushiSpider()
    print(sp)
    print(sp.__dict__)
    print(sp.topic_list)

    iter = sp.start_requests()
    for i in iter:
        print(i.callback)

        print(type(i))


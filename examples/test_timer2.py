import threading
import time
import tushare as ts


class Test(threading.Thread):
    def __init__(self):
        pass

    def test(self):
        df = ts.get_realtime_quotes(['600015', '601988', '601318','600029'])
        print(df[['code','name','price','bid','ask','volume','amount','time']])

    def run(self):
        while True:
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            self.test()
            time.sleep(5)


a = Test()
a.run()

import threading
import time


class Test(threading.Thread):
    def __init__(self):
        pass

    def test(self):
        print('run test')

    def run(self):
        while True:
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            self.test()
            time.sleep(5)


a = Test()
a.run()

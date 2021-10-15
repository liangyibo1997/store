'''
生产者消费者模型
需求:
厨师(生成者)：3个厨师造汉堡,每造一个向篮子扔一个,当篮子已经满了时候，停个3秒,判断是否已满,没满，继续进行。汉堡篮子:最多只能放20个。
消费者：6个消费者，一共有600元,每个汉堡5元。6个人同时抢，当篮子汉堡不够,稍等3秒,然后继续判断是否还有。到前花完为止。
'''

from threading import Thread
import time

basket = 0
money = 600


class Producer(Thread):
    cook_name = ""

    def run(self) -> None:
        global basket, money
        while True:
            if money > 0:
                if basket < 20:
                    basket = basket + 1
                    print("%s又做了1个汉堡，并扔进篮子里。" % self.cook_name)
                else:
                    print("已经做了20个汉堡，篮子已经满了！")
                    time.sleep(3)
            else:
                break


class Consumer(Thread):
    name = ""
    count = 0

    def run(self) -> None:
        global basket, money
        while True:
            if money > 0:
                if basket > 0:
                    self.count = self.count + 1
                    basket = basket - 1
                    money = money - 5
                    print("%s，我抢到了1个汉堡，还剩下%d元钱！" % (self.name, money))
                    time.sleep(0.1)
                else:
                    print("篮子里汉堡不够，请等待3秒！")
                    time.sleep(3)
            else:
                print("钱已花完，%s总共抢了%d个汉堡！" % (self.name, self.count))
                break


p1 = Producer()
p1.cook_name = "厨一"
p2 = Producer()
p2.cook_name = "厨二"
p3 = Producer()
p3.cook_name = "厨三"

c1 = Consumer()
c1.name = "秦一"
c2 = Consumer()
c2.name = "徐二"
c3 = Consumer()
c3.name = "张三"
c4 = Consumer()
c4.name = "李四"
c5 = Consumer()
c5.name = "王五"
c6 = Consumer()
c6.name = "吴六"

p1.start()
p2.start()
p3.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()

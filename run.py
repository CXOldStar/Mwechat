# _*_ coding:utf-8 _*_
import gevent
from gevent import monkey
monkey.patch_socket()
from tigger.auto import sched_gevent
from wechat.base_operation import Operation
from wechat import itchat


def run_tigger():
    g = sched_gevent.start()
    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        pass


def run_wechat():
    Operation.login()
    rooms = Operation.search_rooms()
    itchat.run()


if __name__ == '__main__':
    run_tigger()
    run_wechat()


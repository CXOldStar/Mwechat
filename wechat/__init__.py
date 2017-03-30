import itchat
from itchat.content import *
from .base_operation import Operation


@itchat.msg_register(TEXT)
def roommsg(msg):
    print('recv:', msg)


if __name__ == '__main__':
    Operation.login()
    rooms = Operation.search_rooms()
    itchat.run()


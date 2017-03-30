import itchat
from itchat.content import *

MAP_PARTTERN = 'IRobot'


def login():
    itchat.auto_login(enableCmdQR=2)


def search_rooms(room_name):
    rooms = itchat.search_chatrooms(name=room_name)
    return rooms


def send2room(msg, rooms):
    for i_room in rooms:
        room_username = i_room['UserName']
        itchat.send(msg, room_username)


@itchat.msg_register(TEXT)
def roommsg(msg):
    print('recv:', msg)


if __name__ == '__main__':
    login()
    rooms = search_rooms(MAP_PARTTERN)
    itchat.run()


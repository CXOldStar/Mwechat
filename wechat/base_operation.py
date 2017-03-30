from wechat import itchat


MAP_PARTTERN = 'IRobot'


class Operation:
    @staticmethod
    def login():
        itchat.auto_login(enableCmdQR=2)

    @staticmethod
    def search_rooms(room_name=MAP_PARTTERN):
        rooms = itchat.search_chatrooms(name=room_name)
        return rooms

    @staticmethod
    def send2room(msg, rooms):
        for i_room in rooms:
            room_username = i_room['UserName']
            itchat.send(msg, room_username)
# coding: utf-8
# 2018.08.22

import requests
import uuid
import getBoccoMessage as getMsg
import getUserInformation as getUserInfo

def sendBoccoMessage(msg):
    userInfo = getUserInfo.getUserInformation() # access_token, room_uuidが帰ってくる
    
    if msg is None:
        msg = getMsg.getBoccoMessage(2)

    # curlのオプションで指定している情報
    headers = {
        'Accept-Language': 'ja',
    }

    # curlのオプションで指定している情報
    data = [
      ('access_token', userInfo[0]),
      ('unique_id', uuid.uuid4()), #コマンドラインだと`uuidgen`があるけどPyhton内ではないので
      ('media', 'text'),
      ('text', msg),
    ]

    # post
    response = requests.post('https://api.bocco.me/alpha/rooms/09540d0d-ee72-455c-a248-accbe77ccac6/messages', headers=headers, data=data)

    print('> Send {' + msg + '} to bocco.')
    
if __name__ == "__main__":
    sendBoccoMessage()
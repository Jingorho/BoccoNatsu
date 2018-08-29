# coding: utf-8
# 2018.08.23

import requests
import uuid
import bocco

######
# 自作のBoccoAPIをインストールする方法
######
# APIのディレクトリに移動
# $ cd /Users/yukako/WorkSpace/Bocco/bocco-api-python/
# $ python setup.py install   #setup.pyをインストールコマンドで実行
# $ sudo python setup.py install 
#
# スクリプト内では
# api = bocco.api.Client('アクセストークン') #apiのインスタンスを作る
# どんな場所からでも'import bocco'で利用できる

api = bocco.api.Client('535f77f09d7f6da5da9ab11885302d7885720d7b437efe06cf3f4b096406df45')
room_uuid = uuid.UUID('09540d0d-ee72-455c-a248-accbe77ccac6')

def sendBoccoPicturebook():

  api.post_image_message( 
    room_uuid, '/root/Picturebook/picturebook.png')
  print('> Send picturebook to chatroom.')


if __name__ == "__main__":
  sendBoccoPicturebook()

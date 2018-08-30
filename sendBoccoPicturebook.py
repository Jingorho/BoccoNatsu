# coding: utf-8
# 2018.08.23

import requests
import uuid
import os
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

  # 送信
  api.post_image_message(room_uuid, '/root/Picturebook/picturebook.png')


  # n枚目もあったら送信
  # if len(os.listdir('/root/Picturebook/')) > 2:
  #   for i in len(os.listdir('/root/Picturebook/')): # ファイルのリストを取得
  #     if os.path.exists('/root/Picturebook/picturebook' + str(i) + '.png'):
  #       api.post_image_message(room_uuid, '/root/Picturebook/picturebook' + str(i) + '.png')
  #       os.remove('/root/Picturebook/picturebook' + str(i) + '.png')
  #       print("picturebook" + str(i) + ".png is uploaded")

  #     else:
  #       print("picturebook_n.png is not found")


  print('> Send picturebook to chatroom.')


if __name__ == "__main__":
  sendBoccoPicturebook()

# coding: utf-8
# 2018.08.24

import os
import glob
import datetime
import shutil

import socket
# from datetime import datetime
from time import sleep


def detectUploadPictures():

  dateDirPath = 'pictures/' + datetime.datetime.today().strftime("%y%m%d")

  isPicturesUploaded = False
  pictures = glob.glob('pictures/*.png')
  
  

  s = socket.socket()
  port = 25565 #固有の番号をテキトーに指定
  s.bind(('', port))

  while True:
      print('listening')
      s.listen(5)

      c, addr = s.accept()
      dataFromClient = c.recv(4096).decode()
      print('receiving')
      print('> Received ' + dataFromClient + 'from Camera.')
      
      # ファイル受信通知を受け取ったら
      if c is not None:
        isPicturesUploaded = True
        print('#')
        print('> Detected uploaded pictures.')

        # 受信通知と受信内容を引き渡す
        return isPicturesUploaded, dataFromClient
      
      # else:
      #   print('Received data is null')
      #   return


      # ファイル受信後の処理. 不必要
      # while True:
      #     # print('sending')
      #     # now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      #     # try:
      #     #     c.send(now)
      #     # except:
      #     #     break
      #     sleep(1)

      # c.close()
      # while True

  s.close()
  # while True



  # ###############################
  # # ファイルが存在していたら
  # if len(pictures) != 0:
  #   isPicturesUploaded = True

  #   # 日付のディレクトリがない時のみ新規作成
  #   if os.path.exists(dateDirPath):
  #     print('>' + str(dateDirPath) + 'directory already exist.')
  #   else:
  #     os.mkdir(dateDirPath)

  #   # 新規作成したディレクトリに写真ファイル移動
  #   for i in range(len(pictures)):
  #     shutil.move(pictures[i], dateDirPath+'/'+pictures[i][9:])


  #   print('#')
  #   print('> Detected uploaded pictures.')

  # return isPicturesUploaded
  


if __name__ == "__main__":
    detectUploadPictures()

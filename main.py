# coding: utf-8
# 2018.08.24

# ps -fA | grep python
# kill 14047

import socket
import time
from time import sleep

# import detectUploadPictures as detectUpPict
import sendBoccoMessage as sendBoccoMsg
import getBoccoMessage as getBoccoMsg

import detectUserMessage as detectUsrMsg
import generatePicturebook as generatePb
import sendGoogleDrive as sendGD
import sendBoccoPicturebook as sendBoccoPb


class Main:

  
  
  def main():
    s = socket.socket()
    port = 25565 #固有の番号をテキトーに指定
    s.bind(('', port))
    dataFromClient = ""

    WaitingUserMessage = False



    while True:

      ##############################################################
      #
      # ユーザのメッセージを検知してアルバム生成してGoogleDriveにup
      #
      ##############################################################
      if WaitingUserMessage is True:
        print("> Waiting user message ...")
        if (detectUsrMsg.detectUserMessage()):
          
          generatePb.generatePicturebook(dataFromClient)
          sendGD.sendGoogleDrive(dataFromClient)
          sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(2) )
          # sendBoccoMsg.sendBoccoMessage('GoogleDriveにアップロードしたよ')
          sleep(3)
          sendBoccoPb.sendBoccoPicturebook()
          WaitingUserMessage = False

        else:
          print('> User message does not found (or Bocco spoke).')



      ##############################################################
      #
      # Socket通信で写真up通知を受け取ってBoccoにメッセージ送信
      #
      ##############################################################
      else:

        print('> Listening the notification of uploading pictures ...')
        s.listen(5)

        c, addr = s.accept()
        dataFromClient = c.recv(4096).decode()

        print('> Received ' + dataFromClient + ' from Camera.')
        print('> Detected pictures uploaded.')

        # ファイル受信通知を受け取ったら
        # 「今日は何があったの？」
        sendBoccoMsg.sendBoccoMessage( getBoccoMsg.getBoccoMessage(1) )
        WaitingUserMessage = True


      sleep(10)

    s.close()




  if __name__ == "__main__":
    main()


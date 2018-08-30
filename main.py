# coding: utf-8
# 2018.08.24

# ps -fA | grep python
# kill 14047

import socket
import time
from time import sleep

import sendBoccoMessage as sendBoccoMsg
import trySendBoccoPicture as trySendBoccoPict

import getBoccoMessage as getBoccoMsg

import detectUserMessage as detectUsrMsg
import generatePicturebook as generatePb
import sendGoogleDrive as sendGD
import sendBoccoPicturebook as sendBoccoPb

import getTheme as getTm


class Main:

  
  
  def main():
    s = socket.socket()
    port = 25565 #固有の番号をテキトーに指定
    s.bind(('', port))
    dataFromClient = ""

    WaitingUserMessage = False
    manageScene = 0

    theme = ""


    while True:

      ##############################################################
      #
      # (2) アルバム生成と終了
      # ユーザのメッセージを検知してアルバム生成してGoogleDriveにup
      #
      ##############################################################
      if manageScene  is 2:
      
        print("> Waiting user message ...")

        # メッセージが無かったら
        if detectUsrMsg.detectUserMessage() is 0:
          print("###")

        # # スタートトリガーワードを含むメッセージがあったら
        # elif detectUsrMsg.detectUserMessage() is 1:
        #   sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(0pytho) )

        # それ以外のメッセージがあったら
        elif detectUsrMsg.detectUserMessage() is 2:
          generatePb.generatePicturebook(dataFromClient)
          sendGD.sendGoogleDrive(dataFromClient)
          sendBoccoMsg.sendBoccoMessage( getBoccoMsg.getBoccoMessage(2) )
          
          # sendBoccoPicture()でToo Many Requestが頻発するので、
          # Try-exceptで、Upするまで待つ処理.
          trySendBoccoPict.trySendBoccoPicture()
          

          # WaitingUserMessage = False
          manageScene = 0

        else:
          print('> User message does not found (or Bocco spoke).')



      ##############################################################
      #
      # (1) 写真アップロード
      # Socket通信で写真up通知を受け取ってBoccoにメッセージ送信
      #
      ##############################################################
      elif manageScene is 1:
      
        print('> Listening the notification of uploading pictures ...')
        s.listen(5)

        c, addr = s.accept()
        dataFromClient = c.recv(4096).decode()

        print('> Received ' + dataFromClient + ' from Camera.')
        print('> Detected pictures uploaded.')

        # ファイル受信通知を受け取ったら
        # 「今日は何があったの？」
        sendBoccoMsg.sendBoccoMessage( getBoccoMsg.getBoccoMessage(1) )
        # WaitingUserMessage = True
        manageScene = 2



      ##############################################################
      #
      # (0) セッション開始
      # TRIGGERを含むユーザのメッセージ（開始トリガー）を検知してセッションを開始
      #
      ##############################################################
      elif manageScene is 0:
        print('> Waiting user TRIGGER massage ...')
        # メッセージが無かったら
        if detectUsrMsg.detectUserMessage() is 0:
          print("###")

        # スタートトリガーワードを含むメッセージがあったら
        elif detectUsrMsg.detectUserMessage() is 1:
          sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(0) )
          
        # # それ以外のメッセージがあったら
        # elif detectUsrMsg.detectUserMessage() is 2:
        #   generatePb.generatePicturebook(dataFromClient)
        #   sendGD.sendGoogleDrive(dataFromClient)
        #   sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(2) )
        #   # sendBoccoMsg.sendBoccoMessage('GoogleDriveにアップロードしたよ')
        #   sleep(3)
        #   sendBoccoPb.sendBoccoPicturebook()
        #   WaitingUserMessage = False
          manageScene = 1

        else:
          print('> User message does not found (or Bocco spoke).')



      # whileループ自体を10秒ごとに実行
      sleep(10)

    s.close()




  if __name__ == "__main__":
    main()


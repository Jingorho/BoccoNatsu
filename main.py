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
import getUserMessage as getUserMsg

import detectUserMessage as detectUsrMsg
import generatePicturebook as generatePb
import sendGoogleDrive as sendGD
import sendBoccoPicturebook as sendBoccoPb

import setTheme as setTm

# import getTheme as getTm


class Main:

  
  
  def main():
    # s = socket.socket()
    # port = 25565 #固有の番号をテキトーに指定
    # s.bind(('', port))
    dataFromClient = ""

    WaitingUserMessage = False
    manageScene = 0

    isSetTheme = False

    theme = ""


    while True:

      ##############################################################
      #
      # (2) アルバム生成と終了
      # ユーザのメッセージを検知してアルバム生成してGoogleDriveにup
      #
      ##############################################################
      if manageScene  is 2:
      
        print("> Waiting user report message ...")


        # トリガーを含まないメッセージがあったら
        if detectUsrMsg.detectUserMessage() is 1:
          generatePb.generatePicturebook(dataFromClient)
          sendGD.sendGoogleDrive(dataFromClient)
          # へーそうなんだ
          sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(1) )

          # sendBoccoPicture()でToo Many Requestが頻発するので、
          # Try-exceptで、Upするまで待つ処理.
          trySendBoccoPict.trySendBoccoPicture()
          

          # WaitingUserMessage = False
          # 最初に戻る
          isSetTheme = False
          manageScene = 0

        else:
          print('> User message does not be found (or Bocco spoke).')



      ##############################################################
      #
      # (1) 写真アップロード
      # Socket通信で写真up通知を受け取ってBoccoにメッセージ送信
      #
      ##############################################################
      elif manageScene is 1:
      
        print('> Listening the notification of uploading pictures ...')
        s = socket.socket()
        port = 25565 #固有の番号をテキトーに指定
        s.bind(('', port))
        s.listen(5)

        c, addr = s.accept()
        dataFromClient = c.recv(4096).decode()

        print('> Received ' + dataFromClient + ' from Camera.')
        print('> Detected pictures uploaded.')

        # if c is not None:
        # ファイル受信通知を受け取ったら
        # 今日は何をとったの？
        # sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(0))
        sendBoccoMsg.sendBoccoMessage( getBoccoMsg.getBoccoMessage(0) )
        # WaitingUserMessage = True
        manageScene = 2

        s.close() # ?
        print("> CLOSED! [c is not None] so closed [s] successfully.")
        s = None
        c = None
        addr = None


      ##############################################################
      #
      # (0) セッション開始
      # TRIGGERを含むユーザのメッセージ（開始トリガー）を検知してセッションを開始
      #
      ##############################################################
      elif manageScene is 0:
        print('> Waiting user TRIGGER massage ...')
        # 該当のメッセージが無かったら (0はメッセージ自体なし、1はトリガーを含むメッセージなし)
        if detectUsrMsg.detectUserMessage() < 2:
          print("###")


        ###############################
        # テーマの設定トリガーワードを含むメッセージがあったら
        ###############################
        elif (detectUsrMsg.detectUserMessage() is 2) and (isSetTheme is False):
          tempResult = getUserMsg.getUserMessage(2) #テーマ設定トリガーワードを含むメッセージでの引数は2としてる
          print("tempResult: " + str(tempResult))
          setTm.setTheme(tempResult[0]) #getUserMessage()ではメッセージ本体と天気が返ってくるので第一返り値で
          # 今日のテーマをthemeに設定したよ！
          print(":::" + getBoccoMsg.getBoccoMessage(2))
          sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(2) )
          isSetTheme = True



        ###############################
        # 開始トリガーワードを含むメッセージがあったら
        ###############################
        elif detectUsrMsg.detectUserMessage() is 3:
          # 今日のテーマはthemeだよ!
          sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(3) )
          manageScene = 1 # 次の処理へ

          
        # # それ以外のメッセージがあったら
        # elif detectUsrMsg.detectUserMessage() is 2:
        #   generatePb.generatePicturebook(dataFromClient)
        #   sendGD.sendGoogleDrive(dataFromClient)
        #   sendBoccoMsg.sendBoccoMessage(getBoccoMsg.getBoccoMessage(2) )
        #   # sendBoccoMsg.sendBoccoMessage('GoogleDriveにアップロードしたよ')
        #   sleep(3)
        #   sendBoccoPb.sendBoccoPicturebook()
        #   WaitingUserMessage = False
          
        else:
          print('> User message does not found (or Bocco spoke).')



      # whileループ自体を10秒ごとに実行
      sleep(10)

    # if s is not None:
    #   s.close()
    #   print("> CLOSED COMPULSORY! : [s is not None] so closed [s] compulsory.")




  if __name__ == "__main__":
    main()


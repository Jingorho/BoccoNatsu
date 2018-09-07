# coding: utf-8
# 2018.08.22

import random
import os
import setTheme as setTm
import getTheme as getTm

def getBoccoMessage(typeNum):
  # typeNum: 
  # 0: Userメッセージなし(upload検知)->今日はなにを取ったの?
  # 1: トリガー無し->へーそうなんだ
  # 2: 今日のテーマを設定したよ
  # 3: 今日のテーマはXXだよ

  
  path = 'data/boccoMsgDB_' + str(typeNum) + '.txt'

  if os.path.exists(path):
    with open(path) as f:
      # ファイルからテキストを取得して改行コードで分割してlistに格納
      fileContents = f.read()
      messages = fileContents.split("\n")
      # ランダム番目のテキストを抽出
      boccoMessage = messages[random.randrange(len(messages))]


      ##############################################################
      # それぞれのメッセージ固有の処理
      ##############################################################

      
      ###############################
      # 0: メッセージ無し(写真のupload検知のみ)
      # 今日はなにを取ったの？
      ###############################
      # if typeNum is 0:
      #   # なにもしない

      
      ###############################
      # 1: メッセージありだがトリガー無し
      # へーそうなんだ。GoogleDriveに〜
      ###############################
      if typeNum is 1:
        boccoMessage = boccoMessage + 'GoogleDriveにアップロードしたよ'



      ###############################
      # 2: お題設定トリガー「テーマは」あり
      # テーマをthemeに設定したよ!
      ###############################
      if typeNum is 2:
        # テキストの中の'theme'という文字を変数themeで置き換える
        theme = getTm.getTheme()
        boccoMessage = boccoMessage.replace('theme', theme)
        print("theme: " + theme)
        print("boccoMessage: " + boccoMessage)



      ###############################
      # 3: 開始トリガー「おはよう」あり
      # 今日のお題はthemeだよ!
      ###############################
      if typeNum is 3:
          
        # テキストの中の'theme'という文字を変数themeで置き換える
        theme = getTm.getTheme()
        setTm.setTheme(theme)
        boccoMessage = boccoMessage.replace('theme', theme)



      print( '> {' + str(boccoMessage) + '} was returned.')
      return boccoMessage
  
  else:
    print('> {' + path + '} does not be found.')

  

if __name__ == "__main__":
  getBoccoMessage()
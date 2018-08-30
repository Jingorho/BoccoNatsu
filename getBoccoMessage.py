# coding: utf-8
# 2018.08.22

import random
import os
import setTheme as setTm

def getBoccoMessage(typeNum):
  # typeNum: 1は"今日は何を取ったの", 2は"へーそうなんだ"
  
  path = 'data/boccoMsgDB_' + str(typeNum) + '.txt'

  if os.path.exists(path):
    with open(path) as f:
      # ファイルからテキストを取得して改行コードで分割してlistに格納
      fileContents = f.read()
      messages = fileContents.split("\n")
      # ランダム番目のテキストを抽出
      boccoMessage = messages[random.randrange(len(messages))]


      # それぞれのメッセージ固有の処理
      if typeNum is 0:

        # 0(お題表示)だったら追加ファイルからお題をランダムにとって指定
        with open('data/boccoMsgDB_theme.txt') as f:
          # ファイルからテキストを取得して改行コードでlistに格納
          fileContents = f.read()
          themes = fileContents.split("\n")
          # ランダム番目のテキストを抽出
          theme = themes[random.randrange(len(themes))]
          setTm.setTheme(theme)
        # テキストの中の'theme'という文字を変数themeで置き換える
        boccoMessage = boccoMessage.replace('theme', theme)


      # 2(終了報告)だったら'GoogleDriveに〜'を付記する
      if typeNum is 2:
        boccoMessage = boccoMessage + 'GoogleDriveにアップロードしたよ'


      print( '> {' + str(boccoMessage) + '} was returned.')

      return boccoMessage
  
  else:
    print('> {' + path + '} does not be found.')

  

if __name__ == "__main__":
  getBoccoMessage()
# coding: utf-8
# 2018.08.22

import os
import glob
import detectUserMessage as detectUsrMsg

def getPictures(pictureDirName):

  # 元となる画像の読み込み
  pictures = []
  count = 0
  
  if detectUsrMsg.detectUserMessage():
    pictDir = str(os.getcwd()) + '/pictures/' + pictureDirName + '/*.png' #カレントディレクトリからパス取得
    pictures = glob.glob(pictDir)
    
    for pict in pictures:# ファイルの数だけループ
      count = count + 1
  
  else:
    count = 0
    pictures = []    

  print('> Got ' + str(pictures) + ' (' + str(count) + ' pictures) from bocco server.')

  return pictures, count


if __name__ == "__main__":
    getPictures()
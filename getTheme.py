# coding: utf-8
# 2018.08.29

import random

def getTheme():
  
  currentTheme = ""

  with open('data/currentTheme.txt') as currentThemeFile:
    currentThemeFileContents = currentThemeFile.read()
    print("currentThemeFileContents: " + currentThemeFileContents)
    print("type: " + str(type(currentThemeFileContents)))
    
    # theme.txtがなにも書き込まれてなかったら
    if currentThemeFileContents is "":

      with open('data/themes.txt') as themesFile:
        # ファイルからテキストを取得して改行コードでlistに格納
        themesFileContents = themesFile.read()
        themes = themesFileContents.split("\n")
        # ランダム番目のテキストを抽出
        currentTheme = themes[random.randrange(len(themes))]
        print("> currentThemeFileContents is empty so got {" + currentTheme + "} from themes.txt list. ")
            
          
    # theme.txtにすでに書き込まれてたら
    else:
      currentTheme = currentThemeFileContents
      print("> Got {" + currentTheme + "} from currentTheme.txt. ")


    return currentTheme


if __name__ == "__main__":
  getTheme()
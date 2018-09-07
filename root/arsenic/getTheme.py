# coding: utf-8
# 2018.08.29


def getTheme():
  
  theme = ""

  with open('data/theme.txt') as f:
    # ファイルからテキストを取得して改行コードでlistに格納
    theme = f.read()
    
  return theme


if __name__ == "__main__":
    getTheme()
2018.09.07. ユカイ工学インターンシップ Aチーム
###############################
#                             #
#        ぼこなつサーバ          #
#                             #
###############################


# 0. 環境 

- サーバ環境
Ubuntu 14.04.5 LTS (GNU/Linux 4.2.0-42-generic x86_64) 
Python 3.6.5

- ローカル環境
macOS High Sierra v10.13.4
Python 3.6.5


- ライブラリ（他もあったかも）
bocco-api-python（ユカイ工学純正のものではなく画像送信関数を加えたAPI。同梱）
Python Image Library
google-api-python-client
pyDrive
requests




# 1. 実行方法

1) コード一式をuploadしたサーバにログイン

2) main.pyを実行
$ python3 main.py

あとはサーバ側で打つコマンドはない。BOCCOに挨拶したりカメラuploadしたりすると自動でプロセスが進み、一通り終わると最初の「おはよう」待ち状態になる。




# 2. 主なディレクトリ構成
- bocco-api-python : 純正のものに画像送信関数を加えたカスタムAPI
- data : BOCCOのセリフやランダムに出すお題などで参照するデータ
- Picturebook : 図鑑画像が保存される場所、毎回リセットされる
- pictures : カメラからuploadされた写真が保存・蓄積される場所
- resource : 図鑑画像生成に使用する画像たち




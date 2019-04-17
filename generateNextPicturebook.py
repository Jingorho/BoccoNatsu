# coding: utf-8
# 2018.08.28
from PIL import Image, ImageDraw, ImageFont #pipでインストールできないときはpipをupgradeする(現在動いてるのはv18.0)


def generateNextPicturebook(userMessageRows, cnt):

	# 文章長かったら(13行しか格納できない)分割して3枚目以降作成
	if len(userMessageRows) > 13:
		userMessageRows_latter = userMessageRows[14:] # 7行目以降は別の変数に格納
		userMessageRows = userMessageRows[:13] # 後半を切り取り
		print(userMessageRows_latter)
		# 3枚目以降の作成もできるよ. そう、再起ならね！
		generateNextPicturebook(userMessageRows_latter, cnt+1)
		

	# レイアウト用変数
	margin_interval = 15
	margin_top = 66
	margin_left = 140
	margin_toText = 70
	newLineCharCount = 15
	lineInterval = 72

	pictWith = 280
	pictHeight = 210


	# 背景画像の読み込み
	bg = Image.open("resource/notebook.png")
	bg_edit = bg.copy() #上書きを避けるためバックアップ作成

	# フォントの設定(フォントファイルのパスと文字の大きさ)
	font = ImageFont.truetype('/home/bocco/.local/share/fonts/ヒラギノ丸ゴ ProN W4.ttc', 40)
	
	# 文章を1行ずつ書いていく
	for i in range( len(userMessageRows) ):		
		draw_userMessage = ImageDraw.Draw(bg_edit)
		draw_userMessage.text(
			(margin_left, margin_top + i*lineInterval), 
			userMessageRows[i], fill=(0, 0, 0), font=font)

	bg_edit.save('Picturebook/picturebook' + str(cnt) + '.png', quality=95)
	print("> Generated picturebook" + str(cnt) + ".png successfully.")


if __name__ == "__main__":
  generateNextPicturebook()

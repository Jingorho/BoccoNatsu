# coding: utf-8
# 2018.08.28
from PIL import Image, ImageDraw, ImageFont #pipでインストールできないときはpipをupgradeする(現在動いてるのはv18.0)

# count = 1

def generateNextPicturebook(userMessageRows, _count):

	if len(userMessageRows) > 13:
		userMessageRows_latter = userMessageRows[14:]
		userMessageRows = userMessageRows[:13]
		print(userMessageRows_latter)
		# count = count + 1
		generateNextPicturebook(userMessageRows_latter, _count+1)
		
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
	# font = ImageFont.truetype('resource/font/Arial.ttc', 40)
	font = ImageFont.truetype('/home/bocco/.local/share/fonts/ヒラギノ丸ゴ ProN W4.ttc', 40)
	
	# Drawインスタンスを生成
	# userMessage = u'あいうえおアイウエオあいうえおアイウエオあいうえおアイウエオあいうえお'
	for i in range( len(userMessageRows) ):		
		draw_userMessage = ImageDraw.Draw(bg_edit)
		draw_userMessage.text(
			(margin_left, margin_top + i*lineInterval), 
			userMessageRows[i], fill=(0, 0, 0), font=font)

	bg_edit.save('Picturebook/picturebook' + str(_count) + '.png', quality=95)



if __name__ == "__main__":
  generateNextPicturebook()

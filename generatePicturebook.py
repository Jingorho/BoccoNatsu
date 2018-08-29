# coding: utf-8
# 2018.08.22

from PIL import Image, ImageDraw, ImageFont #pipでインストールできないときはpipをupgradeする(現在動いてるのはv18.0)
from PIL.ImageChops import difference
import getUserMessage as getUsrMsg
import getPictures as getPict
import getMetaData as getMtDt
import sendGoogleDrive as sendGD
import random


def generatePicturebook(pictureDirName):
# def generatePicturebook():
	# pictureDirName = '1535433958'
	if pictureDirName is None:
		return
	else:
		print("> GeneratePicturebook() has started.")

		# 写真の読み込み
		getPictsResult = getPict.getPictures(pictureDirName)
		pictPath = getPictsResult[0] # 1つ目の引数に写真本体
		pictCount = getPictsResult[1] # 2つ目の引数に枚数

		# ファイル名で順番をソート
		pictPath.sort()
		print(str(pictPath))
		
		# テキストの読み込み
		getMsgResult = getUsrMsg.getUserMessage()
		userMessage = getMsgResult[0]
		weatherNum = getMsgResult[1]


		# 背景画像の読み込み
		bg = Image.open("resource/notebook.png")

		
		# レイアウト用変数
		margin_interval = 15
		margin_top = 66
		margin_left = 140
		margin_toText = 70
		newLineCharCount = 14
		lineInterval = 70

		pictWith = 280
		pictHeight = 210

		
		###############################
		# 写真書き込み
		###############################
		bg_edit = bg.copy() #上書きを避けるためバックアップ作成

		for i in range(3):

			pict = Image.open('resource/icon/icon' + str(random.randrange(9)) + '.png')
			mask = pict.split()[3] #透過としてRGBのみ抽出
			
			# ループが総枚数を超えたら代替アイコンに置き換える、つまり
			# デフォルトで代替アイコンで、総枚数内でのループではカメラ画像で置き換える
			if pictCount > i:
				pict = Image.open(pictPath[i])
				pict = pict.resize((pictWith, pictHeight)) #カメラからは大きめの画像でくるのでリサイズ
				mask = pict.split()[3] #透過としてRGBのみ抽出
				
			

			# 3枚なのでベタガキで...
			if i == 0:
				bg_edit.paste(pict, (margin_left, margin_top), mask)

			elif i == 1:
				bg_edit.paste(pict, (margin_left + pict.width + margin_interval, margin_top), mask)

			elif i == 2:
				bg_edit.paste(pict, (margin_left, margin_top + pict.height + margin_interval), mask)
			
			# print(str(i) + " : " + pict)

		

		boccoBg = Image.open('resource/boccoBg.png')
		mask = boccoBg.split()[3] #透過としてRGBのみ抽出

		boccoBgX = margin_left + pict.width + margin_interval
		boccoBgY = margin_top + pict.height + margin_interval

		bg_edit.paste(boccoBg, (boccoBgX, boccoBgY), mask)


		
		###############################
		# テキスト書き込み
		###############################
		
		# フォントの設定(フォントファイルのパスと文字の大きさ)
		# font = ImageFont.truetype('resource/font/Arial.ttc', 40)
		font = ImageFont.truetype('/home/bocco/.local/share/fonts/ヒラギノ丸ゴ ProN W4.ttc', 40)
		
		metaData = getMtDt.getMetaData()
		dateStr = metaData[0] #.decode("utf-8")
		# weatherStr = metaData[1] #.decode("utf-8")
		print(str(weatherNum))
		weatherIcon = Image.open('resource/weatherIcon/' + str(weatherNum) + '.png')
		

		# dateStr書く
		drawCenteringTextToImg(0, bg_edit, dateStr, 
							   boccoBg.width, boccoBg.height+60, 
							   boccoBgX, boccoBgY, 
							   font, 2, 0)
		# weatherIcon貼る
		drawCenteringTextToImg(1, bg_edit, weatherIcon, 
							   boccoBg.width, boccoBg.height+60, 
							   boccoBgX, boccoBgY, 
							   font, 2, 1)

		

		# Drawインスタンスを生成
		# userMessage = u'あいうえおアイウエオあいうえおアイウエオあいうえおアイウエオあいうえお'
		userMessageRows = [userMessage[i : i+newLineCharCount] for i in range(0, len(userMessage), newLineCharCount)]
		
		

		for i in range( len(userMessageRows) ):		
			draw_userMessage = ImageDraw.Draw(bg_edit)
			draw_userMessage.text(
				(margin_left, margin_top + pict.height*2 + margin_interval + margin_toText + i*lineInterval), 
				userMessageRows[i], fill=(0, 0, 0), font=font)



		bg_edit.save('Picturebook/picturebook.png', quality=95)
		print("> Generated picturebook successfully.")

		# sendGD.sendGoogleDrive()




###############################
# drawCenteringTextToImg: センタリングをして複数行を画像に合成する処理
###############################
def drawCenteringTextToImg(imgOrTxtNum, bgImg, obj,
						   bgWidth, bgHeight, 
						   initX, initY, 
						   font, allLineNum, lineNum): # allLineNumは全行数、lineNumは行番目(0からスタート)
	if imgOrTxtNum is 0: #TEXT
		# 中央揃えの処理
		msg_width, msg_height = font.getsize(obj)
		msg_x = initX + int(0.5 * (bgWidth - msg_width))
		msg_y = initY + int(0.5 * (bgHeight - msg_height*allLineNum) + font.size*lineNum) # boccoのぴろってやつの60px分下にずらす

		# 文字を書く
		# Drawインスタンスを生成
		draw = ImageDraw.Draw(bgImg)
		draw.text((msg_x, msg_y), obj, fill=(0, 0, 0), font=font)

	else: #IMG
		# 中央揃えの処理
		msg_width, msg_height = obj.size
		msg_x = initX + int(0.5 * (bgWidth - msg_width))
		msg_y = initY + int(0.5 * (bgHeight - msg_height*allLineNum) + msg_height*lineNum) # boccoのぴろってやつの60px分下にずらす

		# 画像を貼る
		mask = obj.split()[3] #透過としてRGBのみ抽出
		bgImg.paste(obj, (msg_x, msg_y), mask)
		

if __name__ == "__main__":
    generatePicturebook()



# coding: utf-8
# 2018.08.22

from PIL import Image, ImageDraw, ImageFont #pipでインストールできないときはpipをupgradeする(現在動いてるのはv18.0)
import random
import datetime

import getUserMessage as getUsrMsg
import getPictures as getPict
import getTheme as getTm
import generateNextPicturebook as generateNextPb
import sendGoogleDrive as sendGD


def generatePicturebook(pictureDirName):
# def generatePicturebook():
# 	pictureDirName = '1535433958'
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
		
		# メッセージとメタデータの読み込み
		getMsgResult = getUsrMsg.getUserMessage()
		userMessage = getMsgResult[0]
		weatherNum = getMsgResult[1]
		try:
			userMessage = getMsgResult[0]
			# userMessage = "メロスは激怒した。必ず、かの邪智暴虐じゃちぼうぎゃくの王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。笛を吹き、羊と遊んで暮して来た。けれども邪悪に対しては、人一倍に敏感であった。きょう未明メロスは村を出発し、野を越え山越え、十里はなれた此このシラクスの市にやって来た。メロスには父も、母も無い。女房も無い。十六の、内気な妹と二人暮しだ。この妹は、村の或る律気な一牧人を、近々、花婿はなむことして迎える事になっていた。結婚式も間近かなのである。メロスは、それゆえ、花嫁の衣裳やら祝宴の御馳走やらを買いに、はるばる市にやって来たのだ。先ず、その品々を買い集め、それから都の大路をぶらぶら歩いた。メロスには竹馬の友があった。セリヌンティウスである。今は此のシラクスの市で、石工をしている。その友を、これから訪ねてみるつもりなのだ。久しく逢わなかったのだから、訪ねて行くのが楽しみである。歩いているうちにメロスは、まちの様子を怪しく思った。ひっそりしている。もう既に日も落ちて、まちの暗いのは当りまえだが、けれども、なんだか、夜のせいばかりでは無く、市全体が、やけに寂しい。のんきなメロスも、だんだん不安になって来た。路で逢った若い衆をつかまえて、何かあったのか、二年まえに此の市に来たときは、夜でも皆が歌をうたって、まちは賑やかであった筈はずだが、と質問した。若い衆は、首を振って答えなかった。しばらく歩いて老爺ろうやに逢い、こんどはもっと、語勢を強くして質問した。老爺は答えなかった。メロスは両手で老爺のからだをゆすぶって質問を重ねた。老爺は、あたりをはばかる低"
			weatherNum = getMsgResult[1]
		except Exception as e:
			# return
			print(e)
			userMessage = 'メッセージなし'
			
		dateStr = datetime.datetime.today().strftime("%-m月%-d日") # ハイフンは0埋めしないためのやつ
		weatherIcon = Image.open('resource/weatherIcon/' + str(weatherNum) + '.png')
		
		

		# 背景画像の読み込み
		bg = Image.open("resource/notebook.png")

		
		# レイアウト用変数
		margin_interval = 15
		margin_top = 66
		margin_left = 140
		margin_toText = 70
		newLineCharCount = 14
		lineInterval = 72

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
			
			

		boccoBg = Image.open('resource/boccoBg.png')
		mask = boccoBg.split()[3] #透過としてRGBのみ抽出

		boccoBgX = margin_left + pict.width + margin_interval
		boccoBgY = margin_top + pict.height + margin_interval

		bg_edit.paste(boccoBg, (boccoBgX, boccoBgY), mask)


		
		###############################
		# テキスト書き込み
		###############################
		
		# フォントの設定(フォントファイルのパスと文字の大きさ)
		font = ImageFont.truetype('/home/bocco/.local/share/fonts/ヒラギノ丸ゴ ProN W4.ttc', 40)
		
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

		# theme書く
		font_theme = ImageFont.truetype('/home/bocco/.local/share/fonts/ヒラギノ丸ゴ ProN W4.ttc', 20)
		theme = getTm.getTheme()
		themeStr = '今日のお題「'+ theme +'」'
		themeStrWidth, themeStrHeight = font_theme.getsize(themeStr)
		print(str(themeStrWidth) + "----")
		draw = ImageDraw.Draw(bg_edit)
		draw.text(
			( (margin_left + margin_interval + pictWith*2) - themeStrWidth, 30), 
			themeStr, 
			fill=(0, 0, 0), 
			font=font_theme)
		

		# newLineCharCount(改行する文字数)で文章を分割してlistに格納
		userMessageRows = [userMessage[i : i+newLineCharCount] for i in range(0, len(userMessage), newLineCharCount)]
		
		# 文章長かったら(6行しか格納できない)分割して2枚目以降作成
		if len(userMessageRows) > 6:
			userMessageRows_latter = userMessageRows[7:] # 7行目以降は別の変数に格納
			userMessageRows = userMessageRows[:6] # 後半を切り取り
			print(userMessageRows_latter)
			# 2枚目以降作成(第二引数は便宜上. 「2」枚目以降の2)
			generateNextPb.generateNextPicturebook(userMessageRows_latter, 2)
		print(userMessageRows)
		

		# 文章を1行ずつ書いていく
		for i in range( len(userMessageRows) ):		
			draw_userMessage = ImageDraw.Draw(bg_edit)
			draw_userMessage.text(
				(margin_left, margin_top + pict.height*2 + margin_interval + margin_toText + i*lineInterval), 
				userMessageRows[i], fill=(0, 0, 0), font=font)


		# 空白だったら
		if (userMessage is not None) and (theme is not None):
			bg_edit.save('Picturebook/picturebook.png', quality=95)
			print("> Generated picturebook successfully.")
		else:
			print("> Some resources may be empty.")




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



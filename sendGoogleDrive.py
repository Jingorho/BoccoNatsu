# coding: utf-8
# 2018.08.24


import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import sendBoccoMessage as sendBcMsg
import getPictures as getPict


def sendGoogleDrive(pictureDirName):
	# 参照: https://qiita.com/akabei/items/f25e4f79dd7c2f754f0e

	dateTitle = datetime.datetime.today().strftime("20%y年%m月%d日")
	fileTitle = dateTitle # + 'の写真'
	folderTitle = dateTitle + 'の写真'
	picturebookTitle = dateTitle + 'のアルバム'

	gauth = GoogleAuth()
	gauth.CommandLineAuth()
	drive = GoogleDrive(gauth)



	# 図鑑のupload
	f_picturebook = drive.CreateFile(
		{
		'title': picturebookTitle+'.png', 
		'mimeType': 'image/jpeg'
		})
	f_picturebook.SetContentFile('Picturebook/picturebook.png')
	f_picturebook.Upload()


	# 写真のupload
	folder = drive.CreateFile(
		{
		'title': folderTitle, 
		'mimeType': 'application/vnd.google-apps.folder'
		})
	folder.Upload()
	


	getPictsResult = getPict.getPictures(pictureDirName)
	pictCount = getPictsResult[1]
	pict = getPictsResult[0]
	
	for i in range(pictCount):

		# pictName = dataからのファイルネーム

		f_picture = drive.CreateFile(
			{
			'title': fileTitle+'_'+str(i)+'.png', 
			'mimeType': 'image/jpeg',
			"parents": [{"kind": "drive#fileLink", "id": folder['id']}]
			})
		# f_picture.SetContentFile('pictures/' + pictureDirName + '/*.png')
		f_picture.SetContentFile(pict[i])
		f_picture.Upload()


	# uploadの報告
	# sendBcMsg.sendBoccoMessage('GoogleDriveにアップロードしたよ') #発言内容を指定して実行
	print('> Uploaded successfully picturebook and pictures to GoogleDrive.')


if __name__ == "__main__":
    sendGoogleDrive()



# coding: utf-8
# 2018.08.24

import datetime
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sendBoccoMessage as sendBcMsg
import getPictures as getPict


def sendGoogleDrive(pictureDirName):
  # 参照: https://qiita.com/akabei/items/f25e4f79dd7c2f754f0e

  pbPath = '/root/Picturebook/'

  dateTitle = datetime.datetime.today().strftime("20%y年%m月%d日")
  fileTitle = dateTitle # + 'の写真'
  folderTitle = dateTitle + 'の写真'
  picturebookTitle = dateTitle + 'のアルバム'

  gauth = GoogleAuth()
  gauth.CommandLineAuth()
  drive = GoogleDrive(gauth)


  ###############################
  # 図鑑のupload
  ###############################
  # 1枚目はデフォルトで必ず送信
  f_picturebook = drive.CreateFile(
    {
    'title': picturebookTitle+'.png', 
    'mimeType': 'image/jpeg'
    })
  f_picturebook.SetContentFile(pbPath+'picturebook.png')
  f_picturebook.Upload()


  # 図鑑のupload n枚目もあったら送信
  if len(os.listdir(pbPath)) > 1:
    # ファイルの数ぶんだけ回す
    for i in range(len(os.listdir(pbPath))):
      # i枚目があったら
      if os.path.exists(pbPath + 'picturebook' + str(i) + '.png'):
        f_picturebook = drive.CreateFile(
        {
          'title': picturebookTitle+'.png', 
          'mimeType': 'image/jpeg'
        })
        f_picturebook.SetContentFile(pbPath + 'picturebook' + str(i) + '.png')
        f_picturebook.Upload()
        print("> {picturebook" + str(i) + ".png} is uploaded to GoogleDrive.")

      else:
        print("> {picturebook" + str(i) + ".png} is not found")

    print('> Send all picturebook to GoogleDrive.')





  ###############################
  # 写真のupload
  ###############################
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
  print('> Uploaded successfully picturebook and pictures to GoogleDrive.')


if __name__ == "__main__":
  sendGoogleDrive()



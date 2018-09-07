# coding: utf-8
# 2018.08.28

import requests
import json
import uuid


def getUserInformation():
  accessToken = ""
  roomUuid = ""

  with open('data/userInfo.txt') as f:
    # ファイルからテキストを取得して改行コードでlistに格納
    data = f.read()
    data = data.split("\n")
    accessToken = data[0]
    roomUuid = data[1]

  return accessToken, roomUuid


if __name__ == "__main__":
  getUserInformation()

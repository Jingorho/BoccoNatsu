# coding: utf-8
# 2018.08.28

from time import sleep
# import sendBoccoMessage as sendBoccoMsg
import sendBoccoPicturebook as sendBoccoPb
import sys


def sendBoccoPictureCertain():
    # msgs = 'aaaaa'

    while True:
      try:
        print("###")
        sendBoccoPb.sendBoccoPicturebook()
        # sendBoccoMsg.sendBoccoMessage(msgs)
        break

      except Exception as e:
        print("----")
        print(e)
        sleep(8)


if __name__ == "__main__":
    sendBoccoPictureCertain()
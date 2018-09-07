# coding: utf-8
# 2018.08.28

from time import sleep
import sendBoccoPicturebook as sendBoccoPb


def trySendBoccoPicture():
    
    while True:
      try:
        print("> Try sendBoccoPicturebook() successfully.")
        sendBoccoPb.sendBoccoPicturebook()
        break

      except Exception as e:
        print("> Exception has occured ... so sleep until allowed too many request.")
        print(e)
        sleep(8)


if __name__ == "__main__":
    trySendBoccoPicture()
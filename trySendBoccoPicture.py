# coding: utf-8
# 2018.08.28

from time import sleep
import sendBoccoPicturebook as sendBoccoPb


def trySendBoccoPicture():
    
    while True:
      try:
        print("> Run sendBoccoPicturebook() successfully.")
        sendBoccoPb.sendBoccoPicturebook()
        break
        # 成功したらその時点でwhileループを出る

      except Exception as e:
        print("> Exception has occurred ... so sleep and repeat running sendBoccoPicturebook() until exception will be allowed.")
        print(e)
        sleep(8)
        # Exceptionになったら、8秒待って再度ループで実行


if __name__ == "__main__":
    trySendBoccoPicture()
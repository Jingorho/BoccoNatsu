
# encoding: utf-8

# アクセストークンの取得
# curl -i "https://api.bocco.me/alpha/sessions" \
#     -d "apikey=4QiLD9c9Qr8IDJE7ALqX6wpAaKPUNGrf69xfTMCO2a9T9MRiHw4BpA5fHjG6KbOE" \
#     -d "email=miyanishi56@gmail.com" \
#     -d "password=3910yuka"

# 取得された情報
# {"access_token":"103148b9423b6967c6e7971c091ea7ed657ede19d3d3a75ca6ae824ffb4cffb5",
#  "uuid":"33e739e3-b6f0-4ab8-9824-3fde9f6e7827"}


# ルームの情報を取得
# curl -i "https://api.bocco.me/alpha/rooms/joined?access_token=103148b9423b6967c6e7971c091ea7ed657ede19d3d3a75ca6ae824ffb4cffb5"


# メッセージを送る
# curl -i "https://api.bocco.me/alpha/rooms/09540d0d-ee72-455c-a248-accbe77ccac6/messages" \
#     -d "access_token=103148b9423b6967c6e7971c091ea7ed657ede19d3d3a75ca6ae824ffb4cffb5" \
#     -d "unique_id=`uuidgen`" \
#     -d "media=text" \
#     -d "text=今日は何があったの？" \
#     -H "Accept-Language: ja"


# メッセージを取得する
# curl -i "https://api.bocco.me/alpha/rooms/09540d0d-ee72-455c-a248-accbe77ccac6/messages?access_token=103148b9423b6967c6e7971c091ea7ed657ede19d3d3a75ca6ae824ffb4cffb5&newer_than=80"


# 画像を送る
# curl -i "https://api.bocco.me/alpha/rooms/09540d0d-ee72-455c-a248-accbe77ccac6/messages" \
#     -d "access_token=103148b9423b6967c6e7971c091ea7ed657ede19d3d3a75ca6ae824ffb4cffb5" \
#     -d "unique_id=`uuidgen`" \
#     -d "media=image" \
#     -d "image=/Users/yukako/WorkSpace/Bocco/pictures/uuid0.png" \
#     -H "Accept-Language: ja"


# Google Drive の OAuthクライアント情報
# クライアントID
# 769378775709-fm8ai1jc458cmjn3d6t2hap4g66q7eqk.apps.googleusercontent.com
# クライアントシークレット
# Ny5LhXCYzQ0-gnVXM28TxUQO







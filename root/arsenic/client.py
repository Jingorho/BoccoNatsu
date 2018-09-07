import socket
from contextlib import closing
import sys

s = socket.socket()

port = 25565
data = "1535349541"
#with closing(s):
s.connect(('210.152.82.232', port))
s.send(data.encode())
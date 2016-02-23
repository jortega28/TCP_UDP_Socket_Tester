from Socket import mysocket
import time
socket = mysocket()

host = "127.0.0.1"
port = 2696

while True:
    socket.connect(host, port)
    socket.myreceive()
    time.sleep(1)

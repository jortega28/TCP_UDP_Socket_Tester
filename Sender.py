from Socket import mysocket
import time
socket = mysocket()

host = "127.0.0.1"
port = 2696

while True:
    socket.connect(host, port)
    socket.mysend("Hello " + host + " on port " + port)
    time.sleep(1)

import socket
import time

def initserver(tcp_ip, tcp_port, buffer_size, successes):
    connected = 0
    while connected != 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((tcp_ip, tcp_port))
            s.listen(1)
            conn, addr = s.accept()
            print("Connection established!")
            connected = 1
            print("Connection address:", addr)
            # print("Connection port: " + s.getsockname()[1])
            success = 0
            while success != successes:
                data = conn.recv(buffer_size)
                acknowledge = socket.gethostbyname(socket.gethostname()) + " Says: I'm listening!"
                if not data:
                    break
                print("received data:", data)
                print("Sending: " + acknowledge)
                conn.send("1".encode())
                success += 1.
            conn.close()
        except Exception as e:
            print("Could not establish a connection... trying again in 1 seconds!")
        finally:
            time.sleep(1)

# The IP here should just be the local host
initserver("127.0.0.1", 2696, 1024, 5)

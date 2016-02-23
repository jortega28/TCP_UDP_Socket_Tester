import socket
import time

def initserver(udp_ip, udp_port, buffer_size, successes):
    connected = 0
    while connected != 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((udp_ip, udp_port))
            connected = 1
            success = 0
            while success != successes:
                data, addr = s.recvfrom(buffer_size)
                # acknowledge = socket.gethostbyname(socket.gethostname()) + " Says: I'm listening!"
                if not data:
                    break
                print("received data:", data)
                # print("Sending: I'm Listening!")
                s.sendto("1".encode(), addr)
                success += 1
        except Exception as e:
            print("Could not establish a connection... trying again in 1 second!")
        finally:
            time.sleep(1)

# IP here should be the IP of the server without using 127.0.0.1
initserver("192.168.0.102", 2696, 1024, 5)

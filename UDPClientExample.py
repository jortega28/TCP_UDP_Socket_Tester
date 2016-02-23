import socket

UDP_IP = "192.168.0.102"
UDP_PORT = 2696
MESSAGE = "Is anybody listening?"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

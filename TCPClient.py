import socket
import time

def initclient(tcp_ip, tcp_port, buffer_size, message, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))
    success = 0
    while success != successes:
        startTime = time.time()
        s.send(message.encode())
        data = s.recv(1)
        endTime = time.time()
        elapsedTime = endTime-startTime
        # print("received data:", data)
        print(str(elapsedTime))
        success += 1

    s.close()

def rtt(tcp_ip, tcp_port, buffer_size, file_to_use, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))

    f = open(file_to_use + ".txt", 'r')
    message = f.read()
    success = 0
    while success != successes:
        startTime = time.time()
        s.send(message.encode())
        data = s.recv(1)
        endTime = time.time()
        elapsedTime = endTime-startTime
        elapsedTime = elapsedTime*1000000
        # print("received data:", data)
        print(str(elapsedTime))
        success += 1

    s.close()

def throughput(tcp_ip, tcp_port, buffer_size, file_to_use, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))

    f = open(file_to_use + ".txt", 'r')
    message = f.read()
    success = 0
    while success != successes:
        startTime = time.time()
        s.send(message.encode())
        data = s.recv(1)
        endTime = time.time()
        elapsedTime = endTime-startTime
        elapsedTime = elapsedTime*1000000
        # print("received data:", data)
        print(str((1024*64)/elapsedTime))
        success += 1

    s.close()

def interations(tcp_ip, tcp_port, buffer_size, file_to_use, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))

    f = open(file_to_use + ".txt", 'r')
    message = f.read()
    success = 0
    while success != successes:
        startTime = time.time()
        s.send(message.encode())
        time.sleep(1)
        data = s.recv(1)
        endTime = time.time()
        elapsedTime = endTime-startTime
        # print("received data:", data)
        print(str(elapsedTime))

        success += 1

    s.close()

# The IP here should be the servers IP
throughput("192.168.1.151", 2696, 1024*64, "64KB", 1000)

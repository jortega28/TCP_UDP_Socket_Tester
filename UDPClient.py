import socket
import time

def initclient(udp_ip, udp_port, buffer_size, message, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind((udp_ip, udp_port))
    # f = open(file_to_use + ".txt", 'r')
    # message = f.read()
    success = 0
    while success != successes:
        startTime = time.time()
        s.sendto(message.encode(), (udp_ip, udp_port))
        data, addr = s.recvfrom(buffer_size)
        endTime = time.time()
        elapsedTime = endTime-startTime
        elapsedTime = elapsedTime*1000000
        # print("received data:", data)
        print(str(elapsedTime))
        success += 1
    s.close()

def rtt(udp_ip, udp_port, buffer_size, file_to_use, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind((udp_ip, udp_port))
    f = open(file_to_use + ".txt", 'r')
    message = f.read()
    success = 0
    while success != successes:
        startTime = time.time()
        s.sendto(message.encode(), (udp_ip, udp_port))
        data, addr = s.recvfrom(1)
        endTime = time.time()
        elapsedTime = endTime-startTime
        elapsedTime = elapsedTime*1000000
        # print("received data:", data)
        print(str(elapsedTime))
        success += 1
    s.close()

def throughput(udp_ip, udp_port, buffer_size, file_to_use, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind((udp_ip, udp_port))
    f = open(file_to_use + ".txt", 'r')
    message = f.read()
    values = []
    success = 0
    while success != successes:
        startTime = time.time()
        s.sendto(message.encode(), (udp_ip, udp_port))
        data, addr = s.recvfrom(1)
        endTime = time.time()
        elapsedTime = endTime-startTime
        elapsedTime = elapsedTime*1000000
        # print("received data:", data)
        values.append(elapsedTime)
        if len(values) == 32:
            print(str(((1024*1024)/sum(values))))
            values = []
        success += 1
    s.close()

def throughput16(udp_ip, udp_port, buffer_size, file_to_use, successes):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind((udp_ip, udp_port))
    f = open(file_to_use + ".txt", 'r')
    message = f.read()
    success = 0
    while success != successes:
        startTime = time.time()
        s.sendto(message.encode(), (udp_ip, udp_port))
        data, addr = s.recvfrom(1)
        endTime = time.time()
        elapsedTime = endTime-startTime
        elapsedTime = elapsedTime*1000000
        # print("received data:", data)
        print(str((1024*16)/elapsedTime))
        success += 1
    s.close()

# IP here should be the servers IP
# rtt("192.168.0.104", 2696, 1024*1, "1KB", 1000)
throughput("192.168.0.104", 2696, 1024*32, "32KB", 32000)

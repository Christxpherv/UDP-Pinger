import time
import random
from socket import *

# create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# assign IP address and port number to socket
serverSocket.bind(('', 12000))

# list to store received heartbeats
received_heartbeats = []

print('Server is running and listening for heartbeats...')

while True:
    # generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # receive the heartbeat packet
    message, address = serverSocket.recvfrom(1024)
    message = message.decode()

    # if rand is less than 4, we consider the packet lost and do not process it
    if rand < 4:
        print(f'Heartbeat packet dropped: {message}')
        continue

    # split the message to get sequence number and timestamp
    parts = message.split()
    seq_num = int(parts[1])
    timestamp = float(parts[2])

    # calculate the time difference
    time_diff = time.time() - timestamp

    # store the received heartbeat
    received_heartbeats.append((seq_num, timestamp))

    print(f'Received heartbeat: {message}')
    print(f'Time difference: {time_diff} seconds')

    # check for missing heartbeats
    missing_heartbeats = [i for i in range(received_heartbeats[0][0], seq_num) if i not in [beat[0] for beat in received_heartbeats]]
    if missing_heartbeats:
        print(f'Missing heartbeats: {missing_heartbeats}')

# close the socket
serverSocket.close()
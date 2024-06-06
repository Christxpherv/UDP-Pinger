import socket
import time

# server address and port
serverAddress = ('localhost', 12000)

# create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set the number of heartbeats to be sent
heartbeats = 10

# sequence number for heartbeats
seq_num = 0

# loop to send heartbeats
for i in range(heartbeats):
    # create message with sequence number and timestamp
    message = f'HEARTBEAT {seq_num} {time.time()}'

    # send the message
    clientSocket.sendto(message.encode(), serverAddress)

    print(f'Sent heartbeat: {message}')

    # increment sequence number
    seq_num += 1

    # wait for 1 second before sending the next heartbeat
    time.sleep(1)

# close the socket
clientSocket.close()
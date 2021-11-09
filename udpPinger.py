import socket
import time

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
 
# Create a UDP socket at client side
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.settimeout(1)
# Send to server using created UDP socket
for i in range(10): 
    msgFromClient       = "Ping "+ str(i+1) +" "+ str(time.time())
    bytesToSend         = str.encode(msgFromClient)
    sendtime = time.time()
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    try:
        recvtime = time.time()
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msgFromServer[1])
        print(msg)
        print(recvtime-sendtime)
    except TimeoutError:
        print('Request timed out')
            
UDPClientSocket.close()


# send 10 pings
# print response and calculate rtt
# else request timeout
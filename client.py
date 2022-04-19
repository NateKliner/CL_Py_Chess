import socket
import time
import sys
import select

ip = (socket.gethostname(), 1241)
#other = "10.12.112.173"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(ip)

#for line in sys.stdin:
#conn.send(line, ip)
#sent = False

while True:
    #msg = "hello sir"
    try:
        for msg in sys.stdin:
            s.sendto(msg, ip)
            break
        print("waiting")
        data, server = s.recvfrom(1024)
        print("recieved: " + data)
        
    except:
        print("error")
    time.sleep(1)

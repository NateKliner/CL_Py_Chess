import socket
ip = (socket.gethostname(), 1241)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ip)
#s.listen(5)

print(ip)

while True:
    
    #conn, address = s.accept()
    print("Waiting")
    data, address = s.recvfrom(1024)
    print("recieved: " + data)

    if data:
        sent = s.sendto("got it sir", address)
        print("server.pynt data")

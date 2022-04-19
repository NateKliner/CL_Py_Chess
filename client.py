import socket
import time
import sys
import select
import chess

ip = (socket.gethostname(), 1244)
#other = "10.12.112.173"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(ip)
boardTemp = chess.Board()
print("---Board Layout---")
print("8|")
print("7|")
print("6|")
print("5|")
print("4|")
print("3|")
print("2|")
print("1|")
print("  ---------------")
print("  a b c d e f g h\n")
print("Game Start, you are upper-case!\n")
print(boardTemp)

while True:
    #msg = "hello sir"
    try:
        for msg in sys.stdin:
            s.sendto(msg.encode(), ip)
            break
        print("waiting")
        data, server = s.recvfrom(1024)
        board = chess.Board(data.decode())
        print(board)
        print("_______________NEXT BOARD_______________")
        
    except Exception as e:
        print(e)
    time.sleep(1)

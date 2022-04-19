import socket
import chess
ip = (socket.gethostname(), 1244)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ip)

print(ip)
board = chess.Board()
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
print("Game Start, you are lower-case!\n")
print(board)
while True:
    
    #conn, address = s.accept()
    print("Waiting")
    data, address = s.recvfrom(1024)
    gameMove = data.decode("utf-8")
    print("recieved: " + gameMove)
    gameMoveStripped = gameMove.strip()
    try:
        if chess.Move.from_uci(gameMoveStripped) in board.legal_moves:
            processedMove = chess.Move.from_uci(gameMoveStripped)
            board.push(processedMove)
            if board.is_checkmate():
                sent = s.sendto("Checkmate, you win :)".encode(), address)
            else:
                sent = s.sendto(board.epd().encode(), address)
                print(board)
                print("_______________NEXT BOARD_______________")
        else:
            sent = s.sendto("Illegal move".encode(), address)
    except:
        sent = s.sendto("Illegal move".encode(), address)

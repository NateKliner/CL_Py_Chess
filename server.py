import socket
import chess
import sys
ip = (socket.gethostname(), 1244)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ip)
#s.listen(5)

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
turnNumber = 0
while True:
    turnNumber += 1
    clientTurn = True
    while clientTurn:
        #conn, address = s.accept()
        print("Waiting")
        data, address = s.recvfrom(1024)
        gameMove = data.decode("utf-8")
        print("recieved: " + gameMove)
        gameMoveStripped = gameMove.strip()
        try:
            #this if might not be necessary with the try statement
            if chess.Move.from_uci(gameMoveStripped) in board.legal_moves:
                clientTurn = False;
                processedMove = chess.Move.from_uci(gameMoveStripped)
                board.push(processedMove)
                if board.is_checkmate():
                    sent = s.sendto("Checkmate, you win :)".encode(), address)
                    print("Checkmate, you lose :(")
                else:
                    sent = s.sendto(board.epd().encode(), address)
                    print(board)
                    print("_______White's Move_______")
            else:
                sent = s.sendto("Illegal move".encode(), address)
        except:
            sent = s.sendto("Illegal move".encode(), address)


    #servers turn
    serverTurn = True
    while serverTurn:
        print("\nYour Turn:")
        for msg in sys.stdin:
            msgStripped = msg.strip()
            try:
                if chess.Move.from_uci(msgStripped) in board.legal_moves:
                    serverTurn = False
                    processedMove = chess.Move.from_uci(msgStripped)
                    board.push(processedMove)
                    
                    if board.is_checkmate():
                        sent = s.sendto("Checkmate, you lose :(".encode(), address)
                        print("Checkmate, you win :)")
                    else:
                        sent = s.sendto(board.epd().encode(), address)
                        print(board)
                        print("______Move Number: " + str(turnNumber) + "______")
                else:
                    print("Illegal move")
            except Exception as e:
                print(e)
                print("Illegal move")
            break

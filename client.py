import socket
import sys
import select
# open the socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen on port 5555
my_socket.connect(("localhost", 5555))
# call select which will alert if any sources have data to be read
running = True
while running:
    # inputready is a list to check if the input is available for reading
    # outputready is a list to check if the input is availble for writing
    # exceptready is a list to check if the input is an exception
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])
    #when the server has something new to send, this will receive it and display it on the screen. 
    for s in inputready:
        # if input source is the socket, get the msg and display
        if s == my_socket:
            # receive data from the server
            msg = s.recv(1024)

            if msg:
                print msg
            else:
                print"Disconnected from server!"
                running = False
        # if input source is from the keyboard, get the msg and send it
        elif s == sys.stdin:
            msg = s.readline()
            my_socket.sendall(msg)
# send data to the server

# close the connection
my_socket.close()
import socket
import threading
import random
from _thread import *

connections = []
players = []

x = random.randint(1, 51)
print("correct choice ",x)



def clientthread(conn, addr,connections,players):
    welcome_note = '$ welcome to Guess game $  and guess a number between 1 and 50'
    high = 'guess is greater than value!'
    low = 'guess is lesser than value!'
    conn.send(welcome_note.encode())
    print("enter your name")

    try:
        data = conn.recv(1024)
    except:
        return
    username = data.decode()
    players.append(username)
    print('user -->' + str(addr) + ' : ' + "username:" + username)
    conn.send(''.encode())
    while True:
        answer = b''
        try:
            answer = conn.recv(1024)
            print('Guess :  ' + answer.decode())
        except:
            break
        for connx in connections:
            if connx != conn and answer != b'listplayers':
                msg = username + " gussed " + answer.decode()
                connx.send(msg.encode())
        if (str(answer.decode()) == 'listplayers'):
            plyrs = '\n'+'\n'.join(i for i in players)
            conn.send(plyrs.encode())
        elif (int(answer.decode()) > x):
            conn.send(high.encode())
        elif (int(answer.decode()) < x):
            conn.send(low.encode())
        else:
            conn.send('guess is correct'.encode())
            for connx in connections:
                result = "Winner is " + username + " gameover"
                connx.send(result.encode())
            break
    conn.close()


host = '127.0.0.1'
port  = 5000
s = socket.socket()
s.bind((host, port))
s.listen(10)
print('socket is ready')
while True:
    conn, addr = s.accept()
    print('connected from  ' + str(addr))
    connections.append(conn)
    start_new_thread(clientthread, (conn, addr,connections,players))
s.close()
import socket
import random
import threading


def Main():
    host  = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    s.listen(10)

    while True:
        c, addr = s.accept()
        print ('connection from : '+ str(addr))
        initial = 'welcome to guess my number'
        c.send(str(initial).encode())
        threading.Thread(target = Guess, args = (c, addr)).start()

def Guess(c, addr):
    connection = True
    num = random.randrange(1,101)
    while connection:
        option1 = 'correct!'
        option2 = 'your number is less than guess'
        option3 = 'your number is greater than guess'
        data = c.recv(1024).decode()
        data = int(data)
        if not data:
            break
        print ("from connected user : " + str(data))
        if(data == num):
            c.send(str(option1).encode())
            connection = False
            break
        elif(data < num):
            c.send(str(option2).encode())
        elif(data >  num):
            c.send(str(option3).encode())
    print("server closed from" + str(addr))
    c.close()

if __name__ == '__main__':
    Main()
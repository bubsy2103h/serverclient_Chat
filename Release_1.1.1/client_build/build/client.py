import socket

ip = raw_input("server ip: ")
secure = False
s = socket.socket()
s.connect((ip, 12345))
s.setblocking(1)
#Authenticate
while not secure:
    m11 = s.recv(1024)
    m12 = s.recv(1024)
    print 'Server: ', m12
    if m11 == '_PasswordRequest_':
        password = raw_input('Type in Password: ')
        s.send(password)
    else:
        print "Error! Server uses invalid authentication type"
    m21 = s.recv(1024)
    m22 = s.recv(1024)
    print 'Server: ', m22
    if m21 == '_PasswordCorrect_':
        secure = True




#chat
while True:
    message = raw_input("client: ")
    s.send(message)
    mss = s.recv(1024)
    print 'server: ', mss
s.close



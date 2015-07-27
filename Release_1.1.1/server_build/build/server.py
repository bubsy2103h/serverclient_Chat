
import time
import socket               # Import socket module

password = 'bobber03'
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.setblocking(1)
s.listen(5)                # Now wait for client connection.
#Application 
while True:
   c, addr = s.accept()     # Establish connection with client.
   secure = False
   print 'Got connection from', addr
   #Authenticate
   print 'Authenticating...'
   while not secure:
      c.send('_PasswordRequest_')
      c.send("Authentication Required")
      curpass  = c.recv(1024)
      if curpass == password:
         secure = True
         c.send('_PasswordCorrect_')
         c.send('Authentication Succsessful')
         print 'Authentication Successful'
      else:
         c.send('_PasswordIncorrect_')
         c.send('Authentication Failed, Password Incorrect')
      time.sleep(2)
   #Chat
   while True:
      mss = c.recv(1024)
      print 'client: ', mss
      message = raw_input("Server: ")
      c.send(message)
   
   c.close()                # Close the connection

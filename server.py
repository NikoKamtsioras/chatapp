from settings import *
import socket            

s = socket.socket()        
print ("Socket successfully created")
 
s.bind((server_ip, default_port))        
print ("socket binded to %s" %(default_port))
 
s.listen(5)    
print ("socket is listening")           
 
while True:
  c, addr = s.accept()    
  print ('Got connection from', addr )
  c.send('Thank you for connecting'.encode())


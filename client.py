import socket
import CA
from AESCipher import AESCipher


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 9500

s.connect((server, port))


#gets a certificate from the server
server_cert = s.recv(1024)

#The if function is checking to see if the certificate received by the server is known by CA. If it is known,
#a message will be encrypted and sent
if CA.knownCert(server_cert) == server_cert:
    key = CA.getPublicKey()
    cipher = AESCipher(key)
    message = cipher.encrypt('I guess we know each other.')
    s.send(message)
    server_message = s.recv(1024)
    print(cipher.decrypt(server_message))

    s.close()

#A certificate that is not known will instead send a message of 'goodbye' and the connection is closed
else:
    farewell = 'goodbye'
    s.send(farewell.encode())
    s.close() 



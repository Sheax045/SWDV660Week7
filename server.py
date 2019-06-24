import socket
from Crypto.Hash import SHA256
from AESCipher import AESCipher



#Certificate and public key info
server_name = 'youknowme'
hasher = SHA256.new(server_name.encode('utf-8'))
certificate = hasher.digest()
key = 'This is the public key'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket successfully created')
port = 9500
server_address = ('', port)

s.bind(server_address)
print('Socket binded to %s' %(port))

s.listen(1)
print('Socket is listening')



while True:

    c, addr = s.accept()
    #sends certificate 
    c.send(certificate)

    cipher = AESCipher(key)

    #receives encrypted information if certificate is valid
    client_message = c.recv(128)
    updated_message = client_message.decode('utf-8')
    if updated_message == 'goodbye':
        print(updated_message)
        c.close()
    
    else:
        #decrypts information
        decrypted_message = cipher.decrypt(client_message)
        print(decrypted_message)

        c.send(cipher.encrypt('We sure do.'))

        c.close()



    
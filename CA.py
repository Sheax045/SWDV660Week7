#However, it order to validate the server is actually the server, you will need to write 
#another application called the CA or Certificate Authority. The CA will accept a 'certificate' 
#and return the public key associated with the certificate or null depending on whether or not 
#the CA knows the 'certificate'. You can choose what you use for a certificate.

from Crypto.Hash import SHA256


known_name_list = []

#function adds a certificate to the known_name_list
def add(certificate):
    known_name_list.append(certificate)

#function checks to see if certificate is in the known_name_list
def knownCert(certificate):
    if certificate in known_name_list:
        return certificate
    else:
        return ''
    
#gets public key
def getPublicKey():
    p_key = 'This is the public key'
    return p_key


def main():

    #This adds the specific server_name(certificate) below to the known_name_list
    server_name = 'youknowme'
    #Converts the string into bytes to be acceptable by hash function.
    hasher = SHA256.new(server_name.encode('utf-8'))
    #Returns the encoded data in byte format.
    certificate = hasher.digest()
    add(certificate)

main()
    
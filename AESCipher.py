import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


bs = 32
pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
unpad = lambda s : s[:-ord(s[len(s) - 1:])]  


class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )


    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[AES.block_size:])).decode('utf-8')

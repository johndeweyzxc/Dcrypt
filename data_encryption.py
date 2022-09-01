import os
from stat import S_ISDIR
import crypto_dcrypt

class DataEncryption:
    def __init__(self, key):
        self.key = key
    
    def encrypt_string(self, data):
        encrypted_data = crypto_dcrypt.dcrypt(data.encode(), self.key)
        return encrypted_data.decode()
    
    def decrypt_string(self, data):
        decrypted_data = crypto_dcrypt.dcrypt(data.encode(), self.key)
        return decrypted_data.decode()
    
    def encrypt_file(self, file):
        
        with open(file, "rb") as readf:
            content = readf.read()
            with open(file, "wb") as writef:
                writef.write(crypto_dcrypt.dcrypt(content, self.key))
    
    def decrypt_file(self, file):

        with open(file, "rb") as readf:
            content = readf.read()
            with open(file, "wb") as writef:
                writef.write(crypto_dcrypt.dcrypt(content, self.key))
    
    def encrypt_entire_directory(self, path):
        for i in os.listdir(path):
            path_name = os.path.join(path, i)
            properties = os.stat(path_name).st_mode

            # Checks if it is a file or a directory, if it is a file then perform 
            # encryption on that file but if it is a directory we perform a 
            # recursive call with the path of that directory.
            if S_ISDIR(properties):
                self.encrypt_entire_directory(path_name)
            else:
                self.encrypt_file(path_name)
    
    def decrypt_entire_directory(self, path):
        for i in os.listdir(path):
            path_name = os.path.join(path, i)
            properties = os.stat(path_name).st_mode

            if S_ISDIR(properties):
                self.encrypt_entire_directory(path_name)
            else:
                self.encrypt_file(path_name)   
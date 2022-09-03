from data_encryption import DataEncryption

# Encrypting entire directory including its sub directory
path = "C:\\Users\\Johnd\\Desktop\\Github Projects\\Dcrypt\\Example_Directory"
key_path = b"fjwif83jvldpepol"
dcrypt_crypto = DataEncryption(key_path)
# Perform Encryption
dcrypt_crypto.encrypt_entire_directory(path)
# Perform Decryption
# dcrypt_crypto.decrypt_entire_directory(path)

# Encrypting a string
string = "This data will be encrypted..."
key_string = b"fj38v7fhejdk2095"
dcrypt_crypto = DataEncryption(key_string)
# Perform Encryption
encrypted_data = dcrypt_crypto.encrypt_string(string)
print(f"Encrypted message: {encrypted_data}")
# Perform Decryption
decrypted_data = dcrypt_crypto.decrypt_string(encrypted_data)
print(f"Decrypted message: {decrypted_data}")

from data_encryption import DataEncryption

# ENCRYPTING AN ENTIRE DIRECTORY
path = "C:\\PathToExampleDirectory\\Example_Directory"
key_path = b"fjwif83jvldpepol"
data_encrypt = DataEncryption(key_path)
# Perform Encryption
data_encrypt.encrypt_entire_directory(path)
# Perform Decryption
# data_encrypt.decrypt_entire_directory(path)

# ENCRYPTING A STRING
string = "This data will be encrypted..."
key_string = b"fj38v7fhejdk2095"
data_encrypt = DataEncryption(key_string)
# Perform Encryption
encrypted_data = data_encrypt.encrypt_string(string)
print(f"Encrypted message: {encrypted_data}")
# Perform Decryption
decrypted_data = data_encrypt.decrypt_string(encrypted_data)
print(f"Decrypted message: {decrypted_data}")
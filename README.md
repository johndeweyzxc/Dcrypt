## Usage

```python
from data_encryption import DataEncryption

# Encrypting entire directory including its sub directory
path = "C:\\PathToExampleDirectory\\Example_Directory"
key_path = b"fjwif83jvldpepol"
dcrypt_crypto = DataEncryption(key_path)
# Perform Encryption
dcrypt_crypto.encrypt_entire_directory(path)
# Perform Decryption
dcrypt_crypto.decrypt_entire_directory(path)

```

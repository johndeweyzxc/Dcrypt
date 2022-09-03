# Dcrypt Encryption Tool

Dcrypt is an encryption tool capable of encrypting files and directories. When encrypting directories it also encrypts directories inside of it. I originally wrote the program on April 2022, I was reading a book about cryptography and I decided to make a small encryption program for fun.

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

## What I learned

<li>Symmetric Cryptography</li>
<li>XOR Function</li>
<li>Recursion</li>
<li>Stack Data Structure</li>

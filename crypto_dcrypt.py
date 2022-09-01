
def shift_16_bytes(bytes_to_shift):
    shifted_bytes = []

    for i, m in enumerate(bytes_to_shift):
        # Shift bytes in an array
        # [b1, b2, b3, b4, b5, b6] = [b4, b5, b6, b1, b2, b3]
        calc_index = bytes_to_shift[(i + 3) % len(bytes_to_shift)]
        index = bytes_to_shift.index(calc_index)
        shifted_bytes.append(bytes_to_shift[index].to_bytes(1, "big"))

    # Then reverse the array
    # [b4, b5, b6, b1, b2, b3] = [b3, b2, b1, b6, b5, b4]
    shifted_bytes.reverse()
    
    return b"".join(shifted_bytes)

def xor_bytes(bytes_to_xor, key):
    xored = []

    for i, m in enumerate(bytes_to_xor):
        # Peform XOR operation on each byte of data to each byte of key.
        xor = (bytes_to_xor[i] ^ key[i]).to_bytes(1, "big")
        xored.append(xor)

    return b"".join(xored)

def dcrypt(data, key):
    # This function is responsible for encrypting the data, by default
    # it takes a 128 bit of data and performs encryption.

    SIZE = 16
    
    if len(key) == SIZE:
        block = []
        encrypted = []
        pos = 0

        while len(data) > pos:
            block.append(data[pos])
            pos += 1

            # Steps in encryption            
            # Step 1. XOR data and key
            # Step 2. Shift the bytes
            # Step 3. XOR the shifted bytes and key

            # For decryption the step is the same as encryption

            if pos == len(data):
                get_key = key[:len(block) + 1]
                first_xor = xor_bytes(block, get_key)
                shift_bytes = shift_16_bytes(first_xor)
                last_xor = xor_bytes(shift_bytes, get_key)

                encrypted.append(last_xor)
            
            if len(block) == SIZE:
                first_xor_b = xor_bytes(block, key)
                shift_bytes_b = shift_16_bytes(first_xor_b)
                last_xor_b = xor_bytes(shift_bytes_b, key)

                encrypted.append(last_xor_b)
                block = []
    
    else:
        raise Exception(
            f"""Key size error 128 bit is required.
            """
        )
    
    return b"".join(encrypted)
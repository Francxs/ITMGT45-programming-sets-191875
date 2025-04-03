def shift_letter(letter, shift):
    """
    Shift a letter right by the given number, wrapping around if needed.
    Preserves spaces without shifting them.
    
    Args:
        letter (str): A single uppercase English letter or space
        shift (int): Number of positions to shift the letter
        
    Returns:
        str: The letter shifted appropriately or space if input was space
    """
    # Handle space case
    if letter == " ":
        return " "
    
    # Convert letter to ASCII value (A=65, Z=90)
    ascii_val = ord(letter)
    
    # Apply shift with wrapping (modulo 26 for alphabet length)
    shifted_val = ((ascii_val - ord('A') + shift) % 26) + ord('A')
    
    return chr(shifted_val)


def caesar_cipher(message, shift):
    """
    Apply a Caesar cipher to a message of uppercase letters and spaces.
    
    Shifts each letter in the message by the specified amount,
    wrapping around if necessary. Spaces remain unchanged.
    
    Args:
        message (str): A string of uppercase English letters and spaces
        shift (int): Number of positions to shift each letter
        
    Returns:
        str: The encrypted message
    """
    result = []
    
    for char in message:
        result.append(shift_letter(char, shift))
    
    return ''.join(result)


def shift_by_letter(letter, letter_shift):
    """
    Shift a letter by the numeric value of another letter.
    
    A=0, B=1, ..., Z=25
    
    Args:
        letter (str): A single uppercase English letter or space
        letter_shift (str): A single uppercase English letter
        
    Returns:
        str: The shifted letter, or space if input was space
    """
    # Handle space case
    if letter == " ":
        return " "
    
    # Calculate shift amount from letter_shift
    # A=0, B=1, ..., Z=25
    shift_amount = ord(letter_shift) - ord('A')
    
    # Use the existing shift_letter function for the actual shifting
    return shift_letter(letter, shift_amount)


def vigenere_cipher(message, key):
    """
    Apply a Vigenere cipher to encrypt a message using a keyword.
    
    Each letter is shifted by the value of the corresponding letter in the key.
    The key is repeated as needed to match the message length.
    Spaces are preserved unchanged.
    
    Args:
        message (str): A string of uppercase English letters and spaces
        key (str): A string of uppercase English letters (no spaces)
        
    Returns:
        str: The encrypted message
    """
    result = []
    key_index = 0
    
    for char in message:
        if char == " ":
            # Preserve spaces without incrementing key_index
            result.append(" ")
        else:
            # Get the current key letter and increment the index
            key_letter = key[key_index % len(key)]
            result.append(shift_by_letter(char, key_letter))
            key_index += 1
    
    return ''.join(result)


def scytale_cipher(message, shift):
    """
    Encrypt a message using the scytale cipher method.
    
    1. Ensure message length is a multiple of shift, padding with underscores if needed
    2. Construct the encoded message by rearranging characters according to the formula
    
    Args:
        message (str): A string of uppercase English letters and underscores
        shift (int): A positive integer shift value
        
    Returns:
        str: The encoded message
    """
    # Step 1: Ensure message length is a multiple of shift
    padding_needed = (shift - (len(message) % shift)) % shift
    padded_message = message + "_" * padding_needed
    
    # Step 2: Construct the encoded message
    rows = len(padded_message) // shift
    encoded = []
    
    for i in range(len(padded_message)):
        # Calculate the index in the original message using the formula
        original_index = (i // rows) + (i % rows) * shift
        encoded.append(padded_message[original_index])
    
    return ''.join(encoded)


def scytale_decipher(message, shift):
    """
    Decrypt a message that was encrypted with the scytale cipher.
    
    Reverses the encryption process by applying the inverse formula.
    
    Args:
        message (str): The encrypted message
        shift (int): The same shift value used for encryption
        
    Returns:
        str: The decrypted message
    """
    rows = len(message) // shift
    decrypted = [''] * len(message)
    
    for i in range(len(message)):
        # Calculate the original position
        original_position = (i // rows) + (i % rows) * shift
        decrypted[original_position] = message[i]
    
    return ''.join(decrypted)

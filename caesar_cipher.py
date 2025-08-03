# The Caesar Cipher is a simple substitution cipher that shifts letters of the alphabet.

# --- Constants for the ASCII range of uppercase letters ---
# Get the ASCII (ordinal) value of 'A'.
FIRST_CHAR_CODE = ord("A")
# Get the ASCII (ordinal) value of 'Z'.
LAST_CHAR_CODE = ord("Z")
# Calculate the total number of letters in the alphabet.
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def ceasar_shift(message, shift):
    """
    Encrypts or decrypts a message using the Caesar cipher.
    
    Args:
        message (str): The string to be encrypted or decrypted.
        shift (int): The number of positions to shift each letter.
                     Positive for encryption, negative for decryption.
    """
    result = ""
    # Loop through each character in the message, converting it to uppercase.
    for char in message.upper():
        # Check if the character is a letter of the alphabet.
        if char.isalpha():
            # Get the ASCII code of the current character.
            char_code = ord(char)
            # Use the modulo operator to normalize the shift.
            # This ensures the shift is always within the range of the alphabet (0-25),
            # which correctly handles large shifts (e.g., 27 is the same as 1).
            normalized_shift = shift % CHAR_RANGE
            
            # Apply the shift to the character's ASCII code.
            new_char_code = char_code + normalized_shift
            
            # --- Handle the "wrap-around" logic for the alphabet ---
            # If the new code goes past 'Z', wrap it back to the beginning of the alphabet.
            if new_char_code > LAST_CHAR_CODE:
                new_char_code = FIRST_CHAR_CODE + (new_char_code - LAST_CHAR_CODE - 1) % CHAR_RANGE
            # If the new code goes before 'A', wrap it back to the end of the alphabet.
            elif new_char_code < FIRST_CHAR_CODE:
                new_char_code = LAST_CHAR_CODE - (FIRST_CHAR_CODE - new_char_code - 1) % CHAR_RANGE


            # Convert the new ASCII code back to a character and add it to the result.
            result += chr(new_char_code)
        else:
            # If the character is not a letter, add it to the result unchanged.
            result += char
    print(result)

# --- Main program execution ---
# Prompt the user for a message and a shift key.
user_message = input("Message to Encryp: ")
user_shift_key = int(input("Shift Key (integer): "))

# Call the function with the user's input.
ceasar_shift(user_message, user_shift_key)
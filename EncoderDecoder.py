# EncoderDecoder.py
# Billy Ridgeway
# Encode or decode your messages by shifting the ASCII characters.

message = input("Enter a message to encode or decode: ")    # Prompt the user for a message to encode/decode.
message = message.upper()                                   # Convert the string of letters to upper case.
output = ""                                                 # Sets output to an empty string.
for letter in message:                                      # A loop to convert each letter in the message.
    if letter.isupper():                                    # Checks to see if the letter is already in upper case.
        value = ord(letter) + 13                            # Converts the letter to it's corresponding ASCII number.
        letter = chr(value)                                 # Converts an ASCII number to a letter.
        if not letter.isupper():                            # This loop runs to ensure that the ASCII number hasn't shifted too far and gone past 'Z'.
            value -= 26                                     # This subtracts 26 from the number to ensure it's in the range from 'A' to 'Z'.
            letter = chr(value)                             # Converts the ASCII value to a letter.
    output += letter                                        # Add the letter to the output string.
print("Output message: ", output)                           # Prints the encoded/decoded message to the screen.

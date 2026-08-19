import string

alphabet = list(string.ascii_lowercase)

def caesar(text, shift, direction):
    """
    Encrypts or decrypts a message using the Caesar Cipher.
    """
    output_text = ""
    shift = shift % 26
    
    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            current_position = alphabet.index(char)
            new_position = (current_position + shift) % 26
            output_text += alphabet[new_position]
        else:
            output_text += char
            
    print(f"Here's the {direction}d result: {output_text}\n")


def main():
    should_continue = True
    
    print("--- CAESAR CIPHER ENCRYPTION/DECRYPTION ---")
    
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ["encode", "decode"]:
            print("Invalid input. Please choose 'encode' or 'decode'.")
            continue
            
        text = input("Type your message:\n").lower()
        
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Please enter a valid integer for the shift number.")
            continue

        caesar(text=text, shift=shift, direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
        if restart != "yes":
            should_continue = False
            print("Goodbye!")

if __name__ == "__main__":
    main()
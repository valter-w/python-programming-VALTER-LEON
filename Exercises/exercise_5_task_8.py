"""
Every iteration lets user choose to:
1. Encrypt a message
2. Decrypt a message
3. Exit the program
"""
while True:
    action = None
    while action == None:
        print("What would you like to do?")
        print("1) Encrypt a message")
        print("2) Decrypt a message")
        print("3) Exit")

        action_code = input("Choose an option: ")
        action_code = action_code.strip()
        action_code = action_code.lower()
        # e.g. if user enters "1)", change to "1":
        action_code = action_code.replace(")", "")

        if action_code == "1":
            action = "encrypt"
        elif action_code == "2":
            action = "decrypt"
        elif action_code in ["3", "q", "quit"]:
            action = "exit"
        else:
            print("Invalid response. Try again.", end="\n\n")

    lower_swe_alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    upper_swe_alphabet = lower_swe_alphabet.upper()

    if action == "exit":
        break
    elif action == "encrypt":
        original_msg = input("\nEnter a message to encrypt:\n")
        encrypted_msg = ""
        for char in original_msg:

            if char in lower_swe_alphabet:
                char_index = lower_swe_alphabet.find(char)
                char_index += 1
                # if char is "ö" (last letter), decrypt to "a" (first letter)
                if char_index == len(lower_swe_alphabet):
                    char_index = 0
                encrypted_char = lower_swe_alphabet[char_index]
                encrypted_msg += encrypted_char
            elif char in upper_swe_alphabet:
                char_index = upper_swe_alphabet.find(char)
                char_index += 1
                if char_index == len(upper_swe_alphabet):
                    char_index = 0
                encrypted_char = upper_swe_alphabet[char_index]
                encrypted_msg += encrypted_char
            # non-Swedish-alphabetic chars are left unaltered:
            else:
                encrypted_msg += char
        print("\nEncrypted message:")
        print(encrypted_msg, end="\n\n")
    else:
        encrypted_msg = input("\nEnter a message to decrypt:\n")
        decrypted_msg = ""
        for char in encrypted_msg:
            if char in lower_swe_alphabet:
                char_index = lower_swe_alphabet.find(char)
                char_index -= 1
                # if char is "a" (first letter), decrypt to "ö" (lasst letter)
                if char_index == -1:
                    char_index = len(lower_swe_alphabet) - 1
                decrypted_char = lower_swe_alphabet[char_index]
                decrypted_msg += decrypted_char
            elif char in upper_swe_alphabet:
                char_index = upper_swe_alphabet.find(char)
                char_index -= 1
                if char_index == -1:
                    char_index = len(upper_swe_alphabet) - 1
                decrypted_char = upper_swe_alphabet[char_index]
                decrypted_msg += decrypted_char
            # non-Swedish-alphabetic chars are left unaltered:
            else:
                decrypted_msg += char
        print("\nDecrypted message:")
        print(decrypted_msg, end="\n\n")
import base64

#Introduction method
def introduction_print():
    print("_________________________________________________________________________________________________________________")
    print()
    print("Welcome to my Xor encryption CTF presentation!")
    print()
    print("What does Xor(Exclusive or) entail?:")
    print("    One or the other must be true, but both cannot be true")
    print()
    print("How does Xor encryption work?:")
    print("    Xor encryption work by using the exclusive or method to compare every bit in a plain text messsage with the ")
    print("    provided key. The output generated is displayed in the form of cypher text.")
    print()
    print("Now that you understand the basics, lets try to encrypt your own message!")
    print()
    print("_________________________________________________________________________________________________________________")

# method for encryption
def xor_encrypt_text(sentence,key):
    empty_string_text = ""

    for i in range(len(sentence)):
        empty_string_text += chr(ord(sentence[i]) ^ ord(key[i%len(key)]))
    
    return base64.b64encode(empty_string_text.encode('latin1')).decode('utf-8') #since the special characters cant be printed, convert to base64 in order to display in terminal

#method for decryption
def xor_decrypt_text(encrypted_sentence, key):
    
    #since the special characters were converted to base64, convert back to the given special characters
    reverted_sentence = base64.b64decode(encrypted_sentence)

    decrypted_empty_string_text = ""

    for i in range(len(reverted_sentence)):
        decrypted_empty_string_text += chr(reverted_sentence[i] ^ ord(key[i % len(key)]))
    
    return decrypted_empty_string_text #since the special characters cant be printed, convert to base64 in order to display in terminal
    



# Introduction to xor encryption

introduction_print()

# Prompt the user for the hidden plain text, and key
selection_ok = False
while selection_ok == False:
    print("Enter your secret sentence below: ")

    user_string = input("Secret sentence: ")
    user_key = input("Secret key: ")

    satisfied = input("Is this Selection ok? (y/n): ")

    if satisfied == "y":
        print("Let's encrypt your sentence!")
        print()
        selection_ok = "True"
    else:
        print("Enter your input again")

# Call the encryption method
encrypted_user_sentence = xor_encrypt_text(user_string, user_key)

print("Here is your encrypted sentence! Be sure to keep your key private.")
print()
print(encrypted_user_sentence)
print()
print("_______________________________________________________________________________________")

want_to_decrypt = True;
while want_to_decrypt == True:
    print()
    ready_to_decrypt = input("Are you ready to decrypt? (y/n):  ")
    if ready_to_decrypt == "y":
        #prompt the user for their key
        check_key = input("What is your key?: ")

        if check_key == user_key:
            print("That is correct! Now lets see your decrypted message: ")
            print()
            decrypted_final_text = xor_decrypt_text(encrypted_user_sentence,user_key)
            print(decrypted_final_text)
            want_to_decrypt = False
        else: 
            print("That key isnt right, try again :)")  
            want_to_decrypt = False
        
    #if the user doesnt want to input a key
    else:
        print("You may never know the truth!")
        print()
        want_to_decrypt = True; 













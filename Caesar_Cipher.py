#Caeser Cipher

def encrypt():
    Phrase_Plain = raw_input('Please enter the phrase you would like to encrypt: ')
    print(Phrase_Plain.encode('rot13'))

def decrypt():
    Phrase_Ciphered = raw_input('Please enter the phrase you would like to decrypt: ')
    print(Phrase_Ciphered.decode('rot13'))



if __name__ == "__main__":
    quit = False
    print('This program encrypts and decripts phrases according to a Caeser Cipher')
    while quit == False:
        choice = raw_input('Do you want to (e)ncrypt, (d)ecrypt, or (q)uit?')
        if choice == 'e':
            encrypt()
        elif choice == 'd':
            decrypt()
        elif choice == 'q':
            quit = True
        else:
            print 'The input was not an \'e\', \'d\', or \'q\''

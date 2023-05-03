alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
def caesar(codeword,shift):  
    # initialize ciphertext as blank string
    kwordShift = ""
    # loop through the length of the plaintext
    for i in range(len(codeword)):         
        # get the ith letter from the plaintext
        letter = codeword[i] 
        # find the number position of the ith letter
        num_in_alphabet = alphabet.index(letter) 
        # find the number position of the cipher by adding the shift 
        cipher_num = (num_in_alphabet + shift) % len(alphabet) 
        # find the cipher letter for the cipher number you computed
        cipher_letter = alphabet[cipher_num] 
        # add the cipher letter to the ciphertext
        kwordShift =  kwordShift + cipher_letter 
    # return the computed ciphertext
    return kwordShift

def uncaesar(codeword,shift):
    # initialize plainext as blank string
    kwordShift = ""
    # loop through the length of the plaintext
    for i in range(len(codeword)):         
        letter = codeword[i] 
        num_in_alphabet = alphabet.index(letter) 
        plain_num = (num_in_alphabet - shift) % len(alphabet) 
        plain_letter = alphabet[plain_num] 
        kwordShift = kwordShift + plain_letter 
    return kwordShift

def polyCaesar(plaintext,codeword,shift):
        kwordShift = caesar(codeword,shift)
        ciphertext = ''
        for i in range(len(plaintext)):
                letter = plaintext[i]
                num_in_alphabet = alphabet.index(letter)
 
                # Find the position in the codeword with the letter to shift
                shiftIndex = i % len(kwordShift)
                
                # Find the letter in the codeword to shift
                shiftLetter = kwordShift[shiftIndex]
                
                # Find the number associated with the letter to be used as the shift
                shift = alphabet.index(shiftLetter)
                
                cipher_num = (num_in_alphabet + shift) % len(alphabet)
                cipher_letter = alphabet[cipher_num]
                ciphertext = ciphertext + cipher_letter
        return ciphertext

    
def unPolyCaesar(plaintext,codeword,shift):
        kwordShift = caesar(codeword,shift)
        print(kwordShift)   
        ciphertext = ''
        for i in range(len(plaintext)):
                letter = plaintext[i]
                num_in_alphabet = alphabet.index(letter)
 
                # Find the position in the codeword with the letter to shift
                shiftIndex = i % len(kwordShift)
                
                # Find the letter in the codeword to shift
                shiftLetter = kwordShift[shiftIndex]
                
                # Find the number associated with the letter to be used as the shift
                shift = alphabet.index(shiftLetter)
                
                cipher_num = (num_in_alphabet - shift) % len(alphabet)
                cipher_letter = alphabet[cipher_num]
                ciphertext = ciphertext + cipher_letter
        return ciphertext

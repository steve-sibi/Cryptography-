from string import ascii_lowercase
from string import punctuation
import collections

alphabets = ''.join(list(ascii_lowercase))
monoKey = "hljfrtzyqscnbexvumpaokwdgi" # should converted to user input in gui
length=26

#Should be changed to input in gui
text="one way to solve a encrypted message if we know its language is to find different plaintext of the very same language long enough to fill one sheet or so and then we count the occurrences of each letter we call the most frequently occurring letter the first the next most occurring letter the second the following most occurring letter the third and so on until we account for all different letters in the plaintext sample then we look at the cipher text we want to solve and we also classify its symbols we find the most occurring symbol and change it to the form of the first letter of the plaintext sample the next most common symbol is changed to the form of the second letter and the following most common symbol is changed to the form of the third letter and so on until we account for all symbols of the cryptogram we want to solve"

text = text.lower()

no_punc = ""
for char in text:
    if char not in punctuation and char not in " ":
        no_punc += char


toEncrypt = no_punc

#This function takes in two parameters and returns two values
#     parameter 1 -> Character to perform monoalphabetic substitution
#     parameter 2 -> If the substitution is for encryption or decryption (encrypt=1, decrypt= -1 or any other value)
#     Return value 1 -> Character after substitution
#     Return value 2 -> key/number based on index (value limited between 1-25) 
def monoAlphabeticSubstitution(charToSubstitute, action):
    #Checking if encryption or decryption
    if action==1:   
        indexAlphabets = alphabets.index(charToSubstitute)    #finding the character index in alphabets
        
        #Encrypting the character based on monoalphabetic substitution key
        indexMonoKey = monoKey.index(charToSubstitute)       
        charMonoKey  = monoKey[(indexMonoKey+1)%length]
    else:
        
        #Decrypting character based on monoalphabtic substituion key
        indexMonoKey = monoKey.index(charToSubstitute)
        charMonoKey =  monoKey[(indexMonoKey-1)%length]

        #Finding the index of the decrypted character in the alphabets
        indexAlphabets = alphabets.index(charMonoKey)
    
    value = indexAlphabets%(length-1)+1   #Determining value for key(or number of characters) based on index of plain text. The value is limited between 1-25
    return (charMonoKey,value)


#This function takes in three parameters and returns one value
#     parameter 1 -> Character to perform ceaser cipher substitution
#     parameter 2 -> Key for ceaser cipher
#     parameter 3 -> If the substitution is for encryption or decryption (encrypt=1, decrypt= -1 or any other value)
#     Return value 1 -> Character after substitution
def ceaserCipherSubstitution(charToSubstitute, key, action):
    
    if action != 1:
        key = key*-1    #Converting key to negative number if decryption
    
    currentIndex = alphabets.index(charToSubstitute)
    newIndex = (currentIndex + key) % length
    substitutedChar = alphabets[newIndex]

    return substitutedChar

i = 0
encrypted = ""

#Looping through each character in the text to encrypt
while i < len(toEncrypt):
    
    encryptedChar,key = monoAlphabeticSubstitution(toEncrypt[i],1)
    encrypted += encryptedChar
    
    i += 1 #Increasing counter

    if i < len(toEncrypt):    #Making sure that there are characters left in the plain text
        
        encryptedChar, numCharToEncrypt = monoAlphabeticSubstitution(toEncrypt[i],1)
        encrypted+=encryptedChar
        i += 1

        # Encrypting the required number of characters
        for x in range(numCharToEncrypt):
            if i < len(toEncrypt):    #making sure that there are charcaters to encrypt

                encryptedChar = ceaserCipherSubstitution(toEncrypt[i], key, 1)
                encrypted += encryptedChar

                i += 1    #Increasing counter
            else:
                break

print(encrypted)

toDecrypt = encrypted


i = 0
decrypted=""

#Looping through each character in the text to decrypt
while i < len(toDecrypt):

    decryptedChar, key = monoAlphabeticSubstitution(toDecrypt[i],-1)    #finding key and decrypted character
    decrypted += decryptedChar    #adding decrypted character to decrypted text

    i += 1 #Updating counter
  
    if i < len(toEncrypt):    #Making sure that there are characters left to encrypt

        decryptedChar, numCharToDecrypt = monoAlphabeticSubstitution(toDecrypt[i],-1)   #finding number of characters to decrypt and decrypted character
        decrypted += decryptedChar 
        i += 1 #updating counter

        # decrypting the required number of characters
        for x in range(numCharToDecrypt):
            if i < len(toDecrypt):
                #Finding decrypted character and adding it to the decrypted text
                decryptedChar = ceaserCipherSubstitution(toDecrypt[i], key, -1) 
                decrypted += decryptedChar

                i += 1
            else:
                break

print(decrypted)

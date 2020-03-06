from string import ascii_lowercase
from string import punctuation
from tkinter import *
from string import ascii_letters, digits    # includes uppercase letters as well
import random

alphabets = ''.join(list(ascii_lowercase))
monoKey = "hljfrtzyqscnbexvumpaokwdgi" # should converted to user input in gui
length=26

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

def ceaserCipherSubstitution(charToSubstitute, key, action):

        if action != 1:
            key = key*-1    #Converting key to negative number if decryption

        currentIndex = alphabets.index(charToSubstitute)
        newIndex = (currentIndex + key) % length
        substitutedChar = alphabets[newIndex]

        return substitutedChar

def encrypt():
    text = entryPlainText.get()
    text = text.lower()

    no_punc = ""
    for char in text:
        if char not in punctuation and char not in " ":
            no_punc += char


    toEncrypt = no_punc

    i = 0
    encrypted = ""

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
    var.set(encrypted)
    return toEncrypt

def decrypt():
    toEncrypt = encrypt()
    toDecrypt = entryCyphertext.get()
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
    var2.set(decrypted)

# Gui Creation
root = Tk()
root.title("Decryption & Encryption Tool")
topFrame = Frame(root)
topFrame.pack(fill=X,padx=10,pady=10)

labelTitle = Label(topFrame, text="Project 1 Decryption and Encryption Tool")
labelSubTitle = Label(topFrame, text="Created By: Group 3")

labelTitle.pack(fill=X)
labelSubTitle.pack()


secondFrame = Frame(root)
secondFrame.pack(pady=5,padx=5)

labelKey = Label(secondFrame,text="Key: ")
# labelShift = Label(secondFrame, text="Shift: ")
# varShift = StringVar()
messageKey = Label(secondFrame, text=monoKey)
# messageShit = Message(secondFrame, textvariable=varShift)

labelKey.grid(row=0, sticky=E)
messageKey.grid(row=0, column=1)
# labelShift.grid(row=1, sticky=E)
# messageShit.grid(row=1, column=1)

leftFrame = Frame(root)
leftFrame.pack(side=LEFT, ipadx=5, ipady=5)

labelPlaintext = Label(leftFrame, text="Message to Encrypt: ")
entryPlainText = Entry(leftFrame)
buttonEncrypt = Button(leftFrame, text="Encrypt", command=encrypt)
var = StringVar()
labelCypherTextConverted = Label(leftFrame, text="Encrypted Message: ")
labelViewCypher = Message(leftFrame, textvariable=var)

labelPlaintext.grid(row=0, sticky=E)
entryPlainText.grid(row=0, column=1)
labelCypherTextConverted.grid(row=1, sticky=E)
labelViewCypher.grid(row=1, column=1)
buttonEncrypt.grid(columnspan=2)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, ipadx=5, ipady=5)

labelCyphertext = Label(rightFrame, text="Message to Decrypt: ")
entryCyphertext = Entry(rightFrame)
buttonDecrypt = Button(rightFrame, text="Decrypt", command=decrypt)
var2 = StringVar()
labelPlainTextConverted = Label(rightFrame, text="Decrypted Cypher: ")
labelViewPlainText = Message(rightFrame, textvariable=var2)

labelCyphertext.grid(row=0, sticky=E)
entryCyphertext.grid(row=0, column=1)
labelPlainTextConverted.grid(row=1, sticky=E)
labelViewPlainText.grid(row=1, column=1)
buttonDecrypt.grid(columnspan=2)


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

labelConsole = Label(bottomFrame, text="Console:")
labelConsole.pack()

root.mainloop()

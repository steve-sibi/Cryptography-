import tkinter as tk
from tkinter import *
from string import ascii_lowercase
from string import punctuation
import collections

alphabets = ''.join(list(ascii_lowercase))
# monoKey = "hljfrtzyqscnbexvumpaokwdgi"  # should be input
length = 26
monoKey = ""        #User entered key will be stored here

# text="ya test test hi test test hi test test hi test test"
# text = "one way to solve an encrypted message if we know its language is to find a different plaintext of the same language long enough to fill one sheet or so and then we count the occurrences of each letter we call the most frequently occurring letter the first the next most occurring letter the second the following most occurring letter the third and so on until we account for all the different letters in the plaintext sample then we look at the cipher text we want to solve and we also classify its symbols we find the most occurring symbol and change it to the form of the first letter of the plaintext sample the next most common symbol is changed to the form of the second letter and the following most common symbol is changed to the form of the third letter and so on until we account for all symbols of the cryptogram we want to solve"
# text="the european languages are members of the same family their separate existence is a myth for science music sport etc europe uses the same vocabulary the languages only differ in their grammar their pronunciation and their most common words everyone realizes why a new common language would be desirable one could refuse to pay expensive translators to achieve this it would be necessary to have uniform grammar pronunciation and more common words if several languages coalesce the grammar of the resulting language is more simple and regular than that of the individual languages the new common language will be more simple and regular than the existing european languages it will be as simple as occidental in fact it will be occidental to an english person it will seem like simplified english as a skeptical cambridge friend of mine told me what occidental is the european languages are members of the same family their separate existence is a myth for science music sport etc europe uses the same vocabulary the languages only differ in their grammar their pronunciation and their most common words everyone realizes why a new common language would be desirable one could refuse to pay expensive translators to achieve this it would be necessary to have uniform grammar pronunciation and more common words if several languages coalesce the grammar of the resulting language is more simple and regular than that of the individual languages the new common language will be more simple and regular than the existing european languages it will be as simple as occidental in fact it will be occidental to an english person it will seem like simplified english as a skeptical cambridge friend of mine told me what occidental is the european languages are members of the same family their separate existence is a myth for science music sport etc europe uses the same vocabulary the languages only differ in their grammar their pronunciation and their most common words"

def setMonokey():
    global monoKey
    monoKey = key_input.get()

def display_encrypt():
    result_entry.insert("1.0", encryptionFunc())

def display_decrypt():
    result_entry.insert("1.0", decryptionFunc())

def clear_input():
    text_cipher_entry.delete(1.0, END)
    result_entry.delete(1.0, END)

# This function takes in two parameters and returns two values
#     parameter 1 -> Character to perform monoalphabetic substitution
#     parameter 2 -> If the substitution is for encryption or decryption (encrypt=1, decrypt= -1 or any other value)
#     Return value 1 -> Character after substitution
#     Return value 2 -> key/number based on index (value limited between 1-25)
def monoAlphabeticSubstitution(charToSubstitute, action):

    # Checking if encryption or decryption
    if action == 1:
        # finding the character index in alphabets
        indexAlphabets = alphabets.index(charToSubstitute)
        # Encrypting the character based on monoalphabetic substitution key
        indexMonoKey = monoKey.index(charToSubstitute)
        charMonoKey = monoKey[(indexMonoKey + 1) % length]
    else:
        # Decrypting character based on monoalphabtic substituion key
        indexMonoKey = monoKey.index(charToSubstitute)
        charMonoKey = monoKey[(indexMonoKey - 1) % length]
        # Finding the index of the decrypted character in the alphabets
        indexAlphabets = alphabets.index(charMonoKey)
    value = indexAlphabets % (
            length - 1) + 1  # Determining value for key(or number of characters) based on index of plain text. The value is limited between 1-25
    return (charMonoKey, value)

# This function takes in three parameters and returns one value
#     parameter 1 -> Character to perform ceaser cipher substitution
#     parameter 2 -> Key for ceaser cipher
#     parameter 3 -> If the substitution is for encryption or decryption (encrypt=1, decrypt= -1 or any other value)
#     Return value 1 -> Character after substitution
def ceaserCipherSubstitution(charToSubstitute, key, action):
    if action != 1:
        key = key * -1  # Converting key to negative number if decryption

    currentIndex = alphabets.index(charToSubstitute)
    newIndex = (currentIndex + key) % length
    substitutedChar = alphabets[newIndex]

    return substitutedChar

def encryptionFunc():

    setMonokey()        #Calls funtion to set monokey

    text = text_cipher_entry.get('1.0', 'end-1c')
    text = text.lower()
    no_punc = ""
    for char in text:
        if char not in punctuation and char not in " ":
            no_punc += char
    toEncrypt = no_punc
    i = 0
    encrypted = ""
    # Looping through each character in the text to encrypt
    while i < len(toEncrypt):
        encryptedChar, key = monoAlphabeticSubstitution(toEncrypt[i], 1)
        encrypted += encryptedChar
        i += 1  # Increasing counter
        if i < len(toEncrypt):  # Making sure that there are characters left in the plain text
            encryptedChar, numCharToEncrypt = monoAlphabeticSubstitution(
                toEncrypt[i], 1)
            encrypted += encryptedChar
            i += 1
            # Encrypting the required number of characters
            for x in range(numCharToEncrypt):
                if i < len(toEncrypt):  # making sure that there are charcaters to encrypt
                    encryptedChar = ceaserCipherSubstitution(
                        toEncrypt[i], key, 1)
                    encrypted += encryptedChar
                    i += 1  # Increasing counter
                else:
                    break
    return encrypted

def decryptionFunc():

    setMonokey()        #Calls function to set monokey

    toDecrypt = text_cipher_entry.get('1.0', 'end-1c')
    i = 0
    decrypted = ""
    # Looping through each character in the text to decrypt
    while i < len(toDecrypt):
        decryptedChar, key = monoAlphabeticSubstitution(
            toDecrypt[i], -1)  # finding key and decrypted character
        decrypted += decryptedChar  # adding decrypted character to decrypted text
        i += 1  # Updating counter
        if i < len(toDecrypt):  # Making sure that there are characters left to encrypt
            # finding number of characters to decrypt and decrypted character
            decryptedChar, numCharToDecrypt = monoAlphabeticSubstitution(
                toDecrypt[i], -1)
            decrypted += decryptedChar
            i += 1  # updating counter
            # decrypting the required number of characters
            for x in range(numCharToDecrypt):
                if i < len(toDecrypt):
                    # Finding decrypted character and adding it to the decrypted text
                    decryptedChar = ceaserCipherSubstitution(
                        toDecrypt[i], key, -1)
                    decrypted += decryptedChar
                    i += 1
                else:
                    break
    return decrypted

##########################################################################
# start of GUI
##########################################################################
root = tk.Tk()  # root window
root.title("Project 1 - Cryptography")  # title for GUI window

root.geometry("1350x780")
root.config(bg="grey")  # background color

##########################################################################
# All frames used
##########################################################################

title_frame = Frame(root)
title_frame.pack(side=TOP, pady=10)

key_frame = Frame(root)
key_frame.pack(pady=10)

bottomFrame = Frame(root)
bottomFrame.pack(padx=10, pady=10)

bottomFrame0 = Frame(bottomFrame)
bottomFrame0.pack(side=LEFT, padx=10, pady=20)

bottomFrame1 = Frame(bottomFrame)
bottomFrame1.pack(side=LEFT, padx=10)

button_frame = Frame(bottomFrame0)
button_frame.pack(side=BOTTOM)

button_frame1 = Frame(root, bg="grey")
button_frame1.pack()
##########################################################################

title_label = Label(title_frame, text="Project 1 GUI")
title_label.pack(fill=X, pady=10)

##########################################################################
# Key insert frame of GUI
##########################################################################
key_label = Label(key_frame, text="Key:")
key_label.pack(side=LEFT, fill=Y, pady=5)

key_input = Entry(key_frame, width=60)
key_input.pack(side=LEFT, fill=Y, pady=10, padx=20)

display_text = tk.StringVar()
current_key = Label(key_frame, textvariable=display_text)
current_key.pack(side=RIGHT)
##########################################################################

##########################################################################
# Plaintext / Cipher input frame of GUI
##########################################################################
text_cipher_label = Label(bottomFrame0, text="Enter Text to Encrypt or Decrypt")
text_cipher_label.pack(pady=10)

text_cipher_entry = Text(bottomFrame0, height=28)
text_cipher_entry.pack(padx=10)

encrypt_button = Button(button_frame, text="Encrypt", command=display_encrypt)
encrypt_button.pack(side=RIGHT, padx=5, pady=5)

decrypt_button = Button(button_frame, text="Decrypt", command=display_decrypt)
decrypt_button.pack(side=LEFT, pady=10)
##########################################################################

##########################################################################
# Result portion of GUI
##########################################################################
result_label = Label(bottomFrame1, text="Result")
result_label.pack(pady=5)

result_entry = Text(bottomFrame1, height=30)
result_entry.pack(padx=10, pady=10)

clear_button = Button(button_frame1, text="Clear All", command=clear_input)
clear_button.pack(pady=10)

root.mainloop()

# end of GUI
##########################################################################

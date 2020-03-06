from string import ascii_lowercase
import collections
import operator

# This function takes in three parameters and returns one value
#   parameter 1 -> Character to perform ceaser cipher substitution
#   parameter 2 -> Key for ceaser cipher
#   parameter 3 -> If the substitution is for encryption or decryption (encrypt=1, decrypt= -1 or any other value)
#   Return value 1 -> Character after substitution
def ceaserCipherSubstitution(charToSubstitute, key, action):
    if action != 1:
        key = key * -1  # Converting key to negative number if decryption

    # Using current index to find new index based on key
    currentIndex = alphabets.index(charToSubstitute)
    newIndex = (currentIndex + key) % length

    # Substituting character based on new index
    substitutedChar = alphabets[newIndex]

    return substitutedChar

# This function takes in three parameters and returns one value
#   parameter 1 -> String to decode
#   parameter 2 -> shift to be used as key for ceaser cipher
#   parameter 3 -> number of characters to decode
#   Return value 1 -> Text after decoding
def decode(toDecode, shift, number):
    # Adding first two characters in decoded text based on shift and number
    decodedText = alphabets[shift - 1]
    decodedText += alphabets[number - 1]

    # Assigning end based on number, making sure it is between the values 3-27
    end = ((number - 1) % 25) + 3

    # Decoding rest of characters based by using ceaser shift
    for i in range(2, end):
        decodedText += ceaserCipherSubstitution(toDecode[i], shift, -1)
    return decodedText


length = 26

alphabets = ''.join(list(ascii_lowercase))

sample = ""  # Each sub text will be stored here


decodeMappings = {}
frequencyTable = list("etaoinsrhdlucmfywgpbvkxqjz")
# Sample input for encrpted text :
# kbtlpnidhdaktptcntbswhgphvvdjhlizhnqkdxihapcvjpvtxhiduxcssxuuxtjsyuqfnsyjcytkymjaxtdxfrjqfslzfljqtsljbkiuvhctwzzcbsgvsxztwxtfsiymjsbjhtzsyymxkhhzwwjshjxtkjfhljmbbmzemkittblxuwabntximwfljqaoogdduzsxqffqdftqrudefftxbjcyrtxythhzwwnbizshhsfhlxamkwvgzlijsppsamrkqswxsggyvthfydwllwjllxbpqzlobetppovoujmxfbdnkxqwirudoogliihuxbyqjyyjwxnsymjujoubzslhgoadzshvsbkszccyozzbywcjbylnyrnqyquhnnickeoxtgwpxtelhvetccbyrbmllrfuhelpxybgwzlygimniwwmtmdibnthwjgviyxcvibxhyytymjktwpksgursvefgyrggrekriwteaphbcngcbjvyuncqnwxvyrtxyhtrrtsxdrgtqnxhmfslxgytymxrtwrtkylxamkwvgjixxiverhxlijkjadlxcvbdhirdppbaflzobyvfpunbisrhchvsrkxsulznkznoxjrkzzxluhxmkkcjcixaltprrdjcirkxgrryeshuryulznxnwduzkalugqyquhnnimifux
encrypted = input("Please enter encrypted text to attempt decode : ")

start = 0
previous = ""  # Variable for storing text decoded in the previous attempt of each decode
decoded = ""

valuesLeft = []  # Stores the values that is left for decryption
for i in range(1, 27):
    valuesLeft.append(i)  # Adding values from 1-26 to the values left array

# Try block to avoid end conditions where there are not enough characters
try:
    while start < len(encrypted):
        # Checking if the first and second characters exhist in the decode mappings
        if encrypted[start] in decodeMappings and encrypted[start + 1] in decodeMappings:

            # Determining shift and number of characters to decode from the first two character in the subset
            shift = decodeMappings[encrypted[start]]
            number = decodeMappings[encrypted[start + 1]]
            toDecode = encrypted[start:start + number + 2]  # Creating the subset with the desired number of characters

            # Decoding the subset and adding it to the decoded.
            decodeAttempt = decode(toDecode, shift, number)
            decoded += decodeAttempt
            previous = decodeAttempt

            print("Current Decoded:",decoded)
            print("--------------")
            start = start + number + 2  # Updating starting point
        else:
            # Checking if number of character is in decode mappings
            if encrypted[start + 1] not in decodeMappings:
                end = start + 27
            else:
                end = start + decodeMappings[encrypted[start + 1]] + 2  # Assigning end as the longest

            toDecode = encrypted[start:end]
            frequencies = collections.Counter(toDecode[2:])  # Finding frequencies of characters in the sub collection

            # Finding the highest repeating character in the subcollection
            highChar = max(frequencies.items(), key=operator.itemgetter(1))[0]

            # Going over the frequency table to list to find the best shift
            for frequencyEntry in frequencyTable:

                decodedAttemptsDict = {}  # Stores the decoded attempts as values with index as key

                if encrypted[start] in decodeMappings:
                    shift = decodeMappings[toDecode[0]]  # Assigning shift from decode mappings
                else:
                    # Assigning shift based on frequency
                    shift = (alphabets.index(highChar) - alphabets.index(frequencyEntry)) % 26
                    if shift not in valuesLeft:
                        continue        # if shift already mapped, move on to next shift attempt

                if encrypted[start + 1] in decodeMappings:
                    number = decodeMappings[toDecode[1]]    # Assigning number of characters from decode mappings

                    # Attempting a decode map and storing it in a dictionary
                    decodeAttempt = decode(toDecode, shift, number)
                    decodedAttemptsDict[number] = decodeAttempt

                    print(number, previous, decodeAttempt)
                else:
                    # Decoding based on all the possible values of number for given shift and adding each to a
                    # dictionary
                    for i in valuesLeft:
                        number = i
                        decodeAttempt = decode(toDecode, shift, number)
                        decodedAttemptsDict[i] = decodeAttempt
                        print(number, previous, decodeAttempt)

                print("--------------")
                choice = int(input("Select a decoding -1 to check next : "))
                print("--------------")

                # If choice is not -1, adding it to the decoded and storing mappings in a dictionary
                if choice != -1:
                    # Storing decode mappings of shift and choice
                    decodeMappings[toDecode[0]] = shift
                    decodeMappings[toDecode[1]] = choice

                    # Adding selected decodedAttempt to the decoded text
                    decoded += decodedAttemptsDict[choice]
                    previous = decodedAttemptsDict[choice]

                    # Removing shift and number from the values left to find
                    if choice in valuesLeft:
                        valuesLeft.remove(choice)
                    if shift in valuesLeft:
                        valuesLeft.remove(shift)

                    print("Current Decoded:",decoded)
                    print("--------------")

                    start = start + choice + 2      # Updating starting point
                    break       # Moving to the next subset
except:
    print("There was a issue")
finally:
    print("The decode text is :", decoded)      # Printing the decode text
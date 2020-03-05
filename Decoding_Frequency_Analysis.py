from string import ascii_lowercase
import collections
import operator


def ceaserCipherSubstitution(charToSubstitute, key, action):
    if action != 1:
        key = key * -1  # Converting key to negative number if decryption

    currentIndex = alphabets.index(charToSubstitute)
    newIndex = (currentIndex + key) % length
    substitutedChar = alphabets[newIndex]

    return substitutedChar


def decode(toDecode, shift, number):
    decodedText = alphabets[shift - 1]
    decodedText += alphabets[number - 1]
    end = ((number - 1) % 25) + 3
    for i in range(2, end):
        decodedText += ceaserCipherSubstitution(toDecode[i], shift, -1)
    return decodedText


length = 26

alphabets = ''.join(list(ascii_lowercase))

sample = ""  # Each sub text will be stored here
count = 0  # Simple counter to keep track of number of subset and subset position

decodeMappings = {}
frequencyTable = list("etaoinsrhdlucmfywgpbvkxqjz")
encrypted = "kbtlpnidhdaktptcntbswhgphvvdjhlizhnqkdxihapcvjpvtxhiduxcssxuuxtjsyuqfnsyjcytkymjaxtdxfrjqfslzfljqtsljbkiuvhctwzzcbsgvsxztwxtfsiymjsbjhtzsyymxkhhzwwjshjxtkjfhljmbbmzemkittblxuwabntximwfljqaoogdduzsxqffqdftqrudefftxbjcyrtxythhzwwnbizshhsfhlxamkwvgzlijsppsamrkqswxsggyvthfydwllwjllxbpqzlobetppovoujmxfbdnkxqwirudoogliihuxbyqjyyjwxnsymjujoubzslhgoadzshvsbkszccyozzbywcjbylnyrnqyquhnnickeoxtgwpxtelhvetccbyrbmllrfuhelpxybgwzlygimniwwmtmdibnthwjgviyxcvibxhyytymjktwpksgursvefgyrggrekriwteaphbcngcbjvyuncqnwxvyrtxyhtrrtsxdrgtqnxhmfslxgytymxrtwrtkylxamkwvgjixxiverhxlijkjadlxcvbdhirdppbaflzobyvfpunbisrhchvsrkxsulznkznoxjrkzzxluhxmkkcjcixaltprrdjcirkxgrryeshuryulznxnwduzkalugqyquhnnimifux"

start = 0
previous = ""  # Variable for storing text decoded in the previous attempt of each decode
decoded = ""

valuesLeft = []     #Stores the values that is left for decryption
for i in range(1, 27):
    valuesLeft.append(i)    #Adding values from 1-26 to the values left array


while start < len(encrypted):

    #Checking if the first and second characters exhist in the decode mappings
    if encrypted[start] in decodeMappings and encrypted[start + 1] in decodeMappings:

        #Determining shift and number of characters to decode from the first two character in the subset
        shift = decodeMappings[encrypted[start]]
        number = decodeMappings[encrypted[start + 1]]
        toDecode = encrypted[start:start + number + 2]  #Creating the subset with the desired number of characters

        #Decoding the subset and adding it to the decoded. 
        decodeAttempt = decode(toDecode, shift, number)
        decoded += decodeAttempt
        previous = decodeAttempt        

        print(decoded)
        start = start + number + 2      #Updating starting point
    else:
        #Checking if number of character is in decode mappings
        if encrypted[start + 1] not in decodeMappings:
            end = start + 27
        else:
            end = start + decodeMappings[encrypted[start + 1]] + 2      #Assigning end as the longest

        
        toDecode = encrypted[start:end]
        frequencies = collections.Counter(toDecode[2:])     #Finding frequencies of characters in the sub collection

        highChar = max(frequencies.items(), key=operator.itemgetter(1))[0]      #Finding the highest repeating character in the subcollection
        for frequencyEntry in frequencyTable:

            decodedAttemptsDict = {}        #Stores the decoded attempts as values with index as key

            if encrypted[start] in decodeMappings:
                shift = decodeMappings[toDecode[0]]     #Assigning shift from decode mappings
            else:
                shift = (alphabets.index(highChar) - alphabets.index(frequencyEntry)) % 26
                if shift not in valuesLeft:
                    continue

            if encrypted[start + 1] in decodeMappings:
                number = decodeMappings[toDecode[1]]

                decodeAttempt = decode(toDecode, shift, number)
                decodedAttemptsDict[number] = decodeAttempt

                print(number, previous, decodeAttempt)
            else:
                for i in valuesLeft:
                    number = i
                    decodeAttempt = decode(toDecode, shift, number)
                    decodedAttemptsDict[i] = decodeAttempt
                    print(number, previous, decodeAttempt)

            print("--------------")
            choice = int(input("Select a decoding -1 to check next : "))

            if choice != -1:
                decodeMappings[toDecode[0]] = shift
                decodeMappings[toDecode[1]] = choice
                decoded += decodedAttemptsDict[choice]
                previous = decodedAttemptsDict[choice]
                if choice in valuesLeft:
                    valuesLeft.remove(choice)
                if shift in valuesLeft:
                    valuesLeft.remove(shift)
                print(decoded)
                start = start + choice + 2
                count = 0
                break

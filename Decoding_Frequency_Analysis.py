# Initializing variables
# toDecode = encrypted[0:27]
from string import ascii_lowercase
from string import punctuation
import collections
import operator


def ceaserCipherSubstitution(charToSubstitute, key, action):
    if action != 1:
        key = key * -1  # Converting key to negative number if decryption

    currentIndex = alphabets.index(charToSubstitute)
    newIndex = (currentIndex + key) % length
    substitutedChar = alphabets[newIndex]

    return substitutedChar


length = 26

alphabets = ''.join(list(ascii_lowercase))

sample = ""  # Each sub text will be stored here
count = 0  # Simple counter to keep track of number of subset and subset position

decodeMappings = {}
frequencyTable = list("etaoinsrhdlucmfywgpbvkxqjz")
encrypted = "kbtlpnidhdaktptcntbswhgphvvdjhlizhnqkdxihapcvjpvtxhiduxcssxuuxtjsyuqfnsyjcytkymjaxtdxfrjqfslzfljqtsljbkiuvhctwzzcbsgvsxztwxtfsiymjsbjhtzsyymxkhhzwwjshjxtkjfhljmbbmzemkittblxuwabntximwfljqaoogdduzsxqffqdftqrudefftxbjcyrtxythhzwwnbizshhsfhlxamkwvgzlijsppsamrkqswxsggyvthfydwllwjllxbpqzlobetppovoujmxfbdnkxqwirudoogliihuxbyqjyyjwxnsymjujoubzslhgoadzshvsbkszccyozzbywcjbylnyrnqyquhnnickeoxtgwpxtelhvetccbyrbmllrfuhelpxybgwzlygimniwwmtmdibnthwjgviyxcvibxhyytymjktwpksgursvefgyrggrekriwteaphbcngcbjvyuncqnwxvyrtxyhtrrtsxdrgtqnxhmfslxgytymxrtwrtkylxamkwvgjixxiverhxlijkjadlxcvbdhirdppbaflzobyvfpunbisrhchvsrkxsulznkznoxjrkzzxluhxmkkcjcixaltprrdjcirkxgrryeshuryulznxnwduzkalugqyquhnnimifux"
# print (alphabets.index("n")%25)
# count = 0
start = 0
previous = ""
decoded = ""

valuesLeft = []
for i in range(1, 27):
    valuesLeft.append(i)

while start < len(encrypted):
    if encrypted[start + 1] not in decodeMappings:
        end = start + 27
        #print("encrypted[start+1] not in decodeMappings")
    else:
        end = start + decodeMappings[encrypted[start + 1]] + 2
        print(start, end, encrypted[start + 1])

    if encrypted[start] in decodeMappings and encrypted[start + 1] in decodeMappings:
        #print("Seeeeee", decodeMappings[encrypted[start]])
        shift = decodeMappings[encrypted[start]]
        number = decodeMappings[encrypted[start + 1]]
        decodeAttempt = alphabets[shift - 1]
        decodeAttempt += alphabets[number - 1]
        for char in encrypted[start + 2:start + number + 2]:
            decodeAttempt += ceaserCipherSubstitution(char, shift, -1)
        previous = decodeAttempt
        decoded += decodeAttempt
        print(decoded)
        start = start + decodeMappings[encrypted[start + 1]] + 2
    else:
        toDecode = encrypted[start:end]
        frequencies = collections.Counter(toDecode[2:])
        #print(toDecode)
        # for key in collections.OrderedDict(sorted(frequencies.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)):

        # stats = {'a': 1000, 'b': 3000, 'c': 100}
        highChar = max(frequencies.items(), key=operator.itemgetter(1))[0]
        for count in range(26):
            if encrypted[start] in decodeMappings:
                shift = decodeMappings[encrypted[start]]
                #chosenShiftChar=""
            else:
                #chosenShiftChar = frequencyTable[count]
                #while
                shift = (alphabets.index(highChar) - alphabets.index(frequencyTable[count])) % 26
            decodedAttemptsDict = {}
            if (end - start - 2) != 25:
                decodeAttempt = alphabets[shift - 1]
                index = decodeMappings[toDecode[1]]
                decodeAttempt += alphabets[index - 1]
                for char in toDecode[2:index + 3]:
                    decodeAttempt += ceaserCipherSubstitution(char, shift, -1)
                print(index, previous, decodeAttempt)
                decodedAttemptsDict[index] = decodeAttempt
                # decodedList.append(decodeAttempt)
            else:
                for i in range(1, 27):
                    if i in valuesLeft:
                        decodeAttempt = alphabets[shift - 1]
                        decodeAttempt += alphabets[i - 1]
                        for char in toDecode[2:((i - 1) % 25) + 3]:
                            decodeAttempt += ceaserCipherSubstitution(char, shift, -1)
                        print(i, previous, decodeAttempt)
                        decodedAttemptsDict[i] = decodeAttempt
                        # decodedList.append(decodeAttempt)
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
                print(decodeMappings)
                start = start + choice + 2
                count = 0
                break

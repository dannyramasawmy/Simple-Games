
import random as rand
import string


def MakeCipher(SEED):
    # create a shuffled alphabet
    letters = [letter for letter in string.ascii_lowercase]
    rand.Random(SEED).shuffle(letters)

    # create a dictionary lookup
    cipher = {}
    for idx, letter in enumerate(letters):
        cipher[letter] = idx

    return cipher


def DecmalToBase13(number):
    conversion = ('0', '1', '2', '3', '4',
                  '5', '6', '7', '8', '9', 'a', 'b', 'c')
    return conversion[(number//13) % 13] + conversion[number % 13]


def JumbleMessage(cleanMessage, seed):
    cipher = MakeCipher(seed)
    obscureMessage = []
    for letter in cleanMessage.lower():
        if letter in cipher:
            obscureMessage.append(DecmalToBase13(cipher[letter]))
        else:
            obscureMessage.append(letter)
    return obscureMessage


SEED = 10

MESSAGE = 'hello world!'
for key, value in zip(MakeCipher(SEED).keys(), MakeCipher(SEED).values()):
    print(f'k:{key} v:{value}')

print(f'Message: {" ".join(str(i) for i in JumbleMessage(MESSAGE, SEED))}')

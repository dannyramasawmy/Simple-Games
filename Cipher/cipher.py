
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
    return [DecmalToBase13(cipher[letter]) for letter in MESSAGE if letter in cipher]


SEED = 10

MESSAGE = 'hello world!'
print(f'Message: {JumbleMessage(MESSAGE, SEED)}')

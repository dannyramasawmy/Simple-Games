
import random as rand


def MakeCipher(SEED):
    # create a shuffled alphabet
    asciiA = ord('a')
    asciiZ = ord('z')
    alphaRange = asciiZ - asciiA
    letters = [chr(i + asciiA) for i in range(alphaRange + 1)]
    rand.Random(SEED).shuffle(letters)

    # create a dictionary lookup
    cipher = {}
    for idx, letter in enumerate(letters):
        cipher[letter] = idx

    return cipher


def DecmalToBase13(input_):
    return input_


SEED = 10

MESSAGE = 'hello world!'

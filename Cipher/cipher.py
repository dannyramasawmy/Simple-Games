
import random as rand
import string


def MakeCipher(SEED):
    # create a shuffled dictionary of letters
    letters = [letter for letter in string.ascii_lowercase]
    rand.Random(SEED).shuffle(letters)
    return {letter: value for value, letter in enumerate(letters)}


def DecmalToBase13(number):
    conversion = ('0', '1', '2', '3', '4',
                  '5', '6', '7', '8', '9', 'a', 'b', 'c')
    return conversion[(number//13) % 13] + conversion[number % 13]


def JumbleMessage(cleanMessage, cipher):
    return [DecmalToBase13(cipher[letter]) if letter in cipher else letter for letter in cleanMessage.lower()]


# constants
SEED = 10
MESSAGE = 'hello world!'
CIPHER = MakeCipher(SEED)

# display
for key, value in CIPHER.items():
    print(f'{key}:{value}')
print(f'Message: {" ".join(str(i) for i in JumbleMessage(MESSAGE, CIPHER))}')

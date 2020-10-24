import re
import urllib.request

# TODO: parse the html to get the letters import html from website
# fp = urllib.request.urlopen("https://www.nytimes.com/puzzles/spelling-bee").read()
# rawHTML = fp.decode("utf8")
# fp.close()
# print(rawHTML)


# paths
prepath = 'SpellingBee/'
filename = prepath + 'english3.txt'

# input characters
specialCharacter = 'h'
searchCharacters = 'meyalhc'

# compile search pattern
pattern = re.compile(r"\b[" + searchCharacters + r"]{4,20}\b")

# read words for <dict>.txt and write matches to a file
with open(prepath + 'spellingBeeSuggestions.txt', 'w') as f:
    for i, line in enumerate(open(filename)):
        for match in re.finditer(pattern, line):
            if specialCharacter in line:
                f.write(line)
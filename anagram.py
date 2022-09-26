print("Check if two words or phrases are anagrams")
word1 = input("First Word/Phrase: ")
word2 = input("Second Word/Phrase: ")
print()


word1Low = word1.lower()
word2Low = word2.lower()

lstWord1Low = []
lstWord2Low = []
counter = 0
z = True
alphabetCounter = {
  "a": 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0,
      "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0,
          "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0, " " : 0
}

for letter in word1Low:
    lstWord1Low.append(letter)
for letter in word2Low:
    lstWord2Low.append(letter)


if (len(lstWord2Low) == len(lstWord1Low)):
    for letter in alphabetCounter:
        for lettered in lstWord1Low:
            if (letter == lettered):
                alphabetCounter[letter] = alphabetCounter[letter] + 1
        for lettered in lstWord2Low:
            if (letter == lettered):
                alphabetCounter[letter] = alphabetCounter[letter] + 1
                
    for letters in alphabetCounter:
        num = alphabetCounter[letters]
        if (num%2 != 0):
            print(word1, "and", word2, "are not anagrams")
            z = False
            break
    
    
    if (z == True):
        print(word1, "and", word2, "are anagrams")

else:
    print(word1, "and", word2, "are not anagrams")

# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}

word = 'rapture'

wordList = ['rapture']

# def isValidWord(word, hand, wordList):
"""
Returns True if word is in the wordList and is entirely composed of letters in the hand. Otherwise, returns False. Does not mutate hand or wordList.
word: string
hand: dictionary (string -> int)
wordList: list of lowercase strings
"""
count = 0
hand_copy = hand.copy()
# if word in wordList:            # this check works fine if word is present in wordList or not
for i in range(len(word)):
    if word[i] in hand_copy.keys():
        count += 1
        hand_copy[word[i]] -= 1
        if hand_copy[word[i]] == 0:
            del hand_copy[word[i]]
    else:
        break
if word in wordList and count == len(word):
    print('ok')
else:
    print('check code')
# else:
#     print(False)




# hand_copy = hand.copy()
# for char in word:
#     hand_copy[char] -= 1
#     if hand_copy[char] == 0:
#         del hand_copy[char] 
# print(hand_copy)



    # score = 0
    # for char in word:
    #     score += SCRABBLE_LETTER_VALUES[char]
    # score *= len(word)

    # if len(word) == n:
    #     score += 50

    # return score



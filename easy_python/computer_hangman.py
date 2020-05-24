##import library
import random

#variables and data types to be used later
allowed_attempts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
allowed_word_length = [4, 5, 6]
words_4 = ["nerd", "math", "kboo", "mala"]
words_5 = ["happy", "stats", "thingy", "chaan"]
words_6 = ["tswift", "tiktok", "rstats", "fluffy"]
correct_attempt = True 
correct_word_length = True
alphabets = ["aeioubcdfghjklmnpqrstvwxyz"]
vowels = ["aeiou"]
non_vowels = ["bcdfghjklmnpqrstvwxyz"]

#starting game manually.. waiting for user input
print("Starting a game of Hangman... Joy's go-to words. Computer version")

def split(word): 
    return [char for char in word]  

alphabets = list(alphabets[0])
vowels = list(vowels[0])
non_vowels = list(non_vowels[0])

#choosing the word
actual_word = words_4[random.randint(0,4)]
#output screen 
output = ['*']*len(actual_word)

#adding one line
check_if_win = 0

for j in range(0, 10):
	#dumb computer guess
	guess = alphabets[random.randint(0,len(alphabets))]

	for j in range(len(actual_word)):
		if(actual_word[j] == guess):
			output[j] = guess
			alphabets = alphabet.pop(j)
			check_if_win = check_if_win + 1

	print(guess)
	print(output)
	print(actual_word)


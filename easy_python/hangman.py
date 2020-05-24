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

#starting game manually.. waiting for user input
print("Starting a game of Hangman... Joy's go-to words")

while(correct_attempt):
	attempts = int(input("How many incorrect attempts do you want? [1-10]: "))
	for i in range(len(allowed_attempts)):
		if(allowed_attempts[i] == attempts):
			correct_attempt = False

while(correct_word_length):
	word_length = int(input("What minimum word length do you want? [4-6]: "))
	for i in range(len(allowed_word_length)):
		if(allowed_word_length[i] == word_length):
			correct_word_length = False

#randomly selecting word
print("Selecting a word...")

index = random.randint(0,4)

if(word_length == 4):
	answer = words_4[index]

elif(word_length == 5):
	answer = words_5[index]

else:
	answer = words_6[index]

#split word into array for simplicity 
def split(word): 
    return [char for char in word]  

later_print = answer
answer = split(answer)	
output = ['*']*word_length

print("your word is...")
print(output)



playing_game = True
guesses = 0

#check if win. function will be used later
def check(check_if_win, answer, guesses, attempts):
	for l in range(len(answer)):
		if(output[l] == answer[l]):
			check_if_win = check_if_win + 1

	if(check_if_win == len(answer)):
		print("you win! It took you " + str(guesses-1)+ " tries")
		return False 
	if(guesses == attempts):
		print("you lose! The word is " + later_print) 
		return False 
	else:
		return True

#game will keep playing until one condition is broken
while(playing_game):
	#accepting guesses
	check_if_win = 0
	guess = str(input("Accepting guesses: "))

	#changing display if guess is correct
	for j in range(len(answer)):
		if(answer[j] == guess):
			output[j] = guess
	print(output)

	guesses = guesses + 1
	playing_game = check(check_if_win, answer, guesses, attempts)





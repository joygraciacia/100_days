print("Starting a game of Hangman...")

allowed_attempts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
allowed_word_length = [4, 5, 6]
words_4 = ["saga", "lava", "juke"]
words_5 = ["happy", "blunt", "tasty"]
words_6 = ["butter", "harvard", "appall"]
correct_attempt = True 
correct_word_length = True

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

print("Selecting a word...")

if(word_length == 4):
	answer = words_4[0]

elif(word_length == 5):
	answer = words_5[0]

else:
	answer = words_6[0]

def split(word): 
    return [char for char in word]  

answer = split(answer)	
output = ['*']*word_length

print(split(answer))
print("your word is...")
print(output)



playing_game = True
guesses = 1 

while(playing_game):
	check_if_win = 0
	guesses = guesses + 1
	guess = str(input("Accepting guesses: "))

	for j in range(len(answer)):
		if(answer[j] == guess):
			output[j] = guess
	print(output)


	for l in range(len(answer)):
		if(output[l] == answer[l]):
			check_if_win = check_if_win + 1

 
    if(check_if_win == len(answer)):
    	print("you win!")
    	playing_game = False

	# if(check_if_win == len(answer)):
	# 	print("You win!")
	# 	playing_game = False

	# if(guesses == attempts):
	# 	print("You lose!")
	# 	playing_game = False



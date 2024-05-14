import sys
import os

def Convert(string):
    list1 = []
    list1[:0] = string.strip()
    return list1

print("Input the word you'd like your opponent to guess")
word = str((sys.stdin.readline()).lower())
if len(word) <= 1:
	print("You most have a valid word of atleast 2 letters")
	exit()
list_word = Convert(word)
print("Input how many tries the player gets")
trys = int(sys.stdin.readline())
os.system('clear')
print(f'You have {trys} tries to guess this word')
blocked_word = ""
i = 0
while i < (len(word) - 1):
	if word[i] == " ":
		blocked_word = blocked_word + " "
	else:
		blocked_word = blocked_word + "*"
	i += 1
print(blocked_word.strip())
blocked_word = Convert(blocked_word.strip())
letters = []

i = 1
while i <= trys:
	guess = sys.stdin.readline()
	guess = (guess.strip()).lower()
	while guess in letters:
		print(f'You have already tried these letters {", ".join(set(letters))} try again')
		guess = sys.stdin.readline()
		guess = (guess.strip()).lower()
	letters.append(guess)
	if len(guess) == 1:
		if guess in word:
			j = 0
			while j < len(word):
				if word[j] == guess:
					blocked_word[j] = guess
				j += 1
			print("".join(blocked_word))
		if blocked_word == list_word:
			if i == 0:
				print(f'You saved him in 1 try')
			else:
				print(f'You saved him in {i + 1} tries')
			exit()

	elif blocked_word == list_word or guess.strip() == word.strip():
		if i == 0:
			print("You saved him in 1 try")
		else:
			print(f'You saved him in {i + 1} tries')
		exit()

	elif len(guess.strip()) > 1 and guess.strip() != word.strip():
		print(f"You guessed wrong and didn't save him :(\nThe word was {word}")
		exit()
	print(f'\nYou have tried these letters\n{set(letters)}\nYou have {trys - i} attempts left\n')
	i += 1
if i >= trys:
	print(f"You coudn't save him :(\nThe word was {word}")

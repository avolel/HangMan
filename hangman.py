from random import *
from os import system, name

playerScore = 0
computerScore = 0

def StartGame():
	ClearScreen()
	print("Let's Play a Game of Hangman.")
	while PlayGame():
		pass
	ShowScores()

def PlayGame():	
	HangmanDictionary = ["abruptly","absurd","abyss","affix","askew","avenue","azure","bagpipes",
	"bandwagon","boggle","blitz","boxcar","boxful","buffalo","cobweb","crypt","cycle","cockiness",
	"curacao","croquet","caliph","funny","zebra","andy","brooklyn","bronx","queens","bridgetown","valencia"]

	word = choice(sample(HangmanDictionary, len(HangmanDictionary)))
	wordlength = len(word)
	clue = wordlength * ["_"]
	NumberofTries = 6
	WordsTried = "|"
	WordsWrong = 0
	global playerScore, computerScore

	clue[0] = word[0]
	clue[wordlength - 1] = word[wordlength - 1]

	print()
	print(f"I'm thinking of a {wordlength} letter word that starts with \"{word[0]}\" and ends with \"{word[wordlength - 1]}\". What word am I thinking of?")

	while(WordsWrong != NumberofTries):
		guessedword = GuessWord()
		if(WordsTried.find(guessedword) != -1):
			ClearScreen()
			ShowClue(clue,WordsTried)
			print(f"You have already guessed this word: \"{guessedword}\"")
		else:
			WordsTried = f'{WordsTried}{guessedword}|'
			firstIndex = word.find(guessedword)
			if(firstIndex == -1):
				WordsWrong += 1
				RevealNextLetterInClue(wordlength,word,clue)
				ClearScreen()				
				if (WordsWrong == NumberofTries) or ("".join(clue) == word):
					print()
					print("Game Over!")
					print(f"The word was {word}")
					computerScore += 1
					break				
				print(f"I'm sorry, \"{guessedword}\" isn't the word I'm thinking of.")
				ShowHangManGraphic(WordsWrong)
				ShowClue(clue,WordsTried)
			else:
				ClearScreen()
				print("Congratulations, you guessed the correct word.")
				print()
				print("You Won!")
				print(f"The word is {word}")
				playerScore += 1
				break
	return PlayAgain()

def RevealNextLetterInClue(wordlen, word, clue):
	for i in range(wordlen):
		if word[i] != clue[i]:
			clue[i] = word[i]
			break
	return clue

def ShowClue(clue, wordsTried):
    print()
    print("Clue:", "".join(clue))
    print(f"Guesses: {wordsTried}")

def GuessWord():
	print()
	while True:
		word = input("Guess the correct word: ")
		word.strip()
		word.lower()	
		print()
		if word.isalpha():
			return word
		print()
		print("Invalid guess. Please guess the correct word.")

def PlayAgain():
	print()
	Answer = input("Do you want to play again? Yes/No: ")
	if(Answer in ("y","Y","yes","Yes")):
		return Answer
	else:
		print("Thank you for playing. See you next time!")

def ShowScores():
	global playerScore, computerScore
	print()
	print("HIGH SCORES")
	print("Player: ",playerScore)
	print("Computer: ",computerScore)

def ClearScreen():
	if name == 'nt':
		_ = system("cls")
	else:
		_ = system("clear")

def ShowHangManGraphic(hangman):
	graphics = [
	"""
		+-------+
		|
		|
		|
		|
		|
	 ==============
	""",
	"""
		+-------+
		|       |
		|       O
		|
		|
		|
	 ==============
	""",
	"""
		+-------+
		|       |
		|       O
		|       |
		|
		|
	 ==============
	""",
	"""
		+-------+
		|       O
		|      -|
		|
		|
		|
	 ==============
	""",
	"""
		+-------+
		|       |
		|       O
		|      -|-
		|
		|
	 ==============
	""",
	"""
		+-------+
		|       |
		|       O
		|      -|-
		|      /
		|
	 ==============
	""",
	"""
		+-------+
		|       |
		|       O
		|      -|-
		|      / \\
		|
	 ==============
	"""
	]
	print(graphics[hangman])
	return

if __name__ == "__main__":
	StartGame()
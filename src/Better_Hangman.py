import random

# Miggy Reyes
# Started on 12/3/2017
# Completed on 12/10/2017
# Personal Project - Hangman Application
# This is a simple game of hangman that will be played directly on the console
#
# This is an edited version of the bad code because I do not want to leave it
# unfixed.


def main():
	"""
	This will run the code to the end with check_letter() being the menu/loop
	That will check each letter input.
	:return:
	"""
	print(
		"Hello, welcome to the game of Hangman.\n"
		"Here, you will have 8 guesses. Your guess may be letters or words.\n"
		"Each letter and word will count as one guess. \n"
		"You may (1) have a word chosen for you or "
		"(2) input your own word to guess.")
	attempts_remaining = 8
	response = True
	while response is True:
		response = input('>> ')
		if response is "1":
			word, correct_answers, word_to_guess = get_random_word()
			display_state(
				word, attempts_remaining, blanks="".join(word_to_guess))
			check_letter(word, attempts_remaining, correct_answers, word_to_guess)

		elif response is "2":
			word, correct_answers, word_to_guess = get_user_word()
			display_state(
				word, attempts_remaining, blanks="".join(word_to_guess))
			check_letter(word, attempts_remaining, correct_answers, word_to_guess)
		else:
			print('Please pick a valid option')
			response = True


def check_letter(word, attempts_remaining, correct_answers, word_to_guess):
	"""
	This will check to see if the response is correct in any way
	:return:
	"""
	while attempts_remaining > 0:

		letter = input("What letter would you like to guess?\n>> ").upper()

		if letter == word:
			break

		elif len(letter) > 1:
			print("Please only guess one letter at a time.")

		elif letter in correct_answers:
			"""
			This should try and update the correct answers list and tell the 
			user what letter they got correct.
			"""
			correct_answers = update_correct_answers(correct_answers, letter)
			word_to_guess = update_blanks(letter, word_to_guess, word)
			if not correct_answers:
				break
			print("\nThe letter {} is correct".format(letter))
			display_state(word, attempts_remaining, word_to_guess)

		elif letter not in correct_answers:
			"""
			This should send decrease the amount of attempts remaining and 
			tell the user what letter they got wrong
			"""

			print("\nThe letter {} is incorrect.".format(letter))
			attempts_remaining -= 1
			display_state(word, attempts_remaining, word_to_guess)

	print('Congratulations, the word was {}!'.format(word))

	if attempts_remaining == 0:
		print('Sorry. Game over.')

	response = input('Would you like to play again?\n>> ').lower()
	if response == 'yes':
		main()


def update_correct_answers(correct_answers, letter):
	"""
	This function will make sure that the user cannot guess the same letter
	twice.
	:param letter: the letter that was guessed
	:param correct_answers: The word that needs to be guessed
	:return: a list of the correct answers
	"""

	index_answers = correct_answers.index(letter)
	while index_answers > -1:

		correct_answers = list(correct_answers)
		correct_answers[index_answers] = ""
		correct_answers = "".join(correct_answers)
		index_answers = correct_answers.find(letter, index_answers)

	return correct_answers


def update_blanks(letter, blanks, word):
	"""
	This function will continue the blanks so the user will know what they
	have guessed correctly
	:param letter: This will replace the blank with the guessed word
	:param blanks: this is the blank space updated
	:param word: this is the word that was guessed. This is used to determine
	the index
	:return: returns the updated version of the blank to be printed in the
	display_state function
	"""
	index_guess = word.index(letter)
	while index_guess > -1:
		blanks = list(blanks)
		blanks[index_guess] = letter
		blanks = "".join(blanks)
		index_guess = word.find(letter, index_guess + 1)

	return blanks


def display_state(word, incorrect_attempts, blanks):
	"""
	Will give the current information needed to solve the Hangman puzzle.
	:return:
	"""
	spaces = 0
	for i in word:
		if " " is i:
			spaces += 1
	print('There are {} spaces in this word.'.format(spaces))
	letter_count = (len(word) - spaces)
	print('There are {} letters in this word.'.format(letter_count))
	print('You have {} attempts remaining.'.format(incorrect_attempts))
	blanks = "".join(blanks)
	print(blanks)
	return letter_count, spaces


def get_random_word():
	"""
	If they ask for it, we will pick out a random word for them to guess.
	:return: The word that the user will guess
	"""
	response = True
	word = ""
	food = [
		'chips', 'sushi', 'boba', 'spaghetti', 'adobo', 'rice', 'hamburger',
		'cheeseburger', 'sandwich']
	animals = [
		'chicken', 'pig', 'dolphin', 'giraffe', 'elephant', 'dinosaur',
		'shark', 'rhino', 'lion', 'owl', 'zebra']
	artists = [
		'Beyonce', 'Khalid', 'Willie Nelson', 'Sam Smith', 'Pentatonix',
		'Buddy Holly', 'Selena Gomez', 'Kendrick Lamar', 'Demi Lovato']
	brands = [
		'Nike', 'Gucci', 'Chanel', 'Adidas', 'Apple', 'Vans',
		'Ralph Lauren', 'Converse', 'Louis Vuitton', 'Vera Bradley']
	colleges = [
		'Texas Tech', 'University of Houston', 'NorthWestern',
		'University of Texas at Austin', 'Stanford', 'Harvard',
		'Cambridge', 'Mississippi State', 'University of North Texas']
	while response is True:

		response = input(
			" There are 5 categories for you to choose from.\n"
			"(1) Food\n"
			"(2) Animals\n"
			"(3) Artists\n"
			"(4) Brands\n"
			"(5) Colleges\n>> ")

		if response is "1":
			word = random.choice(food).upper()
		elif response is "2":
			word = random.choice(animals).upper()
		elif response is "3":
			word = random.choice(artists).upper()
		elif response is "4":
			word = random.choice(brands).upper()
		elif response is "5":
			word = random.choice(colleges).upper()
		else:
			print("Please input a number 1 - 5...")

	correct_answers = list(word.replace(" ", ""))
	word_to_guess = list(len(word) * "_")
	print(75 * '\n')

	return word, correct_answers, word_to_guess


def get_user_word():
	"""
	If they ask for it, they can input their own word. This function will
	make the whole guessed word uppercase and give the amount of letters
	needed to complete the word.
	:return:
	"""
	word = input("What word would you like to guess?\n>> ").upper()
	correct_answers = list(word.replace(" ", ""))
	word_to_guess = list(len(word) * "_")
	print(75 * '\n')

	return word, correct_answers, word_to_guess


if __name__ == "__main__":
	main()

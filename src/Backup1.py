import random

# Miggy Reyes
# Completed on 10/24/17
# Personal Project - Hangman Application
# This is a simple game of hangman that will be played directly on the console
#
# This is an edited version of the ba code because I do not want to leave it
# unfixed.

food = [
	'chips', 'sushi', 'boba', 'spaghetti', 'adobo', 'rice', 'hamburger',
	'cheeseburger', 'sandwich']
animals = [
	'chicken', 'pig', 'dolphin', 'giraffe', 'elephant', 'dinosaur'
	, 'shark', 'rhino', 'lion', 'owl', 'zebra']
artists = [
	'Beyonce', 'Khalid', 'Willie Nelson', 'Sam Smith', 'Pentatonix',
	'Buddy Holly', 'Selena Gomez', 'Kendrick Lamar', 'Demi Lovato']
brands = [
	'Nike','Gucci', 'Chanel', 'Adidas', 'Apple', 'Vans',
	'Ralph Lauren', 'Converse', 'Louis Vuitton', 'Vera Bradley']
colleges = [
	'Texas Tech', 'University of Houston', 'NorthWestern',
	'University of Texas at Austin', 'Stanford','Harvard',
	'Cambridge', 'Mississippi State', 'University of North Texas']


def give_solution(word):
	print('Congratulations, the word was {}!'.format(word))
	print(' Would you like to play again? \n ')
	response = input("> ").lower()
	if response not in ("yes", "y"):
		play_again = False
		return play_again


def menu():

	play_again = True
	ans_for_menu = True
	ans_for_menu_2 = True

	while play_again is True:

		print("Hello! Today, we will be playing Hangman. \n")

		while ans_for_menu is True:
			ans_for_menu = input(
				"What would you like to do?\n"
				"(1) Have a random word picked out for you.\n"
				"(2) Input your own word \n>> ")
			if ans_for_menu is "1":
				while ans_for_menu_2 is True:
					# This is the start of the new menu for categories
					ans_for_menu_2 = input(
						"What category would you like to pick from?\n"
						"(1) Food\n"
						"(2) Animals\n"
						"(3) Artists\n"
						"(4) Brands\n"
						"(5) Colleges\n>> ")
					if ans_for_menu_2 is "1":
						word = random.choice(food).upper()
					elif ans_for_menu_2 is "2":
						word = random.choice(animals).upper()
					elif ans_for_menu_2 is "3":
						word = random.choice(artists).upper()
					elif ans_for_menu_2 is "4":
						word = random.choice(brands).upper()
					elif ans_for_menu_2 is "5":
						word = random.choice(colleges).upper()
					else:
						print('Please input a value from 1 to 5')

			elif ans_for_menu is "2":
				word = input(
					'What is the word that y''all '
					'want to guess? \n>> ').upper()
			else:
				print('Please input either 1 or 2 \n')
				ans_for_menu = True

	return play_again, word


def clear_console():
	for i in range (0,50): # Clears IDLE
		print(' \n')


def initial_info(word):

	"""
	Will show how many letters are in the word that we are trying to guess
	:param word: the word that we have to guess
	:return: length of the phrase or word without spaces
	"""

	word_without_spaces = word.replace(" ", "")
	print('This word has {} letters.'.format((len(word_without_spaces))))
	return word_without_spaces

def get_letter():
	letter = input('So what letter would you like to guess? \n>> ').upper()
	# Asks for the letter
	return letter


def convert_word(word_without_spaces):
	list_word = list(word_without_spaces)
	# this is for the purpose of determining if the letter is correct
	completed_word = (len(word_without_spaces) * "_")
	# We are trying to make a blank space that is the
	# correct amount of spaces to index
	return list_word, completed_word


def check_attempts(word):

	"""
	This will check to see how many attempts we have left
	:param word:
	:return:
	"""

	attempts = 8
	correct_attempts = 0
	incorrect_attempts = 0
	if " " in word:
		correct_attempts += word.count(" ")

	while incorrect_attempts < 8 and correct_attempts != len(word):
		if letter == word:
			give_solution(word)
			break

		elif len(letter) > 1:
			print('Please give only one letter at a time...')
			print(completed_word + '\n')
			letter = input(
				'So what letter would you like to guess? \n>> ').upper()

		elif letter in list_word:

			completed_word_list = list(completed_word) # Turns it to a list

			index = word_without_spaces.find(letter) # 'Finds the index of letter within "word"'
			while index >= 0: # 'This is the loop that will allow'
				list_word[index] = [] # This will make sure we don't put in the same letter and still get it right
				completed_word_list[index] = letter # This is the line that replaces first occurrance
				if letter in completed_word_list:
					correct_attempts += 1
				index = word_without_spaces.find(letter,index+1) # Finds the next occurrence. The second parameter allows the function to start looking for the next index starting after the first found index

			temp_completed_word_list = "".join(completed_word_list)# turns the list back into a string
			completed_word = temp_completed_word_list # Gives me back the list as a string

			print('This is correct')

			if correct_attempts != len(word):
				print(completed_word + '\n')
				letter = input('So what letter would you like to guess? \n>> ').upper()

			elif correct_attempts == len(word):
				give_solution(word)
				break

		elif letter not in list_word:
			incorrect_attempts += 1
			attempts -= 1
			print('This is incorrect. You have ',attempts,' attempts left. \n')

			if incorrect_attempts != 8:
				print(completed_word + '\n')
				letter = input("So what letter would you like to guess? \n>> ").upper()

			elif incorrect_attempts == 8:
				give_solution(word)
				break
		else:
			result = "invalid input"


def replace_spaces():
	pass


def main():
	"""
	In this function, we will run through the whole code as it needs to
	:return:
	"""
	# 1. Menu
	# 2. Get a word
	# 3. Break down the word so that we can manipulate it
	# 4. Get a letter
	# 5. Make find a way to replace the black spaces with the letter
if __name__ == "__main__":
	menu()

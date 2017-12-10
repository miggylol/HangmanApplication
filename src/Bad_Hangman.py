import random
#--------------------------------------------------Hangman-------------------------------------------#
# Miggy Reyes
# Completed on 10/24/17
# Personal Project - Hangman Application

# Algorithm
# step 1: We need to get inputs
# Step 2: We need to determine if the letters are correct
# Step 3: We need to print out the letters that are correct if they are correct
# Step 4: We need to tell them that they are wrong if the letters are
# Step 5: We need to keep asking for more letters
# Step 6: Once the word is complete, we need to end the loop of questions and say "Done!"
#----------------------------------------------Dictionary-----------------------------------------------#
food = ['chips','sushi','boba','spaghetti','adobo','rice','hamburger','cheeseburger','sandwich']
animals = ['chicken','pig','dolphin','giraffe','elephant','dinosaur','shark','rhino','lion','owl','zebra']
artists = ['Beyonce','Khalid','Willie Nelson','Sam Smith','Pentatonix','Buddy Holly','Selena Gomez','Kendrick Lamar','Demi Lovato']
brands = ['Nike','Gucci','Chanel','Adidas','Apple','Vans','Ralph Lauren','Converse','Louis Vuitton','Vera Bradley']
colleges = ['Texas Tech','University of Houston','NorthWestern','University of Texas at Austin','Stanford','Harvard','Cambridge','Mississippi State','University of North Texas']
drugs = ['ecstasy','weed','cocaine','amphetamines','meth','heroine','crack','LSD','cigarettes']
#------------------------------------------------Variables----------------------------------------------#

# Have spaces be already guessed

def main():
# have Dane look at this code and ask how he can put the ask_again and have it work
	play_again = True

	while play_again == True:

		print("Hello! Today, we will be playing Hangman. \n")
		ans_for_menu = True
		ans_for_menu_2 = True

		while ans_for_menu == True:
			ans_for_menu = input("""What would you like to do?
(1) Have a random word picked out for you.
(2) Input your own word \n>> """)
			if ans_for_menu == "1":
				while ans_for_menu_2 == True: # This is the start of the new menu for categories
					ans_for_menu_2 = input(
						"What category would you like to pick from?"
						"(1) Food"
						"(2) Animals"
						"(3) Artists"
						"(4) Brands"
						"(5) Colleges\n>> ")
					if ans_for_menu_2 == "1":
						word = random.choice(food).upper()
					elif ans_for_menu_2 == "2":
						word = random.choice(animals).upper()
					elif ans_for_menu_2 == "3":
						word = random.choice(artists).upper()
					elif ans_for_menu_2 == "4":
						word = random.choice(brands).upper()
					elif ans_for_menu_2 == "5":
						word = random.choice(colleges).upper()
					else:
						print('Please input a value from 1 to 5')

			elif ans_for_menu == "2":
				word = input(
					'What is the word that y''all'
					' want to guess? \n>> ').upper()
			# Asks for word
			else:
				print('Please input either 1 or 2 \n')
				ans_for_menu = True

		for i in range (0,50): # Clears IDLE
			print(' \n')

		word_without_spaces = word.replace(" ", "")

		list_word = list(word_without_spaces)  # this is for the purpose of
		# determining if the letter is correct

		print('This word has ' + str(len(word_without_spaces)) + ' letters.')
		# Says how many letters are in the word
		letter = input('So what letter would you like to guess? \n>> ').upper()
		# Asks for the letter

		completed_word = (len(word_without_spaces) * "_")
		# We are trying to make a blank space that is the
		# correct amount of spaces to index
		attempts = 8
		correct_attempts = 0
		if " " in word:
			correct_attempts += word.count(" ")

		incorrect_attempts = 0

		while incorrect_attempts < 8 and correct_attempts != len(word):
			# It won't break the loop when we input no as
			# we ask if they want to play again
			if letter == word:
				print('Congratulations, the word was ' + str(word) + ' !')
				print(' Would you like to play again? \n ')
				response = input("> ").lower()
				if response not in ("yes", "y"):
					play_again = False
				break

			elif len(letter) > 1:
				print('Please give only one letter at a time...')
				print(completed_word + '\n')
				letter = input(
					'So what letter would you like to guess? \n>> ').upper()

			elif letter in list_word:

				completed_word_list = list(completed_word)
				# Turns it to a list

				index = word_without_spaces.find(letter)
				# 'Finds the index of letter within "word"'
				while index >= 0:
					# 'This is the loop that will allow'
					list_word[index] = []
					# This will make sure we don't put in the
					# same letter and still get it right
					completed_word_list[index] = letter
					# This is the line that replaces first occurrence
					if letter in completed_word_list:
						correct_attempts += 1
					index = word_without_spaces.find(letter,index+1)
					# Finds the next occurrence.
					# The second parameter allows the function to start looking
					# for the next index starting after the first found index

				temp_completed_word_list = "".join(completed_word_list)
				# turns the list back into a string
				completed_word = temp_completed_word_list
				# Gives me back the list as a string

				print('This is correct')

				if correct_attempts != len(word):
					print(completed_word + '\n')
					letter = input(
						'So what letter would you like to guess? \n>> ').upper()

				elif correct_attempts == len(word):
					print('Congratulations, the word was ' + str(word) + ' !')
					print(' Would you like to play again? \n')
					response = input(">> ").lower()
					if response not in ("yes","y"):
						play_again = False


			elif letter not in list_word:
				incorrect_attempts += 1
				attempts -= 1
				print(
					'This is incorrect. You have ',
					attempts,' attempts left. \n')


				if incorrect_attempts != 8:
					print(completed_word + '\n')
					letter = input(
						"So what letter would you like to guess? \n>> ").upper()

				elif incorrect_attempts == 8:
					print(' Sorry! Game over! The word was ' + word + '.')
					print(' Would you like to play again? \n')
					response = input(">> ").lower()
					if response not in ("yes","y"):
						play_again = False
						break
			else:
				result = "invalid input"


if __name__ == "__main__":
	main()

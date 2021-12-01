import os

HANGMAN_PHOTOS = {
	0:
			"x-------x"
	,
	1:

	"""
			x-------x
			|
			|
			|
			|
			|
	"""
	,
	2:
	"""
			x-------x
			|       |
			|       0
			|
			|
			|"""
	,
	3:
	""""
			x-------x
			|       |
			|       0
			|       |
			|
			|"""
	,
	4:
	"""
			x-------x
			|       |
			|       0
			|      /|\\
			|
			|
			"""
	,
	5:"""
			x-------x
			|       |
			|       0
			|      /|\\
			|      /
			|
			"""
	,
	6:"""
			x-------x
			|       |
			|       0
			|      /|\\
			|      / \\
			|
			"""
}

def check_win(secret_word, old_letters_guessed):
	"""check if all the letter of the secret word exist in the list of the old letters guessed
	:param secret_word: the word that the player need to discover
	:param old_letters_guessed: list of the letter that the player guessed already
	:type secret_word: str
	:type old_letters_guessed: list
	:return: True if all the letter of the secret word exist in the list, else false.
	:rtype: bool
	"""
	count = 0
	for i in secret_word:
		if i in old_letters_guessed:
			count += 1
	if count == len(secret_word):
		return True
	return False

def charposition(string, char):
	""" indexes of specific character on string
	:param string: the function search the character on this string
	:param char: the specific character that the function search
	:type string: str
	:type char: char
	:return: list of the indexes of char on the string
	:rtype: list
	"""
	list_of_indexes = []
	for n in range(len(string)):
		if string[n] == char:
			list_of_indexes.append(n)
	return list_of_indexes
	
def show_hidden_word(secret_word, old_letters_guessed):
	"""show the hidden secret word with underline and letter.
	:param secret_word: the word that the player need to guess
	:param old_letters_guessed: list of letters that already guessed
	:type secret_word: str
	:type old_letters_guessed: list
	:return: string of the secret word, the letter that guessed show by letters and the another letters (that already guessed) show by under line.
	:rtype: str
	"""
	lst_to_return = []
	lst_to_return += "_" * len(secret_word)
	for letter in secret_word:
		if letter in old_letters_guessed:
			list_of_index = charposition(secret_word, letter)
			#index = index.find(secret_word, letter)
			for i in list_of_index:
				lst_to_return[i] = letter
	str_to_return = ' '.join(lst_to_return)
	return(str_to_return)
	
def check_valid_input(letter_guessed, old_letters_guessed):
	"""check if the input that entered is valid, the lenghtof the input it's 1 + the char that entered its letter(alpa) + the letter not guessed already
	:param letter_guessed: input from the user, letter he entered to guess, that function need to check
	:param old_letters_guessed: list of letters that already guessed
	:type letter_guessed: str
	:type old_letters_guessed: list
	:return: True if the input is valid, else False
	:rtype: bool
	"""
	if((len(letter_guessed) == 1) and (letter_guessed.isalpha())) and ((not(letter_guessed in old_letters_guessed))):
		return True
	else:
		return False
		
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""update the list of the letter that already guessed just if the input is valid else write 'X' to the user and print the letter that already guessed
	:param letter_guessed: input from the user, letter he entered to guess, that need to check if need to add it to the list of the letter that already guessed   
	:param old_letters_guessed: list of letters that already guessed
	:type letter_guessed: str
	:type old_letters_guessed: list
	:return: True if the list update, else False
	:rtype: bool
	"""
	if check_valid_input(letter_guessed, old_letters_guessed):
		old_letters_guessed.append(letter_guessed)
		return True
	else:
		print("X")
		old_letters_guessed = sorted(old_letters_guessed, key = min)
		string_of_old_letters_guessed = " -> ".join(old_letters_guessed)
		print("The letters that already guessed: %s \nTry another guess.." % string_of_old_letters_guessed)
		return False
				
def print_hangman(num_of_tries):
	"""print the the illustration of the level of the user on the game
	:param num_of_tries: the number of the level, the key of the illustration in the dict
	:type num_of_tries: int
	:retun:print the the illustration
	:rtype:None
	"""
	num_of_tries = int(num_of_tries)
	print ("\t %s " %HANGMAN_PHOTOS[num_of_tries])
	
def choose_word(file_path, index):
	"""choose secret word from file with string of words
	:param file_path: the path of the file with the string of the secret words
	:param index: the index of the word (that the user need to guess) in the list of the wors in the file
	:type file_path: str
	:type index: int
	:retun: tuple the compose from 2 members, member #1 is the amount of the words on the file(without duplicate) and member #2 it's the word that chosed
	:rtype: taple
	"""
	with open(file_path, "r") as file:
		index = int(index)
		text_of_file = file.read()
		full_list = text_of_file.split(" ")
		list_of_word = text_of_file.split(" ")
		for word in list_of_word:
			count = list_of_word.count(word)
			while count > 1:
				point_to_start_search = list_of_word.index(word)+1
				index_to_remove = list_of_word.index(word, point_to_start_search)
				del list_of_word[index_to_remove]
				count = list_of_word.count(word)
		num_of_words = len(list_of_word)
		mod_index = (index-1) % len(full_list)
		word_to_guss = full_list[mod_index]
		taple_to_return = (num_of_words, word_to_guss)
		return taple_to_return
	
def print_logo():
	"""print the logo of the game
	"""
	print("""
	======================================================
	    _    _
	   | |  | |
	   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
	   |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
	   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
	   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
	                        __/ |
	                       |___/

	======================================================
						   """)

def letter_guessed_in_secret_word(letter_guessed, secret_word):
	"""check if the secret_word contain the letter guessed
	:param secret_word: the word that the player need to discover
	:param letter_guessed: input from the user, letter he entered to guess, that function need to check
	:type secret_word: str
	:type letter_guessed: str
	:return:True if the secret_word contain the letter guessed, else False
	:rtype:bool
	"""
	if letter_guessed in secret_word:
		return True
	else:
		return False

def main():
	old_letters_guessed = []
	MAX_TRIES = 6
	print_logo()
	file_path = input("Please enter a words file path: ")
	if not os.path.exists(file_path):
		print("This file not exists, try again.\n")
		file_path = input("Please enter a words file path: ")
	index_of_word = input("Please enter an index: ")
	print("\n\n\t\t\t\t=============\n\t\t\t\t Let's play!\n\t\t\t\t============= \n\t\t   ~~ You have 6 tries to make a mistake! ~~\n\n")
	taple = choose_word(file_path, index_of_word)
	secret_word = taple[1]
	num_of_mistakes = 0
	print_hangman(num_of_mistakes)
	print("\n %s \n" %show_hidden_word(secret_word, old_letters_guessed))
	
	while num_of_mistakes < MAX_TRIES:
		letter_guessed = input ("\n\nGess a letter: ")
		letter_guessed = letter_guessed.lower()
		if letter_guessed_in_secret_word(letter_guessed, secret_word) and try_update_letter_guessed(letter_guessed, old_letters_guessed):
			print("\n %s" %show_hidden_word(secret_word, old_letters_guessed))
		elif not letter_guessed_in_secret_word(letter_guessed, secret_word) and try_update_letter_guessed(letter_guessed, old_letters_guessed):
				num_of_mistakes +=1
				print("):")
				print_hangman(num_of_mistakes)
				print("\n %s" %show_hidden_word(secret_word, old_letters_guessed))
		if check_win(secret_word, old_letters_guessed):
			print("\n\t\t=====\n\t\t WIN\n\t\t=====")
			return
	print("\n\t\t======\n\t\t LOSE \n\t\t======")
		
		

				
		

		
if __name__ == "__main__":
	main()

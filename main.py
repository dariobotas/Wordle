#First game is with a standard of words with 5 letters
#Choose difficulty after first game - between a word of 4 to 11 letters
#6 tentatives
#Each tentative checks:
##The word is the answer. 
##Not the answer but the right letter in right position
##Not the answer but right letter in the wrong position
#If 0 tentatives game finish
import art
import game_data
from random import randint, choice
from replit import clear

"""Defined functions"""
def get_logo(origin, number_logo):
  return origin[number_logo]

def random_word_from_difficulty(difficulty_list, option=1):
  new_option = option-1
  if new_option >= 0 or new_option <= 7:
    return choice(difficulty_list[new_option])
  else:
    return "Invalid Option"

def validate_answer(word_guess, word_answer):
  guessed_letter = []
  if word_guess.lower() == word_answer.lower():
    return True
  else:
    for guess_letter_position in range(len(word_guess)):
      letter_word_guess = word_guess[guess_letter_position]
      if word_answer[guess_letter_position].lower() == letter_word_guess.lower():
        guessed_letter.append(letter_word_guess.upper())
      elif letter_word_guess in word_answer:
        guessed_letter.append(letter_word_guess.lower())
      else:
        guessed_letter.append("_")
    return guessed_letter
    
def board_game(tentatives_dictionary, word_list):
  for word in range(len(tentatives_dictionary)):
    if word < len(word_list):
      print(f"{' '.join(tentatives_dictionary[word])} - {word_list[word]}")
    else:
      print(f"{' '.join(tentatives_dictionary[word])}")

"""Defined variables"""
random_logo = randint(0,2)
TENTATIVES = 6
tries = 1
DIFFICULTY = [game_data.words_letters4,game_data.words_letters5,game_data.words_letters6,game_data.words_letters7,game_data.words_letters8,game_data.words_letters9,game_data.words_letters10,game_data.words_letters11
]
logo = get_logo(art.logos,random_logo) 
end_of_game = False

"""Game play"""
def game(difficulty_choice=2):
  global end_of_game
  global tries
  global TENTATIVES
  global DIFFICULTY
  display = []
  word_to_guess = random_word_from_difficulty(DIFFICULTY, difficulty_choice)
  guess_words = []
  word_tentatives = {}
  
  for _ in range(len(word_to_guess)):
    display += "_"

  for _ in range(TENTATIVES):
    word_tentatives[_] = display
  
  print(logo)
  print("How to play?\nGuess the wordle in 6 tries.")
  print("Each guess must be a valid 5-letter word (in the standard game).")
  print("The upper/lower case of the tiles will change to show how close your guess was to the word.\n")
  print("Examples\n")
  print("  __a_E - image -> Upper case letters for right letter in the correct spot")
  print("  _ea__ - beach -> Lower case letters for right letter in the wrong spot")
  print("  _____ - start -> The letters are not in the word or any spot\n")
  
  while not end_of_game:
    board_game(word_tentatives, guess_words)
    #print(f"\nThe word: {word_to_guess}")
    #print(f"Tentatives: {tries}")
    guess_word = input("\nGuess a word: ").lower()
    clear()
    
    if len(guess_word) != len(word_to_guess):
      print(f"The word is with {len(word_to_guess)} letters!")  
    elif validate_answer(guess_word, word_to_guess) is True:
      #print(validate_answer(guess_word, word_to_guess))
      print(f"You win! The word was {word_to_guess}.")
      end_of_game = True
    else:
      guess_words.append(guess_word)
      answer_validated = validate_answer(guess_word, word_to_guess)
      word_tentatives[tries-1] = answer_validated
      if tries >= TENTATIVES:
        board_game(word_tentatives, guess_words)
        print(f"\nYou lost the game! The word was {word_to_guess}")
        end_of_game = True
      else:
        tries += 1

"""Options to play after first time"""
game()
while input("Play again? y or n: ") == "y":
  choose_difficulty = int(input("Choose the difficulty:\n  1- Word with 4 letters\n  2- Word with 5 letters (standard)\n  3- Word with 6 letters\n  4- Word with 7 letters\n  5- Word with 8 letters\n  6- Word with 9 letters\n  7- Word with 10 letters\n  8- Word with 11 or more letters\nOption: "))
  end_of_game = False
  tries = 1
  clear()
  game(choose_difficulty)
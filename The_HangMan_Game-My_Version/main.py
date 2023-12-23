import random
from replit import clear
from hangman_art import stages, logo
from hangman_words import words_list
print(logo)
print("\n----------------------Welcome to the HangMan Game!----------------------------\n\n")
# This is the category choices for the game.
Choice = int((input("Choose the category: \n1. Fruits\n2. Vegetables\n3. Animals\n4. Colors\n5. Countries\n6. Cities\n7. Food\n8. Objects\n9. Choose Randomly\n\nEnter your choice in number: ")))
#This done for choosing the random choice
if Choice == 9:
    Choice = random.randint(1,8)

# assigning list from the game_data file
word_list= words_list[Choice-1]
chosen_word= random.choice(word_list).upper()
word_length = len(chosen_word)

print("The word has", word_length, "letters :",end=" ")

display = []
# for creating empty list of underscores
for _ in range(word_length):
  display+="_"
print(display)

# looping the game for the gueses
lives = 6
end_of_game = False
while not end_of_game:
  guess = input("\nGuess a letter: ").upper()
  clear()
  if guess in display:
    print(f"You have already guessed {guess},Please guess another word.")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter 
      show = letter
    
  if show == guess:
    print(f"The chosen word has {show} in it.Now its {display}.\n\n")
  else:
    print(f"The chosen word does not have {guess} in it.Now its {display}.\n\n")
    
  if guess not in chosen_word:
    lives -= 1
    print(f"You have guessed {guess}, and that is not in the word.You have {lives} lives left.")
    print(stages[lives])
    if lives==0:
      end_of_game = True
      print("You have exhausted all the lives.You lost!")
      print(f"The word was {chosen_word}")
      break
  #ending condition for the loop
  if "_" not in display:
    end_of_game = True
    print("You guessed Right, You have won!")
    print(f"The word was {chosen_word}")
    break
    

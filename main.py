
import random
from hangman_words import word_list
from hangman_art import stages,logo

chosen_word = random.choice(word_list)
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

list_of_letters = [] 
for i in range(len(chosen_word)):
    list_of_letters.append('_')

win,lose = 0,0 
counter = 0
lives = 6
while(win==0 and lose==0):
  guess = input("Guess a letter: ").lower()
  if(guess in list_of_letters):
    print(f"You 've Already guessed {guess}")

  elif(guess not in chosen_word and lives > 0):
    print(f"You guessed {guess} ,That's not in the word. You Lose Life.")
    lives-=1

  else:
    for indx in range(len(chosen_word)):
        if(guess == chosen_word[indx]):
            list_of_letters[indx] = chosen_word[indx]
            counter+=1
      

  print(list_of_letters)

  if(counter==len(chosen_word)):
    win = 1
    print("You Win")

  if(lives==0):
    lose = 1
    print("You Lose !!")

  print(stages[lives])  
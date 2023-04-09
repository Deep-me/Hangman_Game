#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


#Check guessed letter
display = []
len=len(chosen_word)
for i in range(len):
  display.append("_")
x=len

while(x>0):
  guess = input("Guess a letter: ").lower()
  c=0
  for j in range(len):
    if chosen_word[j]==guess:
      display[j]=guess
      c+=1
  print(display)
  x-=c
print("You win.")
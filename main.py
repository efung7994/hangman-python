import words
import hangman_art
import random

print(hangman_art.logo)
word = random.choice(words.word_list)
answer = []
for blank in word:
    answer.append("_")
game_end = False
lives = 6


while game_end == False:
    print(word)
    print(f"{' '.join(answer)}")
    guess = input("Guess a letter: \n")
    for idx, letter in enumerate(word):
        if guess == letter:
            answer[idx] = guess
    if guess not in word:
        lives -= 1
    print(f"{' '.join(answer)}")
    print(hangman_art.stages[lives])
    print(lives)
    if "_" not in answer:
        game_end = True
        print("You Win!")
    if lives == 0:
        game_end = True
        print("You Lose")


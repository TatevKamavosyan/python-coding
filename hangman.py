import random

words_list = ['Code', 'Alpha', "Is", "A", 'Softwere', 'Development', 'Company']
secret_word = random.choice(words_list).lower()
guessed_letters = []
attempts = 6

print("Guess the word, letter by letter!")
print(f"You have {attempts} mistakes allowed.")
#print("Word list:", words_list)

while attempts > 0:
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
    print("\nWord:", display_word)
    print("Guessed letters:", ' '.join(guessed_letters))

    if '_' not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess.")
        attempts -= 1
        print(f"Attempts left: {attempts}")

if attempts == 0:
    print("Sorry, you ran out of attempts. The word was:", secret_word)
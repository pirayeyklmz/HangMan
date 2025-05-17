import random

pics = [
    """
   +---+
   |   |
       |
       |
       |
       |
=========""", """
   +---+
   |   |
   O   |
       |
       |
       |
=========""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""", """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""", """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
========="""
]

words = ["java", "python", "html", "ruby", "javascript", "css"]

while True:
    print("-" * 30 + "\nHangman Game\n" + "-" * 30)
    word = random.choice(words)
    correct_guesses = set()
    wrong_guesses = set()
    step = 0

    while step < len(pics) - 1:

        display_word = "".join([c if c in correct_guesses else "-" for c in word])
        print(pics[step])
        print("Word: " + display_word)


        guess = input("\nGuess a letter or the full word: ").lower()


        if guess == word:
            print("You Win!\n")
            break

        elif len(guess) == 1 and guess.isalpha():
            if guess in correct_guesses or guess in wrong_guesses:
                print("You already guessed that letter!")
            elif guess in word:
                correct_guesses.add(guess)
                if set(word) == correct_guesses:
                    print("You Win!\n")
                    break
            else:
                wrong_guesses.add(guess)
                step += 1
        else:
            print("Invalid input. Please guess a single letter or the full word.")

    else:
        print(pics[step])
        print(f"You Lose! The word was: {word}\n")

    if input("Play again (y/n): ").lower() != "y":
        break

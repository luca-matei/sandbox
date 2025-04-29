import random

def play_hangman():
    word_list = ["python", "hangman", "game"]
    word = random.choice(word_list)
    word_completion = "_" * len(word)  # p_t___
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    while guessed == False and tries != 0:
        display_hangman(tries)
        print(word_completion)
        guess = input("Enter a letter or word: ")  # Asta este o litera sau un cuvant

        if guess.isalpha() and len(guess) == 1:  # Guess are caractere doar din alfabet si este o singura litera
            if guess in guessed_letters:
                print(f"Letter '{guess}' has already been guessed!")
            elif guess not in word:
                print(f"Letter '{guess}' isn't in the word!")
                guessed_letters.append(guess)
                tries -= 1
            elif guess in word:
                guessed_letters.append(guess)
                word_as_list = list(word)  # p, y, t, h, o, n  -->  python
                
                indices = []  # Lista indicilor caracterelor ghicite
                for i, letter in enumerate(word_as_list):
                    # Litera din interatia curenta este cea ghicita
                    if guess == letter:
                        indices.append(i)

                # List comprehension
                # indices = [i for i, letter in enumerate(word_as_list) if guess == letter]
                
                word_completion_as_list = list(word_completion) # _, _, _, _, _, _
                for i in indices:
                    # Inlocuim underscore-ul cu litera ghicita
                    word_completion_as_list[i] = word_as_list[i]
                
                word_completion = "".join(word_completion_as_list)
                
                if word_completion == word:
                    guessed = True
        elif guess.isalpha():
            if guess in guessed_words:
                print(f"Word '{guess}' already guessed!")
            elif guess == word:
                guessed = True
            elif guess != word:
                print("Not the word!")
                tries -= 1
                guessed_words.append(guess)
        else:
            print("Invalid input!")

    if guessed:
        print("You win!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    print(stages[tries])


play_hangman()

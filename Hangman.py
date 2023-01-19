def Hangman():
    from replit import clear
    import random
    from hangman_words import word_list
    from hangman_art import logo, stages

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

    Failed_Quotes = ["That's not in the word now is it? Lose a life.", 'That is not in the word.', 'Guess what happened to the last person that guessed that?', 'Another life is gone!', 'Careful... your losing', 'Another one bites the dust! -1']

    print(logo)

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        clear()


        if guess in display:
         print(f'You already guessed {guess}, please choose another letter.')
        
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
            
            
        #Check if user is wrong.
        if guess not in chosen_word:

            lives -= 1
            print(random.choice(Failed_Quotes))
            if lives == 0:
                end_of_game = True
                print(f'You lose. The word was {chosen_word}')


        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])

def game():
    import random
    from art import logo
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    def easy():
        num = random.randint(1, 100)

        attempt = 10
        is_over = False
        while is_over == False and attempt > 0:
            print(f"You have {attempt} left")
            guess = int(input("Make a guess: "))

            if guess > num:
                print("Too high.\nGuess again.")
                attempt -= 1
            elif guess < num:
                print("Too low.\nGuess again.")
                attempt -= 1
            elif guess == num:
                print(f"You win. The number is {num}")  
                is_over = True 
        if attempt == 0:
            print(f"You loose. You have {attempt} attempt left.")
            is_over = True
                            
        if is_over == True:
            again = input("Do you want to play again press 'y' or 'n'").lower()
            if again == "y":
                game()
            else:
                is_over == True    
    def hard():
        num = random.randint(1, 100)

        attempt = 5
        is_over = False
        while is_over == False and attempt > 0:
            print(f"You have {attempt} left")
            guess = int(input("Make a guess: "))

            if guess > num:
                print("Too high.\nGuess again.")
                attempt -= 1
            elif guess < num:
                print("Too low.\nGuess again.")
                attempt -= 1
            elif guess == num:
                print(f"You win. The number is {num}")  
                is_over = True 
        if attempt == 0:
            print(f"You loose. You have {attempt} attempt left.")
            is_over = True
                            
        if is_over == True:
            again = input("Do you want to play again press 'y' or 'n'").lower()
            if again == "y":
                game()
            else:
                is_over == True
    
    
    if level == "easy":
        easy()            
    elif level == "hard":
        hard()    
    else:
        print("Ooops you enter something wrong")
        game()


game()        
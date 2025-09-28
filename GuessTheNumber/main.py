import random

player_scores = []

print("GUESS THE NUMBER BETWEEN 1 TO 100".center(85))
players = int(input("Enter the number of players: "))
for i in range(players):
    score = 100
    num = random.randint(1, 100)
    print(f"Player {i+1}:")
    while True:
        guess = int(input("Guess the number: "))
        if score == 0:
            print("You Lost!")
            break
        elif guess == num:
            print(f"You Guessed the number!\nYour Score: {score}")
            break
        elif guess < num:
            print("Try Greater!")
            score -= 10
        else: 
            print("Try Lesser!")
            score -= 10
    player_scores += [score]
    print("-----------------------------------")
    
winning_score = max(player_scores)
winning_player = player_scores.index(winning_score)

print(f"Player {winning_player+1} Wins!\nScore: {winning_score}!")

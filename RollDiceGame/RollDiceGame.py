import random

if __name__ == '__main__':

    def roll():
        max_score = 6
        min_score = 1
        value = random.randint(min_score, max_score)

        return value
    
    while True:
        players = input('input the number of players(2-4): ')
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print('players must be within 2 and 4')
        else: 
            print('Invalid, Entera valid number')

    max_score = 50
    player_score = [0 for _ in range(players)]
    
    while max(player_score) < max_score:

        if max(player_score) > max_score:
            break

        for player_idx in range(players):
            print(f'\nPlayer {player_idx + 1} turn has just started!')
            print(f'your total score is {player_score[player_idx]} \n')

            current_score = 0

            while True:

                should_roll = input('Would you like to roll (y)? ')
                if should_roll.lower() != 'y':
                    break
                else:
                    value = roll()

                if value == 1:
                    print('You rolled 1, Turn done!')
                    current_score = 0
                    break

                else: 
                    current_score += value
                    print(f'you rolled {value}')
                    
                
                print(f'you score is {current_score}')

            player_score[player_idx] += current_score
            print(f'your total score is {player_score[player_idx]}')
    
    print(player_score)
    max_score = max(player_score)
    winning_idx = player_score.index(max_score)
    print(f'Player number {winning_idx + 1} have won the game with score of {max_score}')

import random

if __name__ == '__main__':

    # global variables
    MAX_LINES = 5
    MAX_BET = 1000
    MIN_BET = 10

    #maxlines and rows must be same
    ROWS = 5
    COLS = 3

    symbol_count = {
        'A': 2, 
        'B': 4, 
        'C': 6,
        'D': 8
    }

    symbol_value = {
        'A': 5, 
        'B': 4, 
        'C': 3,
        'D': 2
    }

    def check_winnings(columns, lines, bet, values):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines


    def get_slot_machine_spin(rows, cols, symbols):
        all_symbols = []
        for symbol, count in symbol_count.items():
            for _ in range(count):
                all_symbols.append(symbol)

        columns =[]
        for _ in range(cols):
            column = []
            for _ in range(rows):
                current_symbol = all_symbols[:]
                value = random.choice(current_symbol)
                current_symbol.remove(value)
                column.append(value)

            columns.append(column)

        return columns
    
    def print_slot_machine(columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if  i != len(columns[0]) - 1:
                    print(column[row], end=' | ')
                else:
                    print(column[row], end="")
            print()


    def deposit():
        while True:
            amount = input("Enter Your balance: ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else: 
                    print('Amount must be greater than 0.')
            else: 
                print('Enter a valid amount.')

        return amount
    
    def get_number_of_lines():
        while True:
            lines = input("The number of lines you would like to bet(1-" + str(MAX_LINES) +"): ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else: 
                    print('Enter a valid number.')
            else: 
                print('Enter a number.')

        return lines
    
    def get_bet():
        while True:
            bet_amt = input("The amount you would like to bet: ")
            if bet_amt.isdigit():
                bet_amt = int(bet_amt)
                if MIN_BET <= bet_amt <= MAX_BET:
                    break
                else: 
                    print(f'amount must be between {MIN_BET} amd {MAX_BET}')
            else: 
                print('Enter a number.')

        return bet_amt

    def spin(balance):
        lines = get_number_of_lines()
        
        while True:
            bet = get_bet()
            total_amt = lines * bet
            if total_amt <= balance:
                print(f'You have betted for {lines} lines with an amount of {bet}. The total bet amount is {total_amt}')
                break
            else:
                print(f"You have not enough balance. your current balance is {balance}")
        slot = (get_slot_machine_spin(ROWS, COLS, symbol_count))
        print_slot_machine(slot)
        winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)
        print(f'You won {winnings}')
        print('You won on', *winning_lines)
        return winnings - total_amt

    def main():
        balance = deposit()
        while True:
            if balance < 10:
                print('You did not have enough balance right now!!')
                break
            print(f'Current balance: {balance}')
            answer = input('Press Enter to Play (q to quit) ')
            if answer == 'q':
                break
            balance += spin(balance)

        print(f'You left with {balance}')


    main()



import random
from colorama import Fore, Back, Style
import time

print(f'''
████████████████████████████████████████████████████████
█─▄─▄─█▄─▄█─▄▄▄─███─▄─▄─██▀▄─██─▄▄▄─███─▄─▄─█─▄▄─█▄─▄▄─█
███─████─██─███▀█████─████─▀─██─███▀█████─███─██─██─▄█▀█
▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀
''')

P11 = "1"
P12 = "2"
P13 = "3"
P21 = "4"
P22 = "5"
P23 = "6"
P31 = "7"
P32 = "8"
P33 = "9"
P_list = [P11, P12, P13, P21, P22, P23, P31, P32, P33]
round_count = 0
starting_word = 0
winner_found = False
again_message = "Do you want to start?"

print(f'''
    |    {P_list[0]}    |    {P_list[3]}    |    {P_list[6]}    |
    |    {P_list[1]}    |    {P_list[4]}    |    {P_list[7]}    |
    |    {P_list[2]}    |    {P_list[5]}    |    {P_list[8]}    |
    ''')


def Your_Turn():
    global round_count

    if round_count < 9:
        your_choice = str(input("Select position to put 'X':"))

        if your_choice in P_list:
            P_list[P_list.index(your_choice)] = "X"
            round_count += 1
            print(f"You selected : {your_choice}")
            print(f'''
                |    {P_list[0]}    |    {P_list[3]}    |    {P_list[6]}    |
                |    {P_list[1]}    |    {P_list[4]}    |    {P_list[7]}    |
                |    {P_list[2]}    |    {P_list[5]}    |    {P_list[8]}    |
                ''')
        else:
            print("The position you chose was selected or not existed")
            print("Please select position again")
            print("")
            Your_Turn()


def Computer_Turn():
    global round_count

    if round_count < 9:
        computer_choice = random.randint(0, 8)
        while P_list[computer_choice] == "X" or P_list[computer_choice] == "O":
            computer_choice = random.randint(0, 8)
        P_list[computer_choice] = "O"
        round_count += 1
        print(f"Computer selected : {computer_choice + 1}")
        print(f'''
            |    {P_list[0]}    |    {P_list[3]}    |    {P_list[6]}    |
            |    {P_list[1]}    |    {P_list[4]}    |    {P_list[7]}    |
            |    {P_list[2]}    |    {P_list[5]}    |    {P_list[8]}    |
            ''')


def check():
    global winner_found, round_count

    if P_list[0] == "X" and (P_list[1] == "X" and P_list[2] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    elif P_list[3] == "X" and (P_list[4] == "X" and P_list[5] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    elif P_list[6] == "X" and (P_list[7] == "X" and P_list[8] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    elif P_list[0] == "X" and (P_list[3] == "X" and P_list[6] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    elif P_list[1] == "X" and (P_list[4] == "X" and P_list[7] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    elif P_list[2] == "X" and (P_list[5] == "X" and P_list[8] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    elif P_list[0] == "X" and (P_list[4] == "X" and P_list[8] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    elif P_list[2] == "X" and (P_list[4] == "X" and P_list[6] == "X"):
        print(Fore.GREEN + "You win!\n\n")
        winner_found = True
    else:
        if P_list[0] == "O" and (P_list[1] == "O" and P_list[2] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        elif P_list[3] == "O" and (P_list[4] == "O" and P_list[5] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        elif P_list[6] == "O" and (P_list[7] == "O" and P_list[8] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        elif P_list[0] == "O" and (P_list[3] == "O" and P_list[6] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        elif P_list[1] == "O" and (P_list[4] == "O" and P_list[7] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        elif P_list[2] == "O" and (P_list[5] == "O" and P_list[8] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        elif P_list[0] == "O" and (P_list[4] == "O" and P_list[8] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        elif P_list[2] == "O" and (P_list[4] == "O" and P_list[6] == "O"):
            print(Fore.RED + "You lose!\n\n")
            winner_found = True
        else:
            if round_count == 9:
                print(Fore.CYAN + "Draw!\n\n")
                winner_found = True


while input(f"{Fore.YELLOW}{again_message}").upper() == "Y":
    P_list = [P11, P12, P13, P21, P22, P23, P31, P32, P33]
    round_count = 0
    starting_word = 0
    winner_found = False
    again_message = f"{Fore.BLUE}Rematch?"
    first_player = random.randint(1, 2)

    while round_count <= 9:
        print(Style.RESET_ALL)

        if starting_word == 0:
            if first_player == 1:
                time.sleep(1)
                print("You are 1st player")
                starting_word += 1
            else:
                time.sleep(1)
                print("Computer is 1st player")
                starting_word += 1

        if first_player == 1:
            if winner_found is False:
                Your_Turn()
                time.sleep(1)
                check()
                time.sleep(1)
            else:
                break

            if winner_found is False:
                Computer_Turn()
                time.sleep(1)
                check()
                time.sleep(1)
            else:
                break
        else:
            if winner_found is False:
                Computer_Turn()
                time.sleep(1)
                check()
                time.sleep(1)
            else:
                break

            if winner_found is False:
                Your_Turn()
                time.sleep(1)
                check()
                time.sleep(1)
            else:
                break

print(Style.RESET_ALL)
print("BYE!")





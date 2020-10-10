import time
import random
import sys

# just of effects. add a delay of 1 second before performing any action
sleep_between_action=1
max_val=100
dice_face=6

# snake takes you down from 'key' to 'value'
snakes={8: 4,18: 1,26: 10,39: 5,51: 6,54: 36,56: 1,60: 23,75: 28,83: 45,85: 59,90: 48,92: 25,97: 87,99: 63}

# ladder takes you up from 'key' to 'value'
ladder={3: 20,6: 14,11: 28,15: 34,17: 74,22: 37,38: 59,49: 67,57: 76,61: 78,73: 86,81: 98,88: 91}

player_turn_text = ["Your turn.","Go.","Please proceed.","Lets win this.","Are you ready?","",]

snake_bite = ["boohoo","bummer","snake bite","oh no","dang"]

ladder_jump = ["woohoo","woww","nailed it","oh my God...","yaayyy"]

def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    Version: 1.0.0
    Developed by: Ram Punia

    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.

    """
    print(msg)

def get_player_names():
    player1_name=None
    while not player1_name:
        player1_name=input("enter the valid name for palyer 1: ")
    player2_name=None
    while not player2_name:
        player2_name=input("enter the valid name for player 2: ")
    return player1_name,player2_name

def get_dice_value():
    time.sleep(sleep_between_action)
    dice_value=random.randint(1,dice_face)
    print("its a "+str(dice_value))
    return dice_value

def got_snake_bite(old_value,current_value,player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))

def got_ladder_jump(old_value,current_value,player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a ladder jump. Up from " + str(old_value) + " to " + str(current_value))

def snake_ladder(player_name,current_value,dice_value):
    time.sleep(sleep_between_action)
    old_value=current_value
    current_value=old_value+dice_value
    
    if current_value>max_val:
        print(f"you need {current_value-max_val} to win this game")
        return old_value
    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value=snakes[current_value]
        got_snake_bite(current_value,final_value,player_name)
    
    elif current_value in ladder:
        final_value=ladder[current_value]
        got_ladder_jump(current_value,final_value,player_name)
    else:
        final_value=current_value
    return final_value

def check_win(player_name,position):
    time.sleep(sleep_between_action)
    if max_val==position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        exit()


def start():
    welcome_msg()
    time.sleep(sleep_between_action)
    player1_name,player2_name=get_player_names()
    time.sleep(sleep_between_action)

    player1_current_position=0
    player2_current_position=0
    
    while True:
        time.sleep(sleep_between_action)
        input_1=input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(sleep_between_action)
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name,player1_current_position)


        input_2=input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(sleep_between_action)
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name,player2_current_position)
if __name__=="__main__":
    start()






    










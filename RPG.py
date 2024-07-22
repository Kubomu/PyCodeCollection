# RPG
import time
import random

def print_slow(text, delay=0.03):
    """
    Prints the input text character by character with a delay.

    Args:
        text (str): The text to be printed.
        delay (float, optional): The delay between each character. Defaults to 0.03.

    Example:
        print_slow("Hello, World!")
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def battle():
    """
    Simulates a turn-based battle between the player and an enemy.

    The player can choose to attack or heal. The enemy will attack the player after each turn.
    The battle continues until either the player or the enemy's health reaches 0.

    Example:
        battle()
    """
    enemy_health = 50
    player_health = 50

    print_slow("You encounter an enemy!")
    
    while enemy_health > 0 and player_health > 0:
        print_slow("\nYour Health: {}".format(player_health))
        print_slow("Enemy Health: {}".format(enemy_health))
        
        action = input("\nWhat will you do? (attack/heal): ").lower()

        if action == "attack":
            damage = random.randint(5, 15)
            enemy_health -= damage
            print_slow("You deal {} damage to the enemy!".format(damage))
        elif action == "heal":
            healing = random.randint(10, 20)
            player_health += healing
            print_slow("You heal yourself for {} health points.".format(healing))
        else:
            print_slow("Invalid action. Try again.")

        # Enemy's turn
        enemy_damage = random.randint(3, 10)
        player_health -= enemy_damage
        print_slow("The enemy attacks and deals {} damage to you!".format(enemy_damage))

    if player_health > 0:
        print_slow("\nYou defeated the enemy! Your final health: {}".format(player_health))
    else:
        print_slow("\nYou were defeated by the enemy. Game over.")

# Run the RPG battle
battle()
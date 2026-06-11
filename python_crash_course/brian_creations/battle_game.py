#Brian Saville
#June 11, 2026
#Toying around and making a little RPG game.
import random

#set values
player_health = 100
beast_health = 300
player_mp = 50
defend = False

player_attack = 30
attack_modifier = 0
beast_attack = 30

print("You are a wandering traveler on a quest.")
print("Suddenly, a beast attacks!")
print("\nLet the battle begin!")

#player turn
while beast_health > 0:
    print("\nYour HP: " + str(player_health))
    print("Your MP: " + str(player_mp))
    print("What will you do? Type your command.")
    choice = input("Options: [Attack] [Defend] [Magic] [Heal] ")

    #reset variables
    defend = False

    #PLAYER TURN

    #Attack
    if choice.lower() == "attack":
        print("\nYou attack the beast!")

        #calculate damage modifier
        attack_modifier = random.randrange(-10, 10)
        player_damage = player_attack + attack_modifier

        attack_rng = random.randrange(1, 20)
        #critical hit
        if attack_rng == 20:
            player_damage = player_damage * 2
            print("Wow! A critical hit!")
            print("The beast takes " + str(player_damage) + " damage!")
            beast_health = beast_health - player_damage

        #missed attack
        elif attack_rng == 1:
            print("Whoops! Your attack missed.")

        #standard attack
        else:
            print("The beast takes " + str(player_damage) + " damage!")
            beast_health = beast_health - player_damage

    #Defend
    elif choice.lower() == "defend":
        print("\nYou assume a denfesive stance!")
        defend = True

    #Magic
    elif choice.lower() == "magic":
        print("\nYou use a fire spell on the beast!")

        #Determine whether the fire attack lands
        magic_hit = random.randrange(1,9)
        
        #magic hit
        if magic_hit > 3:
            magic_damage = random.randrange(50, 65)
            print("The beast takes " + str(magic_damage) + " damage!")
        #magic miss
        else:
            print("The flames narrowly miss the beast!")
        player_mp -= 10


    #Heal
    elif choice.lower() == "heal":
        print("\nYou use a healing spell on yourself!")
        heal_amount = random.randrange(40, 55)

        if player_health == 100:
            print("... but you are already at full health!")
        elif player_health + heal_amount > 100:
            heal_amount = 100 - player_health
            print("You recover " + str(heal_amount) + " HP." )
            player_health = 100
        else: 
            player_health = player_health + heal_amount
            print("You recover " + str(heal_amount) + " HP." )

    #Run
    elif choice.lower() == "run" or "flee" or "escape":
        print("\nNice try, but there's no running from this fight!")

    #Invalid input
    else:
        print("Invalid command! Your loss.")
        break

    #BEAST TURN
    #end the fight if the beast has been defeated
    if beast_health <= 0:
        break

    #roll to determine what the beast will do.
    #1-4: normal attack
    #5-6: big attack
    #7: gear up for finisher.
    #8: nothing
    beast_action = random. randrange(1, 8)

    #beast normal attack
    if beast_action > 0:
        print("\nThe beast attacks with fierce claws!")
        attack_modifier = random.randrange(-10, 10)
        beast_damage = beast_attack + attack_modifier
        print("You take " + str(beast_damage) + " hit points of damage!")
        player_health = player_health - beast_damage





#Beast is defeated
print("\nThe beast admits defeat!")
print("\n--- YOU WIN! ---\n")
print("You earned 6942067 experience points.")
            



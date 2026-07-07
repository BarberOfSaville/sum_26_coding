#Brian Saville
#June 11, 2026
#Toying around and making a little RPG game.
import random

#SET PARAMETERS

#HP and MP
player_health = 100
beast_health = 300
player_mp = 50
defend = False

#attack parameters
player_attack = 30
attack_modifier = 0
p_modifier_upper_limit = 15
p_modifier_lower_limit = -5

#magic parameters
magic_upper_limit = 65
magic_lower_limit = 50
magic_cost = 5

#heal parameters
heal_lower_limit = 80
heal_upper_limit = 100
heal_cost = 3

#beast parameters
beast_attack = 30
b_modifier_upper_limit = 10
b_modifier_lower_limit = -10
beast_finisher = False

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
        attack_modifier = random.randrange(p_modifier_lower_limit, p_modifier_upper_limit)
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
        magic_hit = random.randrange(1,10)
        
        #magic hit
        if magic_hit > 2:
            magic_damage = random.randrange(magic_lower_limit, magic_upper_limit)
            print("The beast takes " + str(magic_damage) + " damage!")
        #magic miss
        else:
            print("The flames narrowly miss the beast!")
        player_mp -= magic_cost


    #Heal
    elif choice.lower() == "heal":
        print("\nYou use a healing spell on yourself!")
        heal_amount = random.randrange(heal_lower_limit, heal_upper_limit)

        if player_health == 100:
            print("... but you are already at full health!")
        elif player_health + heal_amount > 100:
            heal_amount = 100 - player_health
            print("You recover " + str(heal_amount) + " HP." )
            player_health = 100
        else: 
            player_health = player_health + heal_amount
            print("You recover " + str(heal_amount) + " HP." )
        player_mp -= heal_cost

    #Run
    elif choice.lower() == "run" or "flee" or "escape":
        print("\nNice try, but there's no running from this fight!")

    #Invalid input
    else:
        print("Invalid command! Your loss.")

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

    #beast finisher attack
    if beast_finisher == True:
        print("\nThe beast launches a deadly onslaught!")
        if defend == True:
            beast_damage = 20
        else:
            beast_damage = 85
        print("You take " + str(beast_damage) + " hit points of damage!")
        
        if defend == True:
            print("Good thing you defended yourself!")
        else:
            print("Yowch! That's going to leave a mark!")
        player_health = player_health - beast_damage
        beast_finisher = False

    else:
        #beast normal attack
        if beast_action <= 4:
            print("\nThe beast attacks with fierce claws!")
            beast_modifier = random.randrange(b_modifier_lower_limit, b_modifier_upper_limit)
            beast_damage = beast_attack + beast_modifier

            #reduce damage if the player defended
            if defend == True:
                beast_damage = round(beast_damage / 2)

            print("You take " + str(beast_damage) + " hit points of damage!")
            player_health = player_health - beast_damage

        #beast big attack
        elif beast_action <= 6:
            print("\nThe beast takes a vicious bite!")
            beast_modifier = random.randrange(b_modifier_lower_limit, b_modifier_upper_limit)
            beast_damage = round((beast_attack + beast_modifier) * 1.3)

            #reduce damage if the player defended
            if defend == True:
                beast_damage = round(beast_damage / 2)

            print("You take " + str(beast_damage) + " hit points of damage!")
            player_health = player_health - beast_damage

        #beast gear up for finisher
        elif beast_action == 7:
            print("\nThe beast is gearing up for a deadly attack! Better defend!")
            beast_finisher = True

        #beast do nothing
        elif beast_action == 8:
            print("\nThe beast is staring absentmindedly.")



    #end the fight if the player is defeated
    if player_health <= 0:
        print("\nYou are out of HP!")
        print("You black out...")
        print("\n---GAME OVER---\n")
        print("We hope you try again!")
        exit()





#Beast is defeated
print("\nThe beast admits defeat!")
print("\n--- YOU WIN! ---\n")
print("You earned 6942067 experience points.")
            



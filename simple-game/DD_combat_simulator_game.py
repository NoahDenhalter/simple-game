import random
import numbers
import combat_messages

def main() :

    potion_compounding_effect = 1
    roll_for_twenty = 1
    ceiling_collapsed = False
    turkey = 5
    turn_tracker = 0


    #sigh... dictionaries are efficient
    characters = {
        "player": {
            "health" : 20,
            "damage" : {
                "light" : 1,
                "big" : 2,
                "lucky" : 10
            }
        },
        "enemy" : {
            "health" : 10,
            "damage" : {
                "light" : 1,
                "big" : 2,
                "huge" : 5
            }
        }
    }

    #this is literally just for double knick
    names = list(characters)

    combat_messages.intro(characters["player"]["health"], characters["enemy"]["health"])

    while characters["player"]["health"] > 0 and characters["enemy"]["health"] > 0 :
        
        #D20 simulator
        roll_for_twenty = random.randint(1, 20)
        
        #For victory flavor 
        turn_tracker += 1

        print(roll_for_twenty)
        if (roll_for_twenty == 1):

            print(f"Oof! Critical fail, you take {characters["enemy"]["damage"]["huge"]} damage!")

            #Way too much work for a rare mechanic
            if (characters["player"]["health"] > 0) :
                print(f"Uh-oh, what's that strange potion the enemy is drinking?")

                characters["player"]["health"] = numbers.take_damage(characters["player"]["health"], characters["enemy"]["damage"]["huge"])

                #increases each method of damage
                for pain in characters["enemy"]["damage"]:
                    characters["enemy"]["damage"][pain] = numbers.engine_increase(characters["enemy"]["damage"][pain], potion_compounding_effect)

                #potion gets stronger and heals enemy for decent amount at early levels
                potion_compounding_effect, characters["enemy"]["health"] = numbers.strange_potion(potion_compounding_effect, characters["enemy"]["health"])

            combat_messages.still_alive(characters["player"]["health"], characters["enemy"]["health"])
            

        elif roll_for_twenty > 1 and roll_for_twenty < 5 :

            print(f"That smarts! You take {characters["enemy"]["damage"]["big"]} damage!")

            characters["player"]["health"] = numbers.take_damage(characters["player"]["health"], characters["enemy"]["damage"]["big"])

            combat_messages.still_alive(characters["player"]["health"], characters["enemy"]["health"])
            

        elif roll_for_twenty >= 5 and roll_for_twenty < 10 :
            print(f"Ouch! You take {characters["enemy"]["damage"]["light"]} damage")

            characters["player"]["health"] = numbers.take_damage(characters["player"]["health"], characters["enemy"]["damage"]["light"])

            combat_messages.still_alive(characters["player"]["health"], characters["enemy"]["health"])
            
        #Double knick is 1 when enemy damage is 1
        elif roll_for_twenty == 10 and characters["enemy"]["damage"]["light"] == 1:
            print(f"Double knick, you both take 1 damage!")

            for character in characters :
                characters[character]["health"] = numbers.take_damage(characters[character]["health"], 1)

            combat_messages.still_alive(characters["player"]["health"], characters["enemy"]["health"])

        #Double knick remains accurate as enemy strength increases
        elif roll_for_twenty == 10 and characters["enemy"]["damage"]["light"] != 1:
            print(f"Double knick, you deal 1 damage and take {characters["enemy"]["damage"]["light"]} damage!")

            for i in range(len(names)) :
                attacker = names[i]
                target = names[(i + 1) % len(characters)]
                
                characters[target]["health"] = numbers.take_damage(characters[target]["health"], characters[attacker]["damage"]["light"])

            combat_messages.still_alive(characters["player"]["health"], characters["enemy"]["health"])
            

        elif roll_for_twenty > 10 and roll_for_twenty < 16 :
            print(f"Nice Shot! You deal 1 damage!")

            characters["enemy"]["health"] = numbers.take_damage(characters["enemy"]["health"], 1)

            combat_messages.still_alive(characters["player"]["health"], characters["enemy"]["health"])
            
        #Healing always seems more fun to me than increased damage
        elif roll_for_twenty >= 16 and roll_for_twenty < 20 :
            print(f"Life Sap!! Deal 2 damage and heal for 1!")

            characters["player"]["health"] = numbers.heal(characters["player"]["health"], 1)
            characters["enemy"]["health"] = numbers.take_damage(characters["enemy"]["health"], 2)

            combat_messages.still_alive(characters["player"]["health"], characters["enemy"]["health"])
            

        #Ceiling collapse one-time event, auto-win without additional enemy health
        elif roll_for_twenty == 20 and ceiling_collapsed == False :
            print(f"You clip a pillar and the roof collapses on the enemy!")

            ceiling_collapsed = True
            characters["enemy"]["health"] = numbers.take_damage(characters["enemy"]["health"], 10)

            if characters["enemy"]["health"] < 1 :
                print(f"...")

            else :
                combat_messages.wellness_check(characters["player"]["health"], characters["enemy"]["health"])
            
        #Dealing 10 damage every time seems overkill, a big heal leads to a longer game
        #If you already rolled a 20 you should be winning anyway
        else :
            print(f"You find a whole freshly cooked turkey!! Heal for {turkey}!")
            print()
            
            characters["player"]["health"] = numbers.heal(characters["player"]["health"], turkey)
            turkey = numbers.engine_increase(turkey, (turkey - 4))
        
    
    combat_messages.game_end(characters["player"]["health"], characters["enemy"]["health"], roll_for_twenty, turn_tracker)
    
if __name__ == "__main__":
    main()
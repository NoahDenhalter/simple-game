#DD_combat_simulator_game.py

import random
import numbers as n
import combat_messages as m
import shorthand as s
from game_data import characters

def main() :

    import variables as v


    #sigh... dictionaries are efficient

    #this is literally just for double knick
    names = list(characters)

    m.intro()

    while s.combat_active():
        
        #D20 simulator
        roll = random.randint(1, 20)
        
        #For victory flavor 
        v.turn_tracker += 1

        print(roll)
        if s.critical_fail(roll):

            print(f"Oof! Critical fail, you take {s.huge_attack()} damage!")

            #Way too much work for a rare mechanic
            if s.player_alive() :
                print(f"Uh-oh, what's that strange potion the enemy is drinking?")

                n.get_hit(s.huge_attack())

                #increases each method of damage
                for pain in characters["enemy"]["damage"]:
                    characters["enemy"]["damage"][pain] += v.elixir

                #potion gets stronger and heals enemy for decent amount at early levels
                v.elixir = n.strange_potion(v.elixir)

            m.still_alive()
            

        elif s.low_roll(roll) :

            print(f"That smarts! You take {s.big_attack()} damage!")

            n.get_hit(s.big_attack())

            m.still_alive()
            

        elif s.mid_low_roll(roll) :
            print(f"Ouch! You take {s.small_attack()} damage")

            n.get_hit(s.small_attack())

            m.still_alive()
            
        #Double knick is 1 when enemy damage is 1
        elif s.mid_roll(roll) and s.small_attack() == 1:
            print(f"Double knick, you both take 1 damage!")

            for character in characters :
                characters[character]["health"] -= 1

            m.still_alive()

        #Double knick remains accurate as enemy strength increases
        elif s.mid_roll(roll) and s.small_attack() != 1:
            print(f"Double knick, you deal 1 damage and take {s.small_attack()} damage!")

            for i in range(len(names)) :
                attacker = names[i]
                target = names[(i + 1) % len(characters)]
                
                characters[target]["health"] -= characters[attacker]["damage"]["light"]

            m.still_alive()
            

        elif s.mid_high_roll(roll) :
            print(f"Nice Shot! You deal 1 damage!")

            n.deal_damage(s.small_strike())

            m.still_alive()
            
        #Healing always seems more fun to me than increased damage
        elif s.high_roll(roll) :
            print(f"Life Sap!! Deal 2 damage and heal for 1!")

            n.hero_heal(s.big_strike() // 2)
            n.deal_damage(s.big_strike())

            m.still_alive()
            

        #Ceiling collapse one-time event, auto-win without additional enemy health
        elif s.critical_success(roll) and v.ceiling_collapsed == False :
            print(f"You clip a pillar and the roof collapses on the enemy!")

            v.ceiling_collapsed = True
            n.deal_damage(s.lucky_strike())

            if characters["enemy"]["health"] < 1 :
                print(f"...")

            else :
                m.wellness_check()
            
        #Dealing 10 damage every time seems overkill, a big heal leads to a longer game
        #If you already rolled a 20 you should be winning anyway
        else :
            print(f"You find a whole freshly cooked turkey!! Heal for {v.turkey}!")
            print()
            
            n.hero_heal(v.turkey)
            v.turkey += (v.turkey - 4)
        
    
    m.game_end(roll, v.turn_tracker)
    
if __name__ == "__main__":
    main()
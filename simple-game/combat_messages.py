#combat_messages.py
import shorthand as s


def intro():
    print()
    print(f"Let's speedrun some D&D combat!")
    print()
    print(f"Your health is at {s.hero()} and the enemy is at {s.villain()}")
    print()

def wellness_check():
    print(f"Now your health is at {s.hero()} and the enemy's health is at {s.villain()}!")
    print()

def still_alive():
    if s.player_alive() and s.enemy_alive() :
        wellness_check()

def game_end(rolls, turns):
    if s.hero() < 1 and s.villain() < 1 :
            print()
            print(f"You defeated the enemy! But as you stumble back, you realize you've been dealt a mortal blow yourself. Your vision slowly fades, and you realize it was all for naught.")
            print(f"Better luck next time!")
            print()

    elif s.enemy_alive() :
            print()
            print(f"Your enemy stands above you as you bleed out on the floor. With a smile, he lifts a large rock above his head. \"Goodbye, worthless hero\", he smirks, and slams the rock down on your head.")
            print(f"Ouch! That had to hurt. Try again?")
            print()

    elif s.player_alive() and s.not_critical_success(rolls) and s.short_time(turns) :
            print()
            print(f"You did it without a sweat, well done!")
            print(f"Play again?")
            print()
    
    elif s.player_alive() and s.not_critical_success(rolls) and s.awhile(turns) :
            print()
            print(f"You did it!! A hard won victory, well done!")
            print(f"Play again?")
            print()
    
    elif s.player_alive() and s.not_critical_success(rolls) and s.long_time(turns) :
            print()
            print(f"You did it!! What a slog, well done!!!")
            print(f"Play again?")
            print()  
    
    elif s.player_alive() and s.critical_success(rolls) and s.not_short_time(turns) :
            print()
            print(f"Wow!! You did it! But what a lame end after all that work...")
            print(f"Maybe you should try again? Win for real this time?")
            print()
    
    elif s.player_alive() and s.critical_success(rolls) and s.short_time(turns) :
            print()
            print(f"Wow!! You did it! But you did get kind of lucky, not much credit for you on this win, is there?")
            print(f"Maybe you should try again? Win for real this time?")
            print()
    
    elif s.player_alive() and s.critical_success(rolls) and s.one(turns) :
            print()
            print(f"Wow, that was easy!! What a baby game!")
            print(f"You did get really lucky though, not much credit for you on this win, is there?")
            print(f"Maybe you should try again? Win for real this time?")
            print()
    
    else :
            print()
            print(f"Oops, how did you get here?? uhhh.... leave please? I have to fix the code now")
            print()
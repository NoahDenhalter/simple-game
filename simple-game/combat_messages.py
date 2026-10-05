def intro(yours, theirs):
    print()
    print(f"Let's speedrun some D&D combat!")
    print()
    print(f"Your health is at {yours} and the enemy is at {theirs}")
    print()

def wellness_check(yours, theirs):
    print(f"Now your health is at {yours} and the enemy's health is at {theirs}!")
    print()

def still_alive(yours, theirs):
    if yours > 0 and theirs > 0 :
        wellness_check(yours, theirs)

def game_end(yours, theirs, rolls, turns):
    if yours < 1 and theirs < 1 :
            print()
            print(f"You defeated the enemy! But as you stumble back, you realize you've been dealt a mortal blow yourself. Your vision slowly fades, and you realize it was all for naught.")
            print(f"Better luck next time!")
            print()
    
    elif yours > 1 and theirs < 1 and rolls != 20 and turns <= 5 :
            print()
            print(f"You did it without a sweat, well done!")
            print(f"Play again?")
            print()
    
    elif yours > 1 and theirs < 1 and rolls != 20 and 5 < turns <= 15 :
            print()
            print(f"You did it!! A hard won victory, well done!")
            print(f"Play again?")
            print()
    
    elif yours > 1 and theirs < 1 and rolls != 20 and turns > 15 :
            print()
            print(f"You did it!! What a slog, well done!!!")
            print(f"Play again?")
            print()
    
    elif yours < 1 and theirs > 1 :
            print()
            print(f"Your enemy stands above you as you bleed out on the floor. With a smile, he lifts a large rock above his head. \"Goodbye, worthless hero\", he smirks, and slams the rock down on your head.")
            print(f"Ouch! That had to hurt. Try again?")
            print()
    
    elif yours > 1 and rolls == 20 and turns > 5 :
            print()
            print(f"Wow!! You did it! But what a lame end after all that work...")
            print(f"Maybe you should try again? Win for real this time?")
            print()
    
    elif yours > 1 and rolls == 20 and 1 < turns <= 5 :
            print()
            print(f"Wow!! You did it! But you did get kind of lucky, not much credit for you on this win, is there?")
            print(f"Maybe you should try again? Win for real this time?")
            print()
    
    elif yours > 1 and rolls == 20 and turns == 1 :
            print()
            print(f"Wow, that was easy!! What a baby game!")
            print(f"You did get really lucky though, not much credit for you on this win, is there?")
            print(f"Maybe you should try again? Win for real this time?")
            print()
    
    else :
            print()
            print(f"Oops, how did you get here?? uhhh.... leave please? I have to fix the code now")
            print()
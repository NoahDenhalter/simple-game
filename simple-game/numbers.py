#numbers.py
from game_data import characters

#multi-use variable increase
def engine_increase(engine, increment):
    engine += increment
    return engine

#potion gets stronger and heals enemy
def strange_potion(potion): 
    if potion > 2 :
            enemy_heal(potion)
    else :
            enemy_heal(potion + 2)
                
    potion *= 2
    return potion

#character specific damage shorthand
def get_hit(ouch):
    characters["player"]["health"] -= ouch

def deal_damage(ouch):
    characters["enemy"]["health"] -= ouch

#character specific healing shorthand
def enemy_heal(amount):
    characters["enemy"]["health"] += amount

def hero_heal(amount):
    characters["player"]["health"] += amount
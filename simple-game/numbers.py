#multi-use variable increase
def engine_increase(engine, increment):
    engine += increment
    return engine

#multi-use health decrease
def take_damage(health, hurt):
    health -= hurt
    return health

#multi-use health increase
def heal(health, heal_amount):
    health += heal_amount
    return health

#potion gets stronger and heals enemy
def strange_potion(potion, health): 
    if potion > 2 :
            health += potion
    else :
            health += (potion + 2)
                
    potion *= 2
    return potion, health
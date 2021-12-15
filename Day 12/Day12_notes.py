################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local scope
def drink_potion():
    potion_strength=2
    print(potion_strength)

drink_potion()
#print(potion_strength) This does not work as potion_strength is not existing outside

#global scope
player_health = 10

def game():
    def drink_potion2():
        potion_strength =2
        print(player_health)
    drink_potion2()

#drink_potion2() does also not work

game_level = 5
enemies = ["Skeleton","Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # Works as its not a new scope in python

def create_enemy():
    if game_level < 5:
        new_enemy2 = enemies[1]

#print(new_enemy2) does also not work

# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

#text based game
# core game mechanics
    #be able to enter rooms, fight enemies, pick up items, use items, win when all enimies are dead
import random
gameData = {"rooms":{"Entrance":[], "Hall":[], "Armoury":[], "Bedroom":[], "Kitchen":[], "Exit":[]},
            "Items":["Sword", "Potion", "Gold", "Shield", "Gun"], 
            "PlayerState":{"inventory":[], "PlayerHealth":100,},
            "Stats":{"TotalDamageD":0, "TotalDamageL":0, "TotalHeald":0, "EnemiesKlld":0, "itemsLooted":0}
            }

# initialise each room to have a random item and choice of enemy
def setupGame(gameData): 
    for room in gameData["rooms"]:
        room["enemy"] = random.choice([True, False])
        room["item"] = random.choice(gameData["items"])
        gameData["items"].remove(room["item"])

    for room in gameData["rooms"]:
        print(f"room:", room, "item:", room["item"], "enemy:", room["enemy"])

setupGame(gameData)
         




def main(gameData): # main code will run here
    ...
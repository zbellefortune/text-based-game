#text based game
# core game mechanics
    #be able to enter rooms, fight enemies, pick up items, use items, win when all enimies are dead
import random
import time
gameData = {"rooms":{"Entrance":{"number":1, }, "Hall":{"number":2, }, "Armoury":{"number":3, }, "Bedroom":{"number":4, }, "Kitchen":{"number":5, }, "Exit":{"number":6, }},
            "items":["Sword", "Potion", "Gold", "Shield", "Gun", "placeholder"], 
            "PlayerState":{"inventory":[], "PlayerHealth":100, "curRoom":"Entrance"},
            "Stats":{"TotalDamageD":0, "TotalDamageL":0, "TotalHeald":0, "EnemiesKlld":0, "itemsLooted":0}
            }
# initialise each room to have a random item and choice of enemy
def setupGame(gameData): 
    for room in gameData["rooms"].values():
        room["enemy"] = random.choice([True, False])
        room["item"] = random.choice(gameData["items"])
        gameData["items"].remove(room["item"])

    for name, room in gameData["rooms"].items():
        print("room:", name, "item:", room["item"], "enemy:", room["enemy"])

# menu gives user a choice to pick an option of what they can do
def menu():
    while True:
        print("---Options---")
        print("1. Move")
        print("2. Check inventory")
        print("3. Search Room")
        print("4. Save/Load")
        print("5. Exit")
        choice = input("... ").strip()
        if choice in ["1","2","3","4","5"]:
            return choice
        else:
            print("pick an option 1 - 5")
            time.sleep(1)


def move(gameData):
    while True:
    # changes the players current room and is saved and returnd in game data
        print(f"You are in the {gameData["PlayerState"]["curRoom"]}")
        print("--Pick a room--")
        for room in gameData["rooms"]:
            if room == gameData["PlayerState"]["curRoom"]:
                print(end = "")
            else:
                print(f"{gameData['rooms'][room]['number']}. {room}")
        choice = input("...").strip()
        for name, room in gameData["rooms"].items():
            if str(room["number"]) == choice and name != gameData["PlayerState"]["curRoom"]:
                gameData["PlayerState"]["curRoom"] = name
                print(f"You moved to the {name}")
                return
        print("Invalid choice")
        time.sleep(1)
def checkInv(gameData):
    print("--Inventory--")
    x = 0
    for item in gameData["PlayerState"]["inventory"]:
        x += 1
        print(f"{x}. {item}")

def searchRoom(gameData):
    ...
def save(gameData):
    ...
def load(gameData):
    ...    

def main(gameData): # main code will run here
    setupGame(gameData)
    choice = int(menu())

    if choice == 1:
        move()
    elif choice == 2:
        checkInv()
    elif choice == 3:
        searchRoom()
    elif choice == 4:
        # save or load
        ...
    elif choice == 5:
        # exit 
        ...
    else:
        raise ValueError("somethings wrong")
menu()
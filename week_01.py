
player_name = input("Wat is je naam? ")
player_gold = 100
inventory = []

print("Welkom", player_name)
print("Je hebt", player_gold, "gold.")


items = ["Sword", "Shield", "Potion", "Bow"]

for item in items:
    print(item)



while True:
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    keuze = input("What would you like to do? ")

    match keuze:
        case "1":
            if player_gold >= 50:
                player_gold -= 50
                inventory.append("Sword")
                print("Sword gekocht!")
                print("Gold over:", player_gold)
            else:
                print("Niet genoeg gold!")

        case "2":
            if player_gold >= 40:
                player_gold -= 40
                inventory.append("Shield")
                print("Shield gekocht!")
                print("Gold over:", player_gold)
            else:
                print("Niet genoeg gold!")

        case "3":
            if player_gold >= 20:
                player_gold -= 20
                inventory.append("Potion")
                print("Potion gekocht!")
                print("Gold over:", player_gold)
            else:
                print("Niet genoeg gold!")

        case "4":
            if player_gold >= 60:
                player_gold -= 60
                inventory.append("Bow")
                print("Bow gekocht!")
                print("Gold over:", player_gold)
            else:
                print("Niet genoeg gold!")


        case "5":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("Your inventory:")
                for item in inventory:
                    print(item)

        case "6":
           

       
            print("Thanks for visiting,", player_name + "!")
            print("You have", player_gold, "gold left.")
            break

        case _:
            print("Invalid option! Try again.")

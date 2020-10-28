from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n\n")
print("NAME           HP                            MP")

print("                 _________________________     __________")
print("Valos: 460/460   |                        |    |         |")

print("                 _________________________     __________")
print("Valos: 460/460   |                        |    |         |")

# Create Black Magic
fire = Spell("Fire", 10, 100, "Black Magic")
thunder = Spell("Thunder", 10, 100, "Black Magic")
blizzard = Spell("Blizzard", 10, 100, "Black Magic")
meteor = Spell("Meteor", 20, 200, "Black Magic")
quake = Spell("Quake", 14, 140, "Black Magic")

# Create White Magic
cure = Spell("Cure", 12, 120, "White Magic")
cura = Spell("Cura", 18, 200, "White magic")

# Create Items
potion = Item("Potion", "potion", "Heals 50HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500HP", 500)
elixer = Item("Elixer", "elixir", "Fully restores HP/HP of one party member", 9999)
hielixer = Item("MegaElixer", "elixir", "Fully restores party's HP/MP", 9999)

granade = Item ("Granade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"items": potion, "quantity": 15},
                {"items": hipotion, "quantity": 5},
                {"items": superpotion, "quantity": 5},
                {"items": elixer, "quantity": 5},
                {"items": hielixer, "quantity": 2},
                {"items": granade, "quantity": 5}]

# Instant Players
player = Person("Valos: ", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Nick: ", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot: ", 460, 65, 60, 34, player_spells, player_items)

enemy = Person(1200, 65, 45, 25, [], [])

players = [player, player2, player3]

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "An enemy attacked" + bcolors.ENDC)

while running:
    print("============")
    player.choose_action()
    choice = input("Choose actions: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" +spell.name + " heals for ", str(magic_dmg), +"HP." +bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" +spell.name+ "deals", str(magic_dmg), "points of damage" +bcolors.ENDC)
    elif index == 2:
        player.choose_items()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]["items"]

        if player_items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            continue

        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "Elixer":
            player.hp = player.mahhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN +"\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL+ "\n" + item.name + " deals", str(item.prop), "points of damage" +bcolors.EDNC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemmy attacks for", enemy_dmg)

    print("-----------------------------------------")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("You MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" +bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
# ModuleSixMilestone.py
# Jaden Knotts

# A dictionary for the "Defeat the Dragon" game
# The dictionary links a room to other rooms and includes items in each room.
rooms = {
    'Castle Courtyard': {'South': 'Dark Forest', 'Item': None},
    'Dark Forest': {'North': 'Castle Courtyard', 'South': 'Ancient Ruins', 'Item': 'Bow and Arrows'},
    'Ancient Ruins': {'North': 'Dark Forest', 'South': 'Enchanted Castle', 'Item': 'Amulet of Power'},
    'Enchanted Castle': {'North': 'Ancient Ruins', 'South': 'Dragon\'s Lair', 'Item': 'Magic Wand'},
    'Dragon\'s Lair': {'North': 'Enchanted Castle', 'South': 'Dragon\'s Nest', 'Item': None},
    'Dragon\'s Nest': {'North': 'Dragon\'s Lair', 'Item': 'Dragon Egg'}
}


# Function to display the current room and its contents
def display_current_room(current_room, inventory):
    print(f'You are in the {current_room}.')
    if rooms[current_room]['Item'] is not None and rooms[current_room]['Item'] not in inventory:
        print(f'You see a {rooms[current_room]["Item"]} here.')
    else:
        print('There is nothing of interest here.')


# Function to handle player movement
def move_player(current_room, direction):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print('You can\'t go that way.')
        return current_room


def main():
    # Starting room
    current_room = 'Castle Courtyard'
    # Player inventory
    inventory = []

    # Gameplay loop
    while current_room != 'exit':
        # Display current room and its contents
        display_current_room(current_room, inventory)

        # Prompt player for a command
        command = input('Enter your move (North, South) or type "exit" to quit: ').strip().capitalize()

        # Handle move commands
        if command.lower() == 'exit':
            current_room = 'exit'
        elif command in ['North', 'South']:
            current_room = move_player(current_room, command)
        elif command.lower() == 'take':
            if rooms[current_room]['Item'] is not None and rooms[current_room]['Item'] not in inventory:
                inventory.append(rooms[current_room]['Item'])
                print(f'You have taken the {rooms[current_room]["Item"]}.')
            else:
                print('There is nothing to take.')
        else:
            print('Invalid command. Try again.')

    print('Thank you for playing!')


# Run the main function to start the game
if __name__ == "__main__":
    main()

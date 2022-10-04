
from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys


def read_paths(source):
	"""Returns a list of lists according to the specifications in a config file, (source).
	source contains path specifications of the form:
	origin > direction > destination.
	read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""
	f = open(source, "r")
	_path = f.readlines()
	if _path == []:
		raise ValueError("No rooms exist! Exiting program...")
	f.close
	i=0
	while i < len(_path):
		_path[i]=_path[i].strip().split(" > ")
		i+=1
	return _path
	

	
def create_rooms(_path):
	"""Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""
	room_list = []
	for i in range(len(_path)):
		room_list.append(_path[i][0])
		room_list.append(_path[i][2])
	room_list = list(dict.fromkeys(room_list)) #how to remove duplicates i think?
	rooms = []
	for i in range(len(room_list)):
		rooms.append(Room(room_list[i])) # adds room objects to list
		
	for i in range(len(_path)):	# now we need to add destinations to the room objects in the list rooms
		for j in range(len(rooms)): #room to the classy room
			if _path[i][0] == rooms[j].name:	
				room = j
		for k in range(len(rooms)): #paring up adjoining room to classy room
			if _path[i][2] == rooms[k].name:
				dest = k
		rooms[room].set_path(_path[i][1], rooms[dest]) # room > direction > class of room
	return rooms


def generate_items(source):
	"""Returns a list of items according to the specifications in a config file, (source).

	source contains item specifications of the form:
	item name | shortname | skill bonus | will bonus
	"""
	f=open(source,"r")
	item = f.readlines()
	f.close()
	i = 0
	while i < len(item):
		item[i] = item[i].strip().split(' | ')
		i += 1
	items = []
	for i in range(len(item)):
		items.append(Item(item[i][0], item[i][1], int(item[i][2]), int(item[i][3])))
	return items



def generate_quests(source, items, rooms):
	"""Returns a list of quests according to the specifications in a config file, (source).

	source contains quest specifications of the form:
	reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	"""
	
	f = open(source, "r") # opening source
	quest = f.readlines()
	f.close()# closing
	quest_list = []
	i = 0
	while i < len(quest): # appending the quests to a list
		quest[i] = quest[i].strip()
		if quest[i] != '':
			quest_list.append(quest[i])
			i += 1
		else:
			i += 1
	aa = 0
	while aa < len(quest_list): # the number of quests split from the |
		quest_list[aa] = quest_list[aa].split(' | ')
		aa += 1
	quests = []
	for i in range(len(quest_list)):
		for j in range(len(rooms)):
			if rooms[j].name == quest_list[i][8]: 
				room = j
		for k in range(len(items)):
			if items[k].name == quest_list[i][0]:
				item = k
		quests.append(Quest(items[item], quest_list[i][1],quest_list[i][2],quest_list[i][3],quest_list[i][4],quest_list[i][5],quest_list[i][6],quest_list[i][7],quest_list[i][8]))
		rooms[room].quest = quests[i]
	return quests


# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.


# TODO: Receive commands from standard input and act appropriately.

if len(sys.argv) < 4:
	exit("Usage: python3 simulation.py <paths> <items> <quests>")
try:
	_path = read_paths(sys.argv[1])
	_rooms = create_rooms(_path) 
	_item = generate_items(sys.argv[2])
	_quest = generate_quests(sys.argv[3], _item, _rooms)

except ValueError as be:
	print(be)
	exit()
except BaseException as be:
	exit("Please specify a valid configuration file.")
	

player = Adventurer()

current_room=_rooms[0]
current_room.draw()
completion = False
if completion != False:
	print("=== All quests complete! Congratulations! ===")
	exit()
while True:
	print()
	command = input(">>> ").upper()
	
	if current_room.quest != None:
		if command == current_room.quest.action:
			current_room.quest.attempt(player)
			command = "SKIP"
	if command == "SKIP":
		pass
	elif command == "HELP":
		print("""HELP       - Shows some available commands.
LOOK or L  - Lets you see the map/room again.
QUESTS     - Lists all your active and completed quests.
INV        - Lists all the items in your inventory.
CHECK      - Lets you see an item (or yourself) in more detail.
NORTH or N - Moves you to the north.
SOUTH or S - Moves you to the south.
EAST or E  - Moves you to the east.
WEST or W  - Moves you to the west.
QUIT       - Ends the adventure.""")
	elif command == "LOOK" or command == "L" or command == "":
		current_room.draw()
		
	elif command == "QUIT": # exiting game
		print("Bye!")
		exit()
		completion = True
	elif command == "NORTH" or command == "N": #move commands
		current_room = current_room.move("N")
	elif command == "WEST" or command == "W":
		current_room = current_room.move("W")
	elif command == "SOUTH" or command == "S":
		current_room = current_room.move("S")
	elif command == "EAST" or command == "E":
		current_room = current_room.move("E")
	
	elif command == "CHECK":
		_check = input("Check what? ").upper()
		i=0
		item_exist = False
		while i < len(player.inventory): # printing each item in the inventory
			if _check == player.inventory[i].name.upper() or _check == player.inventory[i].short.upper(): 
				print()
				player.inventory[i].get_info()
			i+=1
			item_exist = True
		if _check == "ME": # printing for self
			player.check_self()
		elif item_exist == False: # if the item isn't there
			print("\nYou don't have that!")

	elif command == "INV":
		print("You are carrying:")
		if len(player.inventory) == 0:
			print("Nothing.")
		else:
			for i in range(len(player.inventory)): # each individual inventory printed out
				print("- A {}".format(player.inventory[i].name))
				
	elif command == "QUESTS":
		if len(_quest) ==0:
			print("\n=== All quests complete! Congratulations! ===")
			exit()	
		i=0
		while i < len(_quest):
			if _quest[i].complete == True:
				print("#{:02.00f}: {} - {}".format(i, _quest[i].reward.name.ljust(20), _quest[i].desc) + " [COMPLETED]")
			else:
				print("#{:02.00f}: {} - {}".format(i, _quest[i].reward.name.ljust(20), _quest[i].desc))
			i+=1
		count = 0
		for i in range(len(_quest)):
			if _quest[i].complete == True:
				count +=1
			if count == len(_quest):
				print()
				exit("=== All quests complete! Congratulations! ===")
	else:
		print("You can't do that.")
		


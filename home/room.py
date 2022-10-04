class Room:
	def __init__(self, name):
		"""TODO: Initialises a room. Do not change the function signature (line 2)."""
		self.name = name
		self.quest = None
		self.N = None
		self.W = None
		self.S = None
		self.E = None
	def get_name(self):
		"""TODO: Returns the room's name."""
		return self.name
	
	def get_short_desc(self):
		"""TODO: Returns a string containing a short description of the room. This description changes based on whether or not a relevant quest has been completed in this room.
		
		If there are no quests that are relevant to this room, this should return: 'There is nothing in this room.' """
		
		print("You are standing at the {}.".format(self.name))
		if self.quest == None:
				print("There is nothing in this room.")
		else:
			if self.quest.is_complete() == False:
				print(self.quest.before)
			else:
				print(self.quest.after)
				
	def get_quest_action(self):
		"""TODO: If a quest can be completed in this room, returns a command that the user can input to attempt the quest."""
		return self.action

	def set_quest(self, q):
		"""TODO: Sets a new quest for this room."""
		self.quest = q

	def get_quest(self):
		"""TODO: Returns a Quest object that can be completed in this room."""
		return self.quest
		
	def set_path(self, dir, dest):
		"""TODO: Creates a path leading from this room to another."""
		if dir == "N" or dir == "NORTH":
			self.N = dest
		elif dir == "S" or dir == "SOUTH":
			self.S = dest
		elif dir == "W" or dir == "WEST":
			self.W = dest
		elif dir == "E" or dir == "EAST":
			self.E = dest
			

	def draw(self):
		"""TODO: Creates a drawing depicting the exits in each room."""
		room = [[" " for j in range(22)] for i in range(11)]
		for i in range(11):
			for j in  range(22):
				if i ==0 or i == 10:
					room[i][j] = "-" # bottom and top
				if j == 0 or j== 21:
					room[i][j] = "|"
		room[0][0]="+"
		room[0][21]="+"
		room[10][0]="+"
		room[10][21]="+"
		if self.N != None:
			room[0][10]="N"
			room[0][11]="N"
		if self.W != None:
			room[5][0]="W"
		if self.S != None:
			room[10][11]="S"
			room[10][10]="S"
		if self.E != None:
			room[5][21]="E"
		print()
		for i in range(11):
			for j in range(22):
				print(room[i][j],end = "")
			print()
		self.get_short_desc()
	def move(self, dir):
		"""TODO: Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""
		adjoiningroom = self
		self.dir = dir
		if dir == "N":
			if self.N != None:
				adjoiningroom = (self.N)
				print("You move to the north, arriving at the {}.".format(adjoiningroom.name))
			else:
				print("You can't go that way.")
		if dir == "W":
			if self.W != None:
				adjoiningroom = (self.W)
				print("You move to the west, arriving at the {}.".format(adjoiningroom.name))
			else:
				print("You can't go that way.")
		if dir == "S":
			if self.S != None:
				adjoiningroom = (self.S)
				print("You move to the south, arriving at the {}.".format(adjoiningroom.name))
			else:
				print("You can't go that way.")
		if dir == "E":
			if self.E != None:
				adjoiningroom = (self.E)
				print("You move to the east, arriving at the {}.".format(adjoiningroom.name))
			else:
				print("You can't go that way.")
		
		if adjoiningroom != self:
			adjoiningroom.draw()
		return (adjoiningroom)
	

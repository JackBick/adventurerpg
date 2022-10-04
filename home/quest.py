class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		"""TODO: Initialises a quest."""
		self.reward = reward
		self.action = action
		self.desc = desc
		self.before = before
		self.after = after
		req = req.split(" ")
		if req[0] == "SKILL":
			self.req_skill = int(req[1])
			self.req_will = 0
		elif req[0] == "WILL":
			self.req_will = int(req[1])
			self.req_skill = 0
		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room
		self.complete = False
	def get_info(self):
		return self.desc

	def is_complete(self):
		"""TODO: Returns whether or not the quest is complete."""
		return self.complete

	def get_action(self):
		"""TODO: Returns a command that the user can input to attempt the quest."""
		return self.action

	def get_room_desc(self):
		"""TODO: Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed."""
		if self.complete == False:
			return self.before
		if self.complete == True:
			return self.after
		
	def attempt(self, player):
		if self.complete == True:
			print("You have already completed this quest.")
		elif player.item_skill >= self.req_skill and player.item_will >= self.req_will:
			player.take(self.reward)
			self.complete = True
			is_complete = True
			print(self.pass_msg)
		else:
			print(self.fail_msg)
		"""TODO: Allows the player to attempt this quest.

		Check the cumulative skill or will power of the player and all their items. If this value is larger than the required skill or will threshold for this quest's completion, they succeed and are rewarded with an item (the room's description will also change because of this).

		Otherwise, nothing happens."""



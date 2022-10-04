class Adventurer:
	def __init__(self):
		self.inventory = []
		self.skill = 5
		self.will = 5
		self.item_skill = self.skill
		self.item_will = self.will

	def get_inv(self):
		"""TODO: Returns the adventurer's inventory."""
		return self.inventory

	def get_skill(self):
		"""TODO: Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make."""
		return self.item_skill

	def get_will(self):
		"""TODO: Returns the adventurer's will power. Whether this value is generated before or after item bonuses are applied is your decision to make."""
		return self.will_skill

	def take(self, item):
		"""TODO: Adds an item to the adventurer's inventory."""
		self.inventory.append(item)
		if self.item_skill + item.skill_bonus >= 5:
			self.item_skill += item.skill_bonus
		else:
			self.item_skill = 0
			
		if self.item_will + item.will_bonus >= 5:
			self.item_will += item.will_bonus
		else:
			self.item_will = 0

	def check_self(self):
		"""TODO: Shows adventurer stats and all item stats."""
		print("\nYou are an adventurer, with a SKILL of {} and a WILL of {}.".format(self.skill,self.will))
		print(("You are carrying:\n"))
		if len(self.inventory) == 0:
			print("Nothing.\n")
		else:
			i=0
			while i < len(self.inventory):
				self.inventory[i].get_info()
				i+=1
		print("With your items, you have a SKILL level of {} and a WILL power of {}.".format(self.item_skill,self.item_will))


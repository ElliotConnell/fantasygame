# class Dwarf

from class_gameobject import GameObject

class Dwarf(GameObject):
	def __init__(self, name):
		self.class_name = "dwarf"
		self.health = 4
		self._desc = "A stubborn opponent"
		super().__init__(name)

	@property
	def desc(self):
		if self.health >=3:
			return self._desc
		elif self.health == 2:
			health_line = "It has lost its foot."
		elif self.health == 1:
			health_line = "Its lost a lot of blood!"
		elif self.health <= 0:
			health_line = "It is dead"
		return self._desc + "\n" + health_line

	@desc.setter
	def desc(self, value):
		self._desc = value
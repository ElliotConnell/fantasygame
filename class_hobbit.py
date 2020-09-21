# class Hobbit

from class_gameobject import GameObject

class Hobbit(GameObject):
	def __init__(self, name):
		self.class_name = "hobbit"
		self.health = 3
		self._desc = "A friendly companion"
		super().__init__(name)

	@property
	def desc(self):
		if self.health >=3:
			return self._desc
		elif self.health == 2:
			health_line = "It has a cut on its face.."
		elif self.health == 1:
			health_line = "It is seriously injured"
		elif self.health <= 0:
			health_line = "It is dead"
		return self._desc + "\n" + health_line

	@desc.setter
	def desc(self, value):
		self._desc = value
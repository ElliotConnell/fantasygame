# class human

from class_gameobject import GameObject


class Human(GameObject):
	def __init__(self, name):
		self.class_name = "human"
		self.health = 4
		self._desc = "A priviliged ego"
		super().__init__(name)

	@property
	def desc(self):
		if self.health >=3:
			return self._desc
		elif self.health == 2:
			health_line = "It has a gash on its arm."
		elif self.health == 1:
			health_line = "Its left leg has been cut off!"
		elif self.health <= 0:
			health_line = "It is dead"
		return self._desc + "\n" + health_line

	@desc.setter
	def desc(self, value):
		self._desc = value
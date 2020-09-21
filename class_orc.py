#class orc

from class_gameobject import GameObject

class Orc(GameObject):
	def __init__(self, name):
		self.class_name = "orc"
		self.health = 8
		self._desc = "A mighty beast"
		super().__init__(name)

	@property
	def desc(self):
		if self.health >= 8:
			return self._desc
		elif self.health == 7:
			health_line = "It has barely been scratched."
		elif self.health == 6:
			health_line = "It is, but a flesh wound"
		elif self.health == 5:
			health_line = "It felt that one!"
		elif self.health == 4:
			health_line = "It has a wound on its knee."
		elif self.health == 3:
			health_line = "Its flank has been slashed open!"
		elif self.health == 2:
			health_line = "Its left arm has been cut off!"
		elif self.health == 1:
			health_line = "Its right leg has been cut off!"
		elif self.health <= 0:
			health_line = "It is dead"
		return self._desc + "\n" + health_line

	@desc.setter
	def desc(self, value):
		self._desc = value
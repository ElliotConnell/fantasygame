
def get_input():
	command = input(": ").split()
	verb_word = command[0]
	if verb_word in verb_dict:
		verb = verb_dict[verb_word]
	else:
		print("Unknown verb {}". format(verb_word))
		return

	if len(command) >= 2:
		noun_word = command[1]
		print(verb(noun_word))
	else:
		print(verb("nothing"))

def say(noun):
	return 'You said "{}"'.format(noun)

def examine(noun):
	if noun in GameObject.objects:
		return GameObject.objects[noun].get_desc()
	else:
		return "There is no {} here.".format(noun)

def hit(noun):
	if noun in GameObject.objects:
		thing = GameObject.objects[noun]
		if type(thing) == Goblin:
			thing.health -= 1
			if thing.health <= 0:
				msg = "You killed the goblin!"
			else:
				msg = "You hit the {}".format(thing.class_name)
		elif type(thing) == Elf:
			thing.health -= 1
			if thing.health <= 0:
				msg = "You killed the elf!"
			else:
				msg = "You hit the {}".format(thing.class_name)
		elif type(thing) == Orc:
			thing.health -= 1
			if thing.health == 4:
				msg = "That's it, you've got him!"
			elif thing.health <= 0:
				msg = "You killed the orc!"
			else:
				msg = "You hit the {}".format(thing.class_name)
		elif type(thing) == Human:
			thing.health -= 1
			if thing.health <= 0:
				msg = "You killed the human!"
			else:
				msg = "You hit the {}".format(thing.class_name)
		elif type(thing) == Dwarf:
			thing.health -= 1
			if thing.health <= 0:
				msg = "You killed the dwarf!"
			else:
				msg = "You hit the {}".format(thing.class_name)
		else:
			msg = "There is no {} here.".format(noun)
		return msg

def heal(noun):
	if noun in GameObject.objects:
		thing = GameObject.objects[noun]
		if type(thing) == Goblin:
			thing.health += 1
			if thing.health >= 3:
				msg = "Goblin is at full health"
			elif thing.health == 1:
				msg = "Goblin has been revived!"
			else:
				msg = "You healed the {}".format(thing.class_name)
		elif type(thing) == Elf:
			thing.health += 1
			if thing.health >= 4:
				msg = "Elf is at full health"
			elif thing.health == 1:
				msg = "Elf has been revived!"
			else:
				msg = "You healed the {}".format(thing.class_name)
		elif type(thing) == Orc:
			thing.health += 1
			if thing.health >= 8:
				msg = "Orc is at full health"
			elif thing.health == 1:
				msg = "Orc has been revived!"
			else:
				msg = "You healed the {}".format(thing.class_name)
		elif type(thing) == Human:
			thing.health += 1
			if thing.health >= 4:
				msg = "Human is at full health"
			elif thing.health == 1:
				msg = "Human has been revived!"
			else:
				msg = "You healed the {}".format(thing.class_name)
		elif type(thing) == Dwarf:
			thing.health += 1
			if thing.health >= 4:
				msg = "Dwarf is at full health"
			elif thing.health == 1:
				msg = "Dwarf has been revived!"
			else:
				msg = "You healed the {}".format(thing.class_name)
		else:
			msg = "There is no {} here.".format(noun)
		return msg
		
class GameObject:
	class_name = ""
	desc = ""
	objects = {}

	def __init__(self, name):
		self.name = name
		GameObject.objects[self.class_name] = self

	def get_desc(self):
		return self.class_name + "\n" + self.desc

class Goblin(GameObject):
	def __init__(self, name):
		self.class_name = "goblin"
		self.health = 3
		self._desc = "A foul creature"
		super().__init__(name)

	@property
	def desc(self):
		if self.health >=3:
			return self._desc
		elif self.health == 2:
			health_line = "It has a wound on its knee."
		elif self.health == 1:
			health_line = "Its left arm has been cut off!"
		elif self.health <= 0:
			health_line = "It is dead"
		return self._desc + "\n" + health_line

	@desc.setter
	def desc(self, value):
		self._desc = value


class Elf(GameObject):
	def __init__(self, name):
		self.class_name = "elf"
		self.health = 5
		self._desc = "A sensitive soul"
		super().__init__(name)

	@property
	def desc(self):
		if self.health >=4:
			return self._desc
		elif self.health == 3:
			health_line = "It has a wound on its knee."
		elif self.health == 2:
			health_line = "Its ear has been severed!"
		elif self.health == 1:
			health_line = "Its left arm has been cut off!"
		elif self.health <= 0:
			health_line = "It is dead"
		return self._desc + "\n" + health_line

	@desc.setter
	def desc(self, value):
		self._desc = value

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

goblin = Goblin("Gobbly")
elf = Elf("Elfy")
orc = Orc("Orcy")
human = Human("Steve")
dawrf = Dwarf("Dwarfy")


verb_dict = {
	"say": say,
	"examine": examine,
	"hit": hit,
	"heal": heal,
}

while True:
	get_input()




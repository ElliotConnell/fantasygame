#function hit

from class_gameobject import GameObject

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
		elif type(thing) == Hobbit:
			thing.health -= 1
			if thing.health <= 0:
				msg = "You killed the hobbit!"
			else:
				msg = "You hit the {}".format(thing.class_name)
		else:
			msg = "There is no {} here.".format(noun)
		return msg

from class_goblin import Goblin

from class_elf import Elf	

from class_orc import Orc

from class_human import Human

from class_dwarf import Dwarf

from class_hobbit import Hobbit




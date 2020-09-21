# function heal

from class_gameobject import GameObject

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
			if thing.health >= 5:
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


from class_goblin import Goblin

from class_elf import Elf	

from class_orc import Orc

from class_human import Human

from class_dwarf import Dwarf
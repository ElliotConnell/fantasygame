
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
		
from class_gameobject import GameObject

from class_goblin import Goblin

from class_elf import Elf	

from class_orc import Orc

from class_human import Human

from class_dwarf import Dwarf




goblin = Goblin("Gobbly")
elf = Elf("Elfy")
orc = Orc("Orcy")
human = Human("Steve")
dwarf = Dwarf("Dwarfy")


verb_dict = {
	"say": say,
	"examine": examine,
	"hit": hit,
	"heal": heal,
}

while True:
	get_input()




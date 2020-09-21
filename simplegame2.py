
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

from func_say import say

from func_examine import examine

from func_hit import hit

from func_heal import heal

from class_gameobject import GameObject

from class_goblin import Goblin

from class_elf import Elf	

from class_orc import Orc

from class_human import Human

from class_dwarf import Dwarf

from class_hobbit import Hobbit


goblin = Goblin("Gobbly")
elf = Elf("Elfy")
orc = Orc("Orcy")
human = Human("Steve")
dwarf = Dwarf("Dwarfy")
hobbit = Hobbit("Hobbs")


verb_dict = {
	"say": say,
	"examine": examine,
	"hit": hit,
	"heal": heal,
}

while True:
	get_input()




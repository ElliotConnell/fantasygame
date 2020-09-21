# function examine

from class_gameobject import GameObject

def examine(noun):
	if noun in GameObject.objects:
		return GameObject.objects[noun].get_desc()
	else:
		return "There is no {} here.".format(noun)
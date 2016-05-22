from random import randint
from element_game_stats import skullkenStats

def skullken(opponentHP,opponentEP,opponentPoisoned,opponentSinkHole,opponentDisarmed):
	damage = 0

	if opponentPoisoned == True:
		opponentHP = opponentHP - 5

	if randint(0,100) <= skullkenStats['epRegenChance']:
		opponentEP = opponentEP + skullkenStats['epRegenCount']

	opponentAttack = randint(1,4)

	if opponentDisarmed > 0:
		if opponentDisarmed > 0:
			print('Skullken sits there')
		else:
			print('Skullken stands up finally')
		opponentDisarmed = opponentDisarmed - 1

	elif opponentAttack == 1:
		if opponentEP >= 18:
			damage = damage + 12
			opponentEP = opponentEP - 18
			print('Skullken used *Narrator Wonders if he\'s Reading this Correctly* Gkop?')
		else:
			print('Skullken Gkopped himself')

	elif opponentAttack == 2:
		if opponentEP >= 24:
			damage = damage + 10
			opponentEP = opponentEP - 19
			print('Skullken bopped you!? *Narrator\'s Headache Intensifies*')
		else:
			print('Skullken bopped himself...')

	elif opponentAttack == 3:
		if opponentEP >= 1:
			damage = damage + 1
			opponentEP = opponentEP - 1
			print('Skullken lopped you! *Narrator Becomes Confused*')
		else:
			print('Skullken lopped himself')

	elif opponentAttack == 4:
		if opponentEP >= 78:
			damage = damage + 15
			opponentEP = opponentEP - 78
			print('Skullken... *Narrator Shivers* "Licked" you')
		else:
			print('*Narrator Gives Skullken a Weird Look* Skullken licked himself...')

	if opponentSinkHole > 0:
		opponentEP = opponentEP - 25
		opponentSinkHole = opponentSinkHole - 1
		if opponentSinkHole == 0:
			print('Skullken got out of the Sink Hole!')

	input()

	return opponentHP,opponentEP,damage,opponentPoisoned,opponentSinkHole,opponentDisarmed
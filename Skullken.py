#This was Jacob's idea
from random import randint, choice
from element_game_stats import skullkenStats

narratorConfusion = [
"",
"*Narrator Wonders if he's Reading this Correctly* ",
"*Narrator's Headache Intensifies* "
"*Narrator Becomes Confused* ",
"*Narrator Shivers* ",
"*Narrator Gives Skullken a Weird Look* ",
]

def skullken(opponentHP,opponentEP,statusEffects):
	damage = 0

	if statusEffects['opponentPoisoned'] == True:
		opponentHP = opponentHP - 5

	if randint(0,100) <= skullkenStats['epRegenChance']:
		opponentEP = opponentEP + skullkenStats['epRegenCount']

	opponentAttack = randint(1,4)

	if statusEffects['opponentDisarmed'] > 0:
		if statusEffects['opponentDisarmed'] > 0:
			print('Skullken sits there')
		else:
			print('Skullken stands up finally')
		statusEffects['opponentDisarmed'] = statusEffects['opponentDisarmed'] - 1

	elif opponentAttack == 1:
		if opponentEP >= 18:
			damage = damage + 12
			opponentEP = opponentEP - 18
			print('Skullken used '+choice(narratorConfusion)+'Gkop?')
		else:
			print('Skullken Gkopped himself')

	elif opponentAttack == 2:
		if opponentEP >= 24:
			damage = damage + 10
			opponentEP = opponentEP - 19
			print('Skullken bopped you!? '+choice(narratorConfusion))
		else:
			print('Skullken bopped himself...')

	elif opponentAttack == 3:
		if opponentEP >= 1:
			damage = damage + 1
			opponentEP = opponentEP - 1
			print('Skullken lopped you! '+choice(narratorConfusion))
		else:
			print('Skullken lopped himself')

	elif opponentAttack == 4:
		if opponentEP >= 78:
			damage = damage + 15
			opponentEP = opponentEP - 78
			print('Skullken... '+choice(narratorConfusion)+'"Licked" you')
		else:
			print('Skullken licked himself...'+choice(narratorConfusion))

	if statusEffects['opponentSinkHole'] > 0:
		opponentEP = opponentEP - 25
		statusEffects['opponentSinkHole'] = statusEffects['opponentSinkHole'] - 1
		if statusEffects['opponentSinkHole'] == 0:
			print('Skullken got out of the Sink Hole!')

	input()

	return dict(zip(['opponentHP','opponentEP','damage','statusEffects'],[opponentHP,opponentEP,damage,statusEffects]))

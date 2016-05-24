from random import randint
from element_game_stats import testStats

def test(opponentHP,opponentEP,opponentPoisoned,opponentSinkHole,opponentDisarmed):
	damage = 0

	if opponentPoisoned == True:
		opponentHP = opponentHP - 5

	if randint(0,100) <= testStats['epRegenChance']:
		opponentEP = opponentEP + testStats['epRegenCount']

	opponentAttack = randint(1,4)

	if opponentDisarmed > 0:
		if opponentDisarmed == 2:
			print('Test\'s wand leaps out of his hand!')
		else:
			print('Test fumbles for his wand...')
		opponentDisarmed = opponentDisarmed - 1

	elif opponentAttack == 1:
		if opponentEP >= 25:
			damage = damage + 20
			opponentEP = opponentEP - 25
			print('Test used bug finder!')
		else:
			print('Test tried to use bug finder...')

	elif opponentAttack == 2:
		if opponentEP >= 30:
			damage = damage + 25
			opponentEP = opponentEP - 30
			print('Test used BSOD')
		else:
			print('Test tried to use BSOD...')

	elif opponentAttack == 3:
		if opponentEP >= 10:
			damage = damage + 5
			opponentEP = opponentEP - 10
			print('Test use error code: ID 10-T!')
		else:
			print('Test tried to use error code: ID 10-T')

	elif opponentAttack == 4:
		if opponentEP >= 25:
			opponentEP = opponentEP - 25
			opponentHP = opponentHP + 20
			print('Test put on a bandaid!')
		else:
			print('Test looked around for a bandaid...')

	if opponentSinkHole > 0:
		opponentEP = opponentEP - 25
		opponentSinkHole = opponentSinkHole - 1
		if opponentSinkHole == 0:
			print('Test got out of the Sink Hole!')

	input()

	return dict(zip(['opponentHP','opponentEP','damage','opponentPoisoned','opponentSinkHole','opponentDisarmed'],[opponentHP,opponentEP,damage,opponentPoisoned,opponentSinkHole,opponentDisarmed]))

#!/usr/bin/python3.4

'''
I work on this in my free time, but I can't take all the credit.
If it weren't for Ethan and Jacob, I would have stopped working on this long ago.
So thank you guys for keeping me interested in this, and coming up with some of the more fun characters.
'''

import subprocess as sp #clear()
from time import sleep
import sys #detect if OS is Windows or Linux
from random import randint,random #random chance things
from test_enemy import test #test()
from Skullken import skullken #skullken()
from element_game_stats import * #everyone's stats

if sys.platform == 'linux':
	def clear():
		tmp = sp.call('clear',shell=True)
else:
	def clear():
		tmp = sp.call('cls',shell=True)

def potterSpellCast(selectedPotterSpell,HP,EP,opponentDisarmed,opponentHP): #allows for different spells per battle
	
	if selectedPotterSpell == 0:
		if EP >= 10:
			HP = int(1.5*HP)
			EP = EP - 10
			print('You cast Episkey!')
			print('Your HP is now:',HP)
			print()
		else:
			print('You don\'t have enough energy to cast Episkey!')
			print()
	
	elif selectedPotterSpell == 1:
		opponentHP = int(opponentHP - .8*EP)
		EP = 0
		print('AVADA KEDAVRA!!!')
	
	return dict(zip(['EP','opponentHP','HP','opponentDisarmed'],[EP,opponentHP,HP,statusEffects['opponentDisarmed']]))

#########################################################################
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
#########################################################################

elements = [ #the main menu prints from this list, and it checks this list for the character you select
'air',
'water',
'earth',
'fire',
'clone trooper',
'narrator',
'jedi',
'walle',
'potter'
]

while True:
	statusEffects={ #reset things between battles
		'opponentPoisoned':False,
		'opponentSinkHole':0,
		'opponentAsleep':False,
		'forceBlock':False,
		'opponentDisarmed':0
	}
	earthQuakeValue = 0
	plasmaCooldown = 3
	clonesOnSite = 0
	electroSnakeLife = 0
	results = ()
	clear()
	print('choose an element') #display characters
	for x in range(0,len(elements)):
		print(elements[x].title())
	print('Settings')
	print()
	playerElement  =  str(input()).lower() #not case sensitive
	clear()
	if playerElement == elements[0]: #info screen
		HP = airStats['hpPoints']
		EP = airStats['epPoints']
		clear()
		print('You have chosen Air!')
		print()
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',airStats['epRegenChance'])
		print('EP regen:',airStats['epRegenCount'])
		print()
		for ability in range(len(airStats['abilities'])):
			print(airStats['abilities'][ability])
		print()
		input() 
		opponent = randint(1,2) #initialize a random opponent
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True: #fighting sequence

			if randint(1,100) <= airStats['epRegenChance']: #whether or not you'll regain EP
				EP = EP + airStats['epRegenCount'] #how much EP you'll regain

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			clear()

			print(opponentName) #enemy status
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP) #your status
			print('EP:',EP)
			print()
			for ability in range(len(airStats['abilities'])): #print moveset
				y = str(ability+1)+')'
				print(y,airStats['abilities'][ability])
			print()

			attack = getch()

			if str(attack) == '1':
				if EP >= 15: #check if you have enough EP
					opponentHP = opponentHP - 10 #damage
					EP = EP - 15 #EP cost
					print('You used Category 1 wind!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Category 1 wind!')
					print()

			elif str(attack) == '2':
				if EP >= 30:
					opponentHP = opponentHP - 25
					EP = EP - 30
					print('You used Tornado!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Tornado!')
					print()

			elif str(attack) == '3':
				if EP >= 10:
					opponentHP = opponentHP - 5
					EP = EP - 10
					print('You used Updraft!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Updraft!')
					print()

			elif str(attack) == '4':
				if EP >= 25:
					opponentEP = opponentEP - randint(0,20)
					EP = EP - 25
					HP = HP + randint(10,30) #health regen
					print('You used Vortex Blast!')
					print(opponentName+'\'s EP is down to',opponentEP)
					print()
				else:
					print('You don\'t have enough energy to use Vortex Blast!')
					print()

			else:
				print(attack,'is not an attack')

			if opponent == 1: #opponent's turn
				results = test(opponentHP,opponentEP,statusEffects)
			elif opponent == 2:
				results = skullken(opponentHP,opponentEP,statusEffects)

			opponentHP,opponentEP,damage = results['opponentHP'],results['opponentEP'],results['damage'] #result of opponent's turn

			HP = HP - damage #take damage

	elif playerElement == elements[1]:
		HP = waterStats['hpPoints']
		EP = waterStats['epPoints']
		clear()
		print('You have chosen Water!')
		print()
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',waterStats['epRegenChance'])
		print('EP regen:',waterStats['epRegenCount'])
		print()
		print('Abilities')
		for ability in range(len(waterStats['abilities'])):
			print(waterStats['abilities'][ability])
		print()
		input()
		opponent = randint(1,2)
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(1,100) <= waterStats['epRegenChance']:
				EP = EP + waterStats['epRegenCount']

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print()
			for ability in range(len(waterStats['abilities'])):
				y = str(ability+1)+')'
				print(y,waterStats['abilities'][ability])
			print()

			attack = getch()

			if str(attack) == '1':
				if EP >= 30:
					opponentHP = opponentHP - randint(20,30)
					EP = EP - 30
					print('You used Water Spout!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Water Spout!')
					print()

			elif str(attack) == '2':
				if EP >= 15:
					opponentHP = opponentHP - 15
					EP = EP - 15
					print('You used Quick Sand!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Quick Sand!')
					print()

			elif str(attack) == '3':
				if EP >= 50:
					statusEffects['opponentPoisoned'] = True #inflict a status effect <sarcasm>definitely not overpowered</sarcasm>
					EP = EP - 50
					print('You used Poison!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Poison!')
					print()

			elif str(attack) == '4':
				WinterBlastCost = int(input('Cost: ')) #FANCY
				if EP >= WinterBlastCost:
					WinterBlastDamage = WinterBlastCost // 2 + 5
					opponentHP = opponentHP - WinterBlastDamage
					EP = EP - WinterBlastCost
					print('You used Winter Blast!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()

			else:
				print(attack,'is not an attack')

			if opponent == 1:
				results = test(opponentHP,opponentEP,statusEffects)
			elif opponent == 2:
				results = skullken(opponentHP,opponentEP,statusEffects)

			opponentHP,opponentEP,damage,statusEffects = results['opponentHP'],results['opponentEP'],results['damage'],results['statusEffects']

			HP = HP - damage

	elif playerElement == elements[2]:
		HP = earthStats['hpPoints']
		EP = earthStats['epPoints']
		clear()
		print('You have chosen Earth')
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',earthStats['epRegenChance'])
		print('EP regen:',earthStats['epPoints'])
		print()
		print('Abilities')
		for ability in range(len(earthStats['abilities'])):
			print(earthStats['abilities'][ability])
		print()
		input()
		opponent = randint(1,2)
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(1,100) <= earthStats['epRegenChance']:
				EP = EP + earthStats['epRegenCount']

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print()
			for ability in range(len(earthStats['abilities'])):
				y = str(ability+1)+')'
				print(y,earthStats['abilities'][ability])
			print()

			attack = getch()

			if str(attack) == '1':
				earthQuakeValue = randint(0,50)
				if EP >= 30:
					opponentHP = opponentHP - earthQuakeValue
					EP = EP - earthQuakeValue
					print('You used Earth Quake Level VII')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Earth Quake Level VII')
					print()

			elif str(attack) == '2':
				if EP >= 15:
					statusEffects['opponentSinkHole'] = 4 #status effect with a duration
					EP = EP - 15
					print('You used Sink Hole')
					print(opponentName+'\'s EP is down to',opponentEP)
					print()
				else:
					print('You don\'t have enough energy to use Sink Hole!')
					print()

			elif str(attack) == '3':
				if EP >= 30:
					opponentHP = opponentHP - 20
					EP = EP - 30
					print('You used Metal Shot!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Metal Shot!')
					print()

			elif str(attack) == '4':
				if EP >= 15:
					opponentHP = opponentHP - 10
					EP = EP - 15
					print('You used Fissure!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\' have enough energy to use Fissure')
					print()

			else:
				print(attack,'is not an attack')

			if opponent == 1:
				results = test(opponentHP,opponentEP,statusEffects)
			elif opponent == 2:
				results = skullken(opponentHP,opponentEP,statusEffects)

			opponentHP,opponentEP,damage,statusEffects = results['opponentHP'],results['opponentEP'],results['damage'],results['statusEffects']

			HP = HP - damage

	elif playerElement == elements[3]:
		HP = fireStats['hpPoints']
		EP = fireStats['epPoints']
		clear()
		print('You have chosen Fire!')
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',fireStats['epRegenChance'])
		print('EP regen:',fireStats['epRegenCount'])
		print()
		print('Abilities')
		for ability in range(len(fireStats['abilities'])):
			print(fireStats['abilities'][ability])
		print()
		input()
		opponent = randint(1,2)
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(1,100) <= fireStats['epRegenChance']:
				EP = EP + fireStats['epRegenCount']

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print()
			for ability in range(len(fireStats['abilities'])):
				y = str(ability+1)+')'
				print(y,fireStats['abilities'][ability])	
			print()

			attack = getch()

			if str(attack) == '1':
				logs = int(input('How many logs? '))
				refuelCost = logs * randint(5,10)
				refuelGain = logs * randint(10,20)
				if EP >= refuelCost:
					print('You used Refuel!')
					HP = HP + refuelGain
					print('Your HP is:',HP)
					print()
				else:
					print('You don\'t have enough energy to use Refuel!')
					print()

			elif str(attack) == '2':
				if EP >= 30:
					opponentHP = opponentHP - randint(10,30)
					EP = EP - randint(20,30)
					print('You used Fire Devil!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Fire Devil!')
					print()

			elif str(attack) == '3':
				if EP >= 10:
					opponentHP = opponentHP - randint(30,50)
					EP = EP - 50
					print('You used Lightning Strike!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Lightning Strike!')
					print()

			elif str(attack) == '4':
				if EP >= 25:
					opponentEP = opponentEP - randint(20,45)
					EP = EP - randint(25,45)
					print('You used Lava Flow!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use Lava Flow!')
					print()

			else:
				print(attack,'is not an attack')

			if opponent == 1:
				results = test(opponentHP,opponentEP,statusEffects)
			elif opponent == 2:
				results = skullken(opponentHP,opponentEP,statusEffects)

			opponentHP,opponentEP,damage = results['opponentHP'],results['opponentEP'],results['damage']

			HP = HP - damage

	elif playerElement == elements[4]:
		HP = cloneStats['hpPoints']
		EP = cloneStats['epPoints']
		clear()
		print('You have chosen Clone Trooper!') #Ethan would approve
		print()
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',cloneStats['epRegenChance'])
		print('EP regen:',cloneStats['epRegenCount'])
		print()
		print('Abilities:')
		for ability in range(len(cloneStats['abilities'])):
			print(cloneStats['abilities'][ability])
		print()
		input() 
		opponent = randint(1,2)

		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(1,100) <= cloneStats['epRegenChance']:
				EP = EP + cloneStats['epRegenCount']

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			if plasmaCooldown != 0:
				plasmaCooldown = plasmaCooldown - 1

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print('Clones under your command:',clonesOnSite)
			print()
			for ability in range(len(cloneStats['abilities'])):
				y = str(ability+1)+')'
				print(y,cloneStats['abilities'][ability])

			attack = getch()

			if attack == '1': #unique attack that creates decoys
				if EP >= 5:
					EP = EP - 5
					clonesOnSite = clonesOnSite + 2
					print('You called in 2 clones!')
					print()
				else:
					print('There are no clones on call!')
					print()

			elif attack == '2':
				if EP >= 5:
					opponentHP = opponentHP - 5
					EP = EP - 5
					print('You shot '+opponentName+'!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough ammo to shoot '+opponentName+'!')
					print()

			elif attack == '3':
				if EP >= 20:
					opponentHP = opponentHP - randint(40,60)
					EP = EP - 20
					print('You Dropped a nuke on '+opponentName+'!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have any Nukes')
					print()

			elif attack == '4':
				if EP >= 10:
					opponentHP = opponentHP - randint(10,25)
					EP = EP - 10
					print('You used electro whip!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('Your electro whip is out of power!')
					print()

			elif attack == '5': #unique attack that spawns a "sidekick" of sorts
				if EP >= 15:
					EP = EP - 15
					electroSnakeLife = randint(4,6)
					print('You unleashed your electro snake!')
					print()
				else:
					print('Your electro snake is recharging!')
					print()

			elif attack == '6': #I just, just... Not much to say about this... Ethan likes it
				if plasmaCooldown == 0:
					if EP >= 70:
						EP = EP - 70
						opponentHP = opponentHP - randint(70,100) #    O_O
						print('You shot '+opponentName+' with a plasma ball!')
						print(opponentName+'\'s HP is down to',opponentHP)
						print()
					else:
						print('Your plasma blaster is being reloaded!')
						print()
				else:
					print('The plasma blaster is still being built') #this is the only thing that adds some balance (and not very much at that)
					print()

			else:
				print(attack,'is not an attack')

			if clonesOnSite == 0:
				if opponent == 1:
					results = test(opponentHP,opponentEP,statusEffects)
				elif opponent == 2:
					results = skullken(opponentHP,opponentEP,statusEffects)

				opponentHP,opponentEP,damage = results['opponentHP'],results['opponentEP'],results['damage']

				HP = HP - damage

			else: #decoy
				clonesOnSite = clonesOnSite - 1
				print(opponentName+' shot one of your clone troopers!')
				input()

			if electroSnakeLife > 0: #Electro Snake attack
				electroSnakeLife = electroSnakeLife - 1
				opponentHP = opponentHP - randint(20,40)
				print('Electro Snake shocked '+opponentName+'!')
				print(opponentName+'\'s HP is down to',opponentHP)
				input()

	elif playerElement == elements[5]:#<humor>
		HP = narratorStats['hpPoints']
		EP = narratorStats['epPoints']
		print('The Narrator prepares to speak in the third person!')
		sleep(1)
		clear()
		print('The Narrator has been selected!')
		print()
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',narratorStats['epRegenChance'])
		print('EP regen:',narratorStats['epRegenCount'])
		print()
		print('Abilities')
		for ability in range(len(narratorStats['abilities'])):
			print(narratorStats['abilities'][ability])
		print()
		input()
		opponent = randint(1,2)
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(1,100) <= narratorStats['epRegenChance']:
				EP = EP + narratorStats['epRegenCount']

			if opponentHP < 1:
				print('The Narrator won!')
				input()
				print('The Narrator stops speaking in the third person')
				sleep(1)
				break

			if HP < 1:
				print('The Narrator lost!')
				input()
				break

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print()
			for ability in range(len(narratorStats['abilities'])):
				y = str(ability+1)+')'
				print(y,narratorStats['abilities'][ability])
			print()

			attack = getch()

			if str(attack) == '1':
				if EP >= 15:
					opponentHP = opponentHP - 15
					EP = EP - 15
					print('The Narrator told a boring story!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('The Narrator doesn\'t have enough energy to tell a boring story!')
					print()

			elif str(attack) == '2':
				if EP >= 30:
					statusEffects['opponentAsleep'] = True #status effect
					EP = EP - 30
					print('The Narrator gave a mathematics lecture!')
					print(opponentName+' fell asleep')
					print()
				else:
					print('The Narrator doesn\'t have enough energy to give a mathematics lecture!')
					print()

			elif str(attack) == '3':
				if EP >= 10:
					opponentEP = opponentEP - 5
					EP = EP - 10
					print('The Narrator told a sermon!')
					print(opponentName+' feels guilty...')
					print()
				else:
					print('The Narrator doesn\'t have enough energy to tell a sermon!')
					print()

			elif str(attack) == '4':
				if EP >= 25:
					EP = EP - 25
					HP = HP + randint(10,15)
					print('The Narrator told a relaxing tale!')
					print('The Narrator\'s HP is now',HP)
					print()
				else:
					print('The Narrator doesn\'t have enough energy to tell a relaxing tale!')
					print()

			else:
				print(attack,'is not an attack')

			if statusEffects['opponentAsleep'] == True: #chance to wake up
				if randint(1,3) == 1:
					statusEffects['opponentAsleep'] = False

			if statusEffects['opponentAsleep'] == False: #this really should be in the enemy function
				if opponent == 1:
					results = test(opponentHP,opponentEP,statusEffects)
				elif opponent == 2:
					results = skullken(opponentHP,opponentEP,statusEffects)

				opponentHP,opponentEP,damage,statusEffects = results['opponentHP'],results['opponentEP'],results['damage'],results['statusEffects']

				HP = HP - damage

			else:
				print(opponentName+' is asleep from the mathematics lecture')
				input() #</humor>

	elif playerElement == elements[6]: #Ethan and Jacob approve
		HP = jediStats['hpPoints']
		EP = jediStats['epPoints']
		clear()
		print('You have chosen Jedi!')
		print()
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',jediStats['epRegenChance'])
		print('EP regen:',jediStats['epRegenCount'])
		print()
		for ability in range(len(jediStats['abilities'])):
			print(jediStats['abilities'][ability])
		print()
		input()
		opponent = randint(1,2)
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(1,100) <= jediStats['epRegenChance']:
				EP = EP + jediStats['epRegenCount']

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print()
			for ability in range(len(jediStats['abilities'])):
				y = str(ability+1)+')'
				print(y,jediStats['abilities'][ability])
			print()

			attack = getch()

			if str(attack) == '1':
				if EP >= 10:
					opponentHP = opponentHP - 10
					EP = EP - 10
					print('You used force push!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use force push!')
					print()

			elif str(attack) == '2':
				if EP >= 5:
					opponentHP = opponentHP - 10
					EP = EP - 5
					print('You used force ball!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use force ball!')
					print()

			elif str(attack) == '3':
				if EP >= 10:
					opponentHP = opponentHP - 20
					EP = EP - 10
					print('You used your lightsaber!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use your lightsaber!')
					print()

			elif str(attack) == '4':
				if EP >= 10:
					EP = EP - 10
					statusEffects['forceBlock'] = True #self inflicted status effect
					print('You used force block!')
					print()
				else:
					print('You don\'t have enough energy to use force block!')
					print()

			else:
				print(attack,'is not an attack')

			if opponent == 1:
				results = test(opponentHP,opponentEP,statusEffects)
			elif opponent == 2:
				results = skullken(opponentHP,opponentEP,statusEffects)

			opponentHP,opponentEP,damage = results['opponentHP'],results['opponentEP'],results['damage']

			HP = HP - damage

			if statusEffects['forceBlock'] == True: #minimize damage
				damage = round(damage*.3,0)
				statusEffects['forceBlock'] = False

			if randint(1,100) <= 40: #slightly overpowered...
				print('Your Padawan attacked '+opponentName+'!')
				opponentHP = opponentHP - 15
				input()

	elif playerElement == elements[7]: #Jacob approves
		HP = walleStats['hpPoints']
		EP = walleStats['epPoints']
		clear()
		print('You have chosen WALLⒺ!')
		print()
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:',walleStats['epRegenChance'])
		print('EP regen:',walleStats['epRegenCount'])
		print()
		for ability in range(len(walleStats['abilities'])):
			print(walleStats['abilities'][ability])
		print()
		input() 
		opponent = randint(1,2)
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(1,100) <= walleStats['epRegenChance']:
				EP = EP + walleStats['epRegenCount']

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print()
			for ability in range(len(walleStats['abilities'])):
				y = str(ability+1)+')'
				print(y,walleStats['abilities'][ability])
			print()

			attack = getch()

			if str(attack) == '1':
				if EP >= 5:
					opponentHP = opponentHP - 10
					EP = EP - 5
					print('You used your laser!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use your laser!')
					print()

			elif str(attack) == '2':
				if EP >= 20:
					opponentHP = opponentHP - 30
					EP = EP - 20
					print('You used your Trash Compactor!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use your Trash Compactor!')
					print()

			elif str(attack) == '3':
				if EP >= 30:
					opponentHP = opponentHP - 5 # don't
					EP = EP - 30 #                ask
					print('You used EVE\'s Blaster!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to use EVE\'s Blaster!')
					print()

			elif str(attack) == '4':
				if EP >= 2:
					opponentHP = opponentHP - 10
					EP = EP - 2
					print('You used Cute Eyes!')
					print(opponentName+'\'s EP is down to',opponentEP)
					print()
				else:
					print('You don\'t have enough energy to look cute!')
					print()

			else:
				print(attack,'is not an attack')

			if opponent == 1:
				results = test(opponentHP,opponentEP,statusEffects)
			elif opponent == 2:
				results = skullken(opponentHP,opponentEP,statusEffects)

			opponentHP,opponentEP,damage = results['opponentHP'],results['opponentEP'],results['damage']

			HP = HP - damage

	elif playerElement == elements[8]:
		HP = potterStats['hpPoints']
		EP = potterStats['epPoints']
		print('You have chosen The Boy Who Lived!')
		print()
		print('HP:',HP)
		print('EP:',EP)
		print('EP regen chance:'+str(potterStats['epRegenChance'])+'%')
		print('EP regen:',potterStats['epRegenCount'])
		print()
		print('Abilities:')
		for ability in range(len(potterStats['abilities'])):
			print(potterStats['abilities'][ability])
		print()
		input()
		opponent = randint(1,2)
		if opponent == 1:
			opponentHP = testStats['hpPoints']
			opponentEP = testStats['epPoints']
			opponentName = 'Test'
		if opponent == 2:
			opponentHP = skullkenStats['hpPoints']
			opponentEP = skullkenStats['epPoints']
			opponentName = 'Skullken'
		clear()
		print('You are fighting '+opponentName+'!')
		sleep(1)
		while True:

			if randint(0,100) <= potterStats['epRegenChance']:
				EP = EP + potterStats['epRegenCount']

			if opponentHP < 1:
				print('You win!')
				input()
				break

			if HP < 1:
				print('You lose!')
				input()
				break

			clear()

			print(opponentName)
			print('Enemy HP:',opponentHP)
			print('Enemy EP:',opponentEP)

			print()

			print('HP:',HP)
			print('EP:',EP)
			print()
			for ability in range(len(potterStats['abilities'])):
				y = str(ability+1)+')'
				print(y,potterStats['abilities'][ability])
			print()

			attack = input()

			if str(attack) == '1': #selectable spell. batteries not included
				spellResult = potterSpellCast(selectedPotterSpell,HP,EP,statusEffects['opponentDisarmed'],opponentHP)

				EP,opponentHP,HP,statusEffects['opponentDisarmed'] = spellResult['EP'],spellResult['opponentHP'],spellResult['HP'],spellResult['opponentDisarmed']

			elif str(attack) == '2':
				if EP >= 10:
					EP = EP - 10
					print('You cast Expelliarmus!')
					if randint(0,100) <= 50:
						statusEffects['opponentDisarmed'] = statusEffects['opponentDisarmed'] + 2 #status effect
						opponentAttack = 0
						print(opponentName,'was disarmed!')
					else:
						print(opponentName,'countered!')
					print()
				else:
					print('You don\'t have enough energy to cast Expelliarmus!')
					print()

			elif str(attack) == '3':
				if EP >= 30:
					opponentHP = int(random()*opponentHP) #this can hurt a bit...
					EP = EP - 30
					print('You cast Sectumsempra!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to cast Sectumsempra!')
					print()

			elif str(attack) == '4':
				if EP >= 15:
					EP = EP - 15
					opponentHP = opponentHP - randint(15,20)
					print('You cast Expulso!')
					print(opponentName+'\'s HP is down to',opponentHP)
					print()
				else:
					print('You don\'t have enough energy to cast Expulso!')
					print()

			else:
				print(attack,'is not an attack')

			if opponent == 1:
				results = test(opponentHP,opponentEP,statusEffects)
			elif opponent == 2:
				results = skullken(opponentHP,opponentEP,statusEffects)

			opponentHP,opponentEP,damage,statusEffects = results['opponentHP'],results['opponentEP'],results['damage'],results['statusEffects']

			HP = HP - damage

			if randint(0,100) <= 10: #<sarcasm> This is definitely not overpowered. No not at all... </sarcasm>
				HP = HP + 2*damage
				EP = 10*EP
				clear()
				print('Dumbledore!')
				input()

	elif playerElement == 'settings':
		clear()
		print('Choose who to edit')
		for x in range(0,len(elements)):
			print(elements[x].title())
		print()
		playerElement = input()
		clear()

		if playerElement == elements[0]:
			print('HP',airStats['hpPoints'],'default: 80')
			print()
			airStats['hpPoints'] = int(input())
			clear()
			print('EP',airStats['epPoints'],'default: 120')
			print()
			airStats['epPoints'] = int(input())
			clear()
			print('EP regen',airStats['epRegenCount'],'default: 10')
			print()
			airStats['epRegenCount'] = int(input())
			clear()
		elif playerElement == elements[1]:
			print('HP',waterStats['hpPoints'],'default: 120')
			print()
			waterStats['hpPoints'] = int(input())
			clear()
			print('EP',waterStats['epPoints'],'default: 100')
			print()
			waterStats['epPoints'] = int(input())
			clear()
			print('EP regen',waterStats['epRegenCount'],'default: 15')
			print()
			waterStats['epRegenCount'] = int(input())
			clear()
		elif playerElement == elements[2]:
			print('HP',earthStats['hpPoints'],'default: 150')
			print()
			earthStats['hpPoints'] = int(input())
			clear()
			print('EP',earthStats['epPoints'],'default: 100')
			print()
			earthStats['epPoints'] = int(input())
			clear()
			print('EP regen',earthStats['epRegenCount'],'default: 30')
			print()
			earthStats['epRegenCount'] = int(input())
			clear()
		elif playerElement == elements[3]:
			print('HP',fireStats['hpPoints'],'default: 100')
			print()
			fireStats['hpPoints'] = int(input())
			clear()
			print('EP',fireStats['epPoints'],'default: 100')
			print()
			fireStats['epPoints'] = int(input())
			clear()
			print('EP regen',fireStats['epRegenCount'],'default: 50')
			print()
			fireStats['epRegenCount'] = int(input())
			clear()
		elif playerElement == elements[4]:
			print('HP',cloneStats['hpPoints'],'default: 110')
			print()
			cloneStats['hpPoints'] = int(input())
			clear()
			print('EP',cloneStats['epPoints'],'default: 110')
			print()
			cloneStats['epPoints'] = int(input())
			clear()
			print('EP regen',cloneStats['epRegenCount'],'default: 10')
			print()
			cloneStats['epRegenCount'] = int(input())
			clear()

	elif playerElement == 'exit':
		break

	else:
		clear()
		print(playerElement,'is not a choice')
		input()

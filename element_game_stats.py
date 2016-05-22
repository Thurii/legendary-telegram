testStats = {
'hpPoints':100,
'epPoints':100,
'epRegenCount':10,
'epRegenChance':30
}

skullkenStats = {
'hpPoints':65,
'epPoints':99,
'epRegenCount':1,
'epRegenChance':100
}

airStats = {
'hpPoints':80,
'epPoints':120,
'epRegenCount':5,
'epRegenChance':100,
0:'Category 1 wind -- Cost:15 EP - Damage:10 HP',
1:'Tornado -- Cost:30 EP - Damage:25 HP',
2:'Updraft -- Cost:10 EP - Damage:5 HP',
3:'Vortex Blast -- Cost:25 EP - Damage:0~20 EP - Gain:10~30 HP'
}

waterStats = {
'hpPoints':120,
'epPoints':100,
'epRegenCount':15,
'epRegenChance':80,
0:'Water Spout -- Cost:30 EP - Damage:20~30 HP',
1:'Quick Sand -- Cost:15 EP - Damage:15 HP',
2:'Poison -- Cost:50 EP - Damage:5 HP per round',
3:'Winter Blast -- Cost:? EP- Damage:Cost/2+5=HP'
}

earthStats = {
'hpPoints':150,
'epPoints':100,
'epRegenCount':30,
'epRegenChance':50,
0:'Earth Quake Level VII -- Cost:0~50 EP - Damage:0~50 HP',
1:'Sink Hole -- Cost:45 EP - Damage:25 EP per round for 4 rounds',
2:'Metal Shot -- Cost:30 EP - Damage:20 HP',
3:'Fissure -- Cost:15 EP - Damage:10 HP'
}

fireStats = {
'hpPoints':100,
'epPoints':100,
'epRegenCount':50,
'epRegenChance':25,
0:'Refuel -- Cost:5~10 EP per log - Gain:10~20 HP for 1~2 rounds per log',
1:'Fire Devil -- Cost:20~30 EP - Damage:10~30 HP',
2:'Lightning Strike -- Cost:50 - Damage:30~50',
3:'Lava Flow -- Cost:25~45 - Damage:20~45'
}

cloneStats = {
'hpPoints':110,
'epPoints':110,
'epRegenCount':10,
'epRegenChance':100,
0:'Call in Clones -- Cost:10 EP - Clones Called in: 2',
1:'Blaster Gun -- Cost:5 EP - Damage:5 HP',
2:'Nuclear Bomb -- Cost:20 EP - Damage:40~60 HP',
3:'Electro Whip -- Cost:10 EP - Damage:10~25 HP',
4:'Electro Snake -- Cost:15 EP - Damage:20~40 HP for 4~6 Rounds',
5:'Plasma Blaster -- Cost:70 EP - Damage:70~100 HP - Can\'t be used in round 1, 2, and 3'
}

narratorStats = {
'hpPoints':100,
'epPoints':100,
'epRegenCount':15,
'epRegenChance':85,
0:'boring story -- Cost:15 EP - Damage:15 HP',
1:'mathematics lecture -- Cost:30 EP - Effect: Target Falls Asleep',
2:'sermon -- Cost:10 EP - Damage:5 EP',
3:'relaxing tale -- Cost:25 EP - Gain:10~15 HP'
}

jediStats = {
'hpPoints':150,
'epPoints':130,
'epRegenCount':10,
'epRegenChance':100,
0:'Force Push -- Cost:10 EP - Damage:10 HP',
1:'Force Ball -- Cost:5 EP - Damage:10 HP',
2:'Lightsaber -- Cost:10 EP - Damage:20 HP',
3:'Force Block -- Cost:10 - Protection:30%'
}

walleStats = {
'hpPoints':150,
'epPoints':150,
'epRegenCount':20,
'epRegenChance':25,
0:'Laser -- Cost:5 EP - Damage:10 HP',
1:'Trash Compactor -- Cost:20 EP - Damage:30 HP',
2:'EVE\'s Blaster -- Cost:30 EP - Damage:20 HP',
3:'Cute Eyes -- Cost:2 EP - Causes Enemy to Deal 10HP to Itself'
}

selectedPotterSpell = 0
potterSpell = ['Episkey -- Cost:10 EP - Health:+50%','The Killing Curse -- Cost:EP']

potterStats = {
'hpPoints':100,  #HP
'epPoints':100,  #EP
'epRegenCount':10,   #EP Regen
'epRegenChance':75,  #Regen chance
0:potterSpell[selectedPotterSpell],
1:'Expelliarmus -- Cost:10 EP Chance:50%',
2:'Sectumsempra -- Cost:30 EP - Damage:0-100% HP',
3:'Expulso -- Cost:15 - Damage:15-20 HP'
}
#CONSEGUIR QUE O BACKGROUND SE MOVA 

import pygame , sys
from pygame.locals import *
import random
import json
import time

#compartilhado com o grupo do jogo da dança
with open('highscore.json','r') as arquivo:
	dados = json.load(arquivo)

#compartilhado com o grupo do jogo da dança
letras={}
letras[K_a]='a'
letras[K_b]='b'
letras[K_c]='c'
letras[K_d]='d'
letras[K_e]='e'
letras[K_f]='f'
letras[K_g]='g'
letras[K_h]='h'
letras[K_i]='i'
letras[K_j]='j'
letras[K_k]='k'
letras[K_l]='l'
letras[K_m]='m'
letras[K_n]='n'
letras[K_o]='o'
letras[K_p]='p'
letras[K_q]='q'
letras[K_r]='r'
letras[K_s]='s'
letras[K_t]='t'
letras[K_u]='u'
letras[K_v]='v'
letras[K_w]='w'
letras[K_x]='x'
letras[K_y]='y'
letras[K_z]='z'

pygame.init()
pygame.mixer.init()
pygame.font.init()


class jogador(pygame.sprite.Sprite):
	def __init__(self,tela,imagem):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagem)
		self.tela = tela


	def posicao(self,x,y,tela):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rect.top = 525
		self.rect.left = 100
		self.width = 71
		self.height = 523 



	def desenha(self,nave_topo,nave_esq):
		self.tela.blit(self.image,(self.rect.x,
									self.rect.y))

	def update(self,x):
		self.rect.x = x
	

class monstrosgif(pygame.sprite.Sprite):
	def __init__(self,tela,imagem1,imagem2,bomba,tipo):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem1)
		self.image1 = pygame.image.load(imagem1)
		self.image2 = pygame.image.load(imagem2)
		self.image3 = pygame.image.load(bomba)
		self.tela = tela
		self.passo1 = 0
		self.passo2 = 0
		self.passo3 = 0
		self.passo4 = 1
		self.direcao = 1
		self.direcaoy = 1
		self.type = 1
		self.tipo = tipo
		self.descida = 0

	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.yinicial = self.rect.y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
									self.rect.y))


	def update(self):
		if self.image == self.image3:
			self.passo3 += 1
			if self.passo3 >=10:
				self.kill()
		
		if self.descida < 300:
			if self.image != self.image3:
				if self.passo1 < 40:
					self.image = self.image2
				elif self.passo1 >= 40:
					self.image = self.image1
				if self.passo1 == 80:
					self.passo1 = 0
				else:
					self.passo1 += 1

				if self.passo2 >= 30:
					self.direcao = -1
				elif self.passo2 <= -30:
					self.direcao = 1
				self.passo2 += self.direcao
				self.rect.x += self.direcao

		if self.descida >= 300:
			if self.passo4 == 1:
				if self.rect.y < 600:
					self.direcaoy = 1
				elif self.rect.y >= 600:
					self.passo4 = 2
			if self.passo4 == 2:
				self.direcaoy = -1
				if self.yinicial == self.rect.y:
					self.passo4 = 1
					self.descida = 0
			self.rect.y += self.direcaoy
		if self.tipo == 2:
			self.descida +=1
			


				


################### nave mae ############################
class navemae(pygame.sprite.Sprite):
	def __init__(self,tela,imagem,imagem1,imagem2,bomba):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.image1 = pygame.image.load(imagem1)
		self.image2 = pygame.image.load(imagem2)
		self.image3 = pygame.image.load(bomba)
		self.tela = tela
		self.passo = 0
		self.direcao = 1
		self.type = 1
		self.passo1 = 0
		self.passo2 = 0
		self.passo3 = 0

	def posicao(self,x,y):
		self.rect = self.image.get_rect() 
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
									self.rect.y))


	def update(self):
		if self.passo >= 715:
			self.direcao = -1
		elif self.passo <= 0:
			self.direcao = 1
	
		
		self.passo += self.direcao
		self.rect.x += self.direcao

		if self.image == self.image3:
			self.passo3 += 1
			if self.passo3 >=10:
				self.kill()
		
		if self.image != self.image3:
			if self.passo1 < 40:
				self.image = self.image2
			elif self.passo1 >= 40:
				self.image = self.image1
			if self.passo1 == 80:
				self.passo1 = 0
			else:
				self.passo1 += 1

			# if self.passo2 >= 30:
			# 	self.direcao = -1
			# elif self.passo2 <= -30:
			# 	self.direcao = 1
			# self.passo2 += self.direcao
			# self.rect.x += self.direcao


#######################tiros############################
class shots(pygame.sprite.Sprite):
	def __init__(self,tela,imagem,imagemG,m,q):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.imageG = pygame.image.load(imagemG)
		self.tela = tela
		self.m = m
		self.qualidade = q
		self.colisoes = 0

		
	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
									self.rect.y))
	def update(self):
		if self.m == 1:
			self.rect.y -= 5
			if self.rect.y < 0:
				self.kill()
		if self.m == 2:
			self.rect.y += 3
			if self.rect.y > 600:
				self.kill()

		if self.qualidade == 3:
			self.image = self.imageG
		if self.qualidade == 1:
			self.image = self.image

		if self.qualidade == 3:
			if self.colisoes >= 4:
				self.kill()

class premio(pygame.sprite.Sprite):
	def __init__(self,tela,imagem,ajuda):
		pygame.sprite.Sprite.__init__(self)

		#self.image = pygame.image.load(imagem)
		self.image = pygame.image.load(imagem) #vida

		self.tela = tela
		self.ajuda = ajuda

		
	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
									self.rect.y))
	def update(self):
		self.rect.y += 3
		if self.rect.y > 600:
			self.kill()


class Vida(pygame.sprite.Sprite):
	def __init__(self,tela,imagem,x,y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.tela = tela

 
def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	button_was_clicked = False

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect( tela, ac,(x,y,w,h))
		if click[0] == 1:
			button_was_clicked = True    
	else:
		pygame.draw.rect( tela, ic,(x,y,w,h))
	smallText = pygame.font.Font("trench100free.ttf",24)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	tela.blit(textSurf, textRect)
	return button_was_clicked

def buttonback(msg,x,y,w,h,ic,ac):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	button_was_clicked = False

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect( tela, ac,(x,y,w,h))
		if click[0] == 1:
			button_was_clicked = True    
	else:
		pygame.draw.rect( tela, ic,(x,y,w,h))
	smallerText = pygame.font.Font("ABeeZee-Regular.ttf",14)
	textSurf, textRect = text_objects(msg, smallerText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	tela.blit(textSurf, textRect)
	return button_was_clicked


#highscore
#compartilhado com o grupo do jogo da dança
def organizadados(dados):
	highscore = sorted(dados.items(), key=lambda x: x[1], reverse=True)
	dadosorg = []
	for y, z in highscore:
		myfont.set_bold(True)
		pontos = myfont.render('{0} : {1}'.format(y,z) , False, (255,255,255))
		dadosorg.append(pontos)
	print(dadosorg)
	return dadosorg

#compartilhado com o grupo do jogo da dança
def lerpontos(dadosorg,tela):
	for i in range(130,580,50):
		if i == 130:
			tela.blit(dadosorg[0],(25,i))
		elif i == 180:
			tela.blit(dadosorg[1],(25,i))
		elif i == 230:
			tela.blit(dadosorg[2],(25,i))
		elif i == 280:
			tela.blit(dadosorg[3],(25,i))
		elif i == 330:
			tela.blit(dadosorg[4],(25,i))
		elif i == 380:
			tela.blit(dadosorg[5],(25,i))
		elif i == 430:
			tela.blit(dadosorg[6],(25,i))
		elif i == 480:
			tela.blit(dadosorg[7],(25,i))
		elif i == 530:
			tela.blit(dadosorg[8],(25,i))
		
	for  i in range(130,580,50):
		if i == 130:
			tela.blit(dadosorg[9],(425,i))
		elif i == 180:
			tela.blit(dadosorg[10],(425,i))
		elif i == 230:
			tela.blit(dadosorg[11],(425,i))
		elif i == 280:
			tela.blit(dadosorg[12],(425,i))
		elif i == 330:
			tela.blit(dadosorg[13],(425,i))
		elif i == 380:
			tela.blit(dadosorg[14],(425,i))
		elif i == 430:
			tela.blit(dadosorg[15],(425,i))
		elif i == 480:
			tela.blit(dadosorg[16],(425,i))
		elif i == 530:
			tela.blit(dadosorg[17],(425,i))

#compartilhado com o grupo do jogo da dança
def save(dados):
	with open('highscore.json','w') as dados_salvar:
		dados_salvar.writelines(json.dumps(dados))


#cores do menu 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,100,0)
yellow = (255,140,0)
blue = (112,138,144)

def game_intro():
	intro = True

	
display_width = 800
display_height = 600

clock = pygame.time.Clock()

tela = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)

pygame.display.set_caption("Space Recycler's - Code Girls")

background = pygame.image.load("espaco.jpg")
quadrado_name = pygame.image.load("qua2.jpg")
instr1 = pygame.image.load("instru1.jpg")
instr2 = pygame.image.load("instru2.jpg")

tirom = shots(tela,"shot.png","shot.png",2,1)
grupo_tirosm = pygame.sprite.Group()
grupo_boost = pygame.sprite.Group()
grupo_tirosnavem =  pygame.sprite.Group()

ajudas = ["life","tiro3","campodeforca"]
imagemajudas = ["heart.png","rainho.png","rainho.png"]

shoot_sound = pygame.mixer.Sound("laser_shoot.wav")
mus_game = pygame.mixer.Sound("Space2.wav")

#contadores
tiro = 0
numero = 0
pontos = 0
level = 1
contagem = 0
acertosnavemae = 0
c_tirom = 0
c_tironavem = 100
c_boost = 0
vida = 3
life = 1
q = 1
protecao = 0
C_protecao = 0
c_tiroG = 0
C_colisoes = 0
C_gameover = 0
jogoinicial = 0
z = 0
tela_atual = "intro"
contamons = 0

#fontes
myfont = pygame.font.Font('trench100free.ttf', 30)
myfont1 = pygame.font.Font('trench100free.ttf', 100)
myfont2 = pygame.font.Font('trench100free.ttf', 60)
fontmenu = pygame.font.Font('ABeeZee-Regular.ttf', 90)
titulo = fontmenu.render("Space Recycler's", False, white)
#fim = myfont1.render('Você venceu!!!!!!', False, (255,255,255))
gameover = fontmenu.render('Game Over',False, (255,255,255))
instruc = myfont1.render('Bem vindo ao jogo',False, (255,255,255))
proxnivel = fontmenu.render('Próximo nivel',False, (255,255,255))
high = fontmenu.render('High Score',False, (255,255,255))
font_aviso = pygame.font.Font('ABeeZee-Regular.ttf', 20)
font_aviso2 = pygame.font.Font('ABeeZee-Regular.ttf', 40)
mostracampo = font_aviso.render('Campo de força ativo!', False, (255,255,255))
mostraarma = font_aviso.render('Super tiro ativo!', False, (255,255,255))
fontpont = pygame.font.Font('trench100free.ttf', 23)	
digite_nome = font_aviso2.render('Digite seu nome:', False, (255,255,255))
nome = ""
listalixos = [["garrafaagua1.png","garrafaagua2.png","plastico.png"],["garrafavidro.png","garrafavidro2.png","vidro.png"],["lata1.png","lata2.png","metal.png"],["banana1.png","banana2.png","organico.png"],["pizza1.png","pizza2.png","papel.png"]]

grupo_tiros = pygame.sprite.Group()
listasom = ["Sound","Mute"]
indice = 0

dadosorg = organizadados(dados)
while True:

	if tela_atual == "intro":
		intro = True
		while intro:

			pygame.mouse.set_visible(1)
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			tela.blit(background, (0, 0))
			
			tela.blit(titulo,(60,80))
			button_play_clicked = button("Jogar",312.5,230,175,70,black,green)
			button_inst_clicked = button("Instruções",312.5,315,175,70,black,yellow)
			button_score_clicked = button("High Score", 312.5,400,175,70,black,blue)
			button_exit_clicked = button("Sair",312.5,485,175,70,black,red)

			if button_play_clicked:
				desenho_vida = Vida(tela,"nave_vida.png",750,10)
				desenho_vida1 = Vida(tela,"nave_vida.png",700,10)
				desenho_vida2 = Vida(tela,"nave_vida.png",650,10)
				desenho_vida3 = Vida(tela,"nave_vida.png",600,10)

				grupo_vida = pygame.sprite.Group()
				grupo_vida.add(desenho_vida)
				grupo_vida.add(desenho_vida1)
				grupo_vida.add(desenho_vida2)
				tiro = 0
				numero = 0
				pontos = 0
				level = 1
				contagem = 0
				acertosnavemae = 0
				c_tirom = 0
				c_tironavem = 100
				c_boost = 0
				vida = 3
				life = 1
				q = 1
				protecao = 0
				C_protecao = 0
				c_tiroG = 0
				C_colisoes = 0
				C_gameover = 0
				jogoinicial = 0
				contamons = 0
				z = 0
				contagemcampo = 0
				jogoinicial = 0
				tela_atual = "jogo"
				intro = False
				mus_game.play()
				

			elif button_inst_clicked:
				tela_atual = "instrucoes"
				intro = False

			elif button_score_clicked:
				tela_atual = "high score"
				intro = False

			elif button_exit_clicked:
				tela_atual = "sair"
				intro = False


			pygame.display.update()
			clock.tick(60)


	elif tela_atual == "instrucoes":
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sys.exit()
		tela.blit(instr1, (0, 0))
		button_exitgame_clicked = buttonback("Menu",25,7,50,25,red,blue)
		if button_exitgame_clicked:
			tela_atual = "intro"
			intro = True
		button_prox_clicked = buttonback ("Next", 725, 525, 50, 25, yellow, blue)
		if button_prox_clicked:
			tela_atual = "instrucoes2"
		pygame.display.update()
		clock.tick(60)


	elif tela_atual == "instrucoes2":
		for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					sys.exit()
		tela.blit(instr2, (0, 0))
		button_exitgame_clicked = buttonback("Menu",25,7,50,25,red,blue)
		button_back_clicked = buttonback ("Back", 725, 525, 50, 25, yellow, blue)
		if button_back_clicked:
			tela_atual = "instrucoes"
			
		if button_exitgame_clicked:
			tela_atual = "intro"
			intro = True
		pygame.display.update()
		clock.tick(60)


	elif tela_atual == "high score":
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sys.exit()
		tela.blit(background, (0, 0))
		tela.blit(high,(180,10))
		button_exitgame_clicked = buttonback("Menu",700,525,50,25,red,blue)
		if button_exitgame_clicked:
			tela_atual = "intro"
			intro = True
		dadosorg = organizadados(dados)
		lerpontos(dadosorg,tela)
		pygame.display.update()
		clock.tick(60)

	elif tela_atual == "Gameover":

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sys.exit()
			#compartilhado com o grupo do jogo da dança
			if evento.type == pygame.KEYDOWN:
			    if evento.key in letras:
			        letra=letras[evento.key]
			        nome+=letra
			        time.sleep(0.15)
			    if evento.key == pygame.K_RETURN:
			    	dados[nome] = pontos
			    	save(dados)
			    	tela_atual = "intro"
			    	intro = True

		tela.blit(background, (0, 0))
		tela.blit(gameover,(150,50))
		tela.blit(quadrado_name,(440,450))
		tela.blit(digite_nome,(110,450))
		pontofim = font_aviso2.render('Pontuação: {0}'.format(pontos),False, (255,255,255))
		tela.blit(pontofim,(270,150))
		button_exitgame_clicked = buttonback("Menu",700,525,50,25,red,blue)
		if button_exitgame_clicked:
			tela_atual = "intro"
			intro = True
		nometela = font_aviso.render(nome, False, (255,255,255))
		tela.blit(nometela,(470,465))
		pygame.display.update()
		clock.tick(60)

	elif tela_atual == "jogo":
		pygame.mouse.set_visible(1)
		if jogoinicial == 0:
			contagemcampo = 0
			q = 1
			protecao = 0
			C_protecao = 0
			c_tiroG = 0
			C_colisoes = 0
			nome = ""
			grupo_tirosm = pygame.sprite.Group()
			grupo_boost = pygame.sprite.Group() 
			grupo_tirosnavem =  pygame.sprite.Group()

			nave1 = jogador(tela,"nova_nave.png")
			nave1.posicao(100,100,tela)
			grupo_nave = pygame.sprite.Group()
			grupo_nave.add(nave1)

			nave_mae = navemae(tela,"nave_mae1.png","nave_mae1.png","nave_mae2.png","metal.png")
			nave_mae.posicao(0,55)
			grupo_nave_mae = pygame.sprite.Group()
			grupo_nave_mae.add(nave_mae)

			if level == 1:

				mortenavemae = 10
				grupo_monstro = pygame.sprite.Group()
				for i in range(150,350,50):
					for j in range(100,700,80):
						a = 0
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],1)	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)
				liberatiro = 250
				liberatirom = 350

			elif level == 2:

				mortenavemae = 15
				grupo_monstro = pygame.sprite.Group()
				for i in range(150,350,40):
					for j in range(100,700,50):

						a = random.randint(0,1)
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],1)	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)
				liberatiro = 200
				liberatirom = 350

			elif level == 3:

				mortenavemae = 20
				liberatiro = 150
				liberatirom = 350
				grupo_monstro = pygame.sprite.Group()
				for i in range(150,300,40):
					for j in range(100,700,80):

						a = random.randint(0,2)
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],1)	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)


				for i in range(150,300,40):
					for j in range(140,660,80):

						a = random.randint(0,2)
						listarandom = [1,2,1,1,1,1,2,1,1,1,1,1,1]
						b = random.randint(0,len(listarandom)-1)
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],listarandom[b])	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)

			elif level == 4:

				mortenavemae = 25
				liberatiro = 150
				liberatirom = 250
				grupo_monstro = pygame.sprite.Group()
				for i in range(150,300,40):
					for j in range(100,700,80):

						a = random.randint(0,3)
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],1)	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)


				for i in range(150,300,40):
					for j in range(140,660,80):

						a = random.randint(0,3)
						listarandom = [1,2,1,2,1,1,2,1,1,1,2,1,2]
						b = random.randint(0,len(listarandom)-1)
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],listarandom[b])	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)

			elif level == 5:

				mortenavemae = 30
				liberatiro = 150
				liberatirom = 250
				grupo_monstro = pygame.sprite.Group()
				for i in range(150,300,40):
					for j in range(100,700,80):

						a = random.randint(0,2)
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],1)	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)


				for i in range(150,300,40):
					for j in range(140,660,80):

						a = random.randint(0,4)
						listarandom = [1,2,1,2,1,1,2,1,2,2,1,2,1]
						b = random.randint(0,len(listarandom)-1)
						novo_monstro = monstrosgif(tela,listalixos[a][0],listalixos[a][1],listalixos[a][2],listarandom[b])	
						novo_monstro.posicao(j, i)
						grupo_monstro.add(novo_monstro)

				level = 1

			jogoinicial = 1 


		if jogoinicial == 1:
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					sys.exit()
				elif evento.type == MOUSEBUTTONDOWN and indice == 0:
					tiro = shots(tela, "shot.png","shotG.png",1,q)
					tiro.posicao(x+ nave1.width/2,nave1.height)
					grupo_tiros.add(tiro)
					shoot_sound.play()
				elif evento.type == MOUSEBUTTONDOWN and indice == 1:
					tiro = shots(tela, "shot.png","shotG.png",1,q)
					tiro.posicao(x+ nave1.width/2,nave1.height)
					grupo_tiros.add(tiro)
					shoot_sound.stop()



			rel_z = z % background.get_rect().height
			tela.blit(background,(0, rel_z - background.get_rect().height))
			if rel_z < background.get_rect().height:
				tela.blit(background,(0,rel_z))
			z += 0.5

			button_exitgame_clicked = buttonback("Menu",190,7,50,25,red,blue)
			if button_exitgame_clicked:
				tela_atual = "intro"

			button_sound_clicked = buttonback (listasom[indice], 250, 7, 50, 25, yellow, blue)
			if button_sound_clicked:
				if indice == 0:
					mus_game.stop()
					button_sound_clicked = buttonback (listasom[indice], 250, 7, 50, 25, yellow, blue)
					if indice == 0:
						indice += 1
					else:
						indice = 1
				elif indice == 1:
					mus_game.play()
					button_sound_clicked = buttonback (listasom[indice], 250, 7, 50, 25, yellow, blue)
					if indice == 1:
						indice -= 1
					else:
						indice = 0

			posicoesmx = []
			posicoesmy = []

			for i in grupo_monstro:
				g = i.rect.x
				f = i.rect.y
				posicoesmx.append(g)
				posicoesmy.append(f)


			c_tirom += 1
			if len(posicoesmx) != 0:
				if c_tirom >= liberatiro:
					g = random.randint(0,len(posicoesmx)-1)
					tirom = shots(tela,"lasernave.png","lasernave.png",2,1)
					tirom.posicao(posicoesmx[g],posicoesmy[g])
					grupo_tirosm.add(tirom)
					c_tirom = 0

			c_tironavem += 1
			if c_tironavem >= liberatirom:
				if len(grupo_nave_mae) > 0:
					tironavem = shots(tela,"shot_monstro.png","shot_monstro.png",2,1)
					tironavem.posicao(nave_mae.rect.x +35,nave_mae.rect.y+80)
					grupo_tirosnavem.add(tironavem)
					c_tironavem = 0

			c_boost += 1
			if len(posicoesmx) != 0:
				if c_boost >= 500:
					a = random.randint(0,len(ajudas)-1)
					g = random.randint(0,len(posicoesmx)-1)
					boost = premio(tela,imagemajudas[a],ajudas[a])
					print(ajudas[a])
					boost.posicao(posicoesmx[g],posicoesmy[g])
					grupo_boost.add(boost)
					c_boost = 0

			ganhaboost = pygame.sprite.groupcollide(grupo_boost,grupo_nave,True,False)
			for i in ganhaboost:						
				if i.ajuda == "life":
					if vida == 4:
						i.ajuda = "campodeforca"
					if vida < 4:
						vida += 1
					if vida == 2:
						grupo_vida.add(desenho_vida1)
					elif vida == 3:
						grupo_vida.add(desenho_vida2)
					elif vida == 4:
						grupo_vida.add(desenho_vida3)
				elif i.ajuda == "tiro3":
					q = 3
				elif i.ajuda == "campodeforca":
					protecao = 1
			if q == 3:
				c_tiroG += 1
				tela.blit(mostraarma,(10,550))

			if c_tiroG >= 300:
				q = 1
				c_tiroG = 0

			if protecao == 1:
				tela.blit(mostracampo,(10,550))

				
		#---------------------------------#

			x,y = pygame.mouse.get_pos()

			grupo_nave.draw(tela)
			grupo_nave_mae.draw(tela)
			grupo_monstro.draw(tela)
			grupo_tiros.draw(tela)
			grupo_tirosm.draw(tela)
			grupo_vida.draw(tela)
			grupo_boost.draw(tela)
			grupo_tirosnavem.draw(tela)


			if q == 3 :
				col = pygame.sprite.groupcollide(grupo_tiros,grupo_monstro,False,False)
				colmons = pygame.sprite.groupcollide(grupo_monstro,grupo_tiros,False,False)
				for i in col:
					pontos += 1
				for i in col:
					i.qualidade += 1
				for i in col:
					pontos += 1
			if q == 1:
				colmons = pygame.sprite.groupcollide(grupo_monstro,grupo_tiros,False,False)
			colnavemae = pygame.sprite.groupcollide(grupo_tiros,grupo_nave_mae,True,False)
			
			if protecao == 0:
				colmatajoga = pygame.sprite.groupcollide(grupo_tirosm,grupo_nave,True,False)
				colnmaejoga = pygame.sprite.groupcollide(grupo_tirosnavem,grupo_nave,True,False)
				colnavemons = pygame.sprite.groupcollide(grupo_monstro,grupo_nave,False,False)

			elif protecao == 1:
				C_protecao +=1
				if C_protecao >= 300:
					C_protecao = 0
					protecao = 0


			for i in colmons:
				pontos += 1


			for i in grupo_monstro:
				if i in colmons:
					i.image = i.image3
			
			ponto = fontpont.render('Pontuação: {0}'.format(pontos), False, (255,255,255))
			tela.blit(ponto,(10,10))

			for i in colmatajoga:
				vida -= 1

			for i in colnavemons:
				if contamons == 0:
					vida -= 1
					contamons += 1
				if contamons >= 100:
					contamons = 0
			if contamons > 0:
				contamons += 1

			for i in colnmaejoga:
				vida -= 1

			if vida == 0:
				nave1.kill()
			if vida == 3:
				desenho_vida3.kill()
			if vida == 2:
				desenho_vida2.kill()
			if vida == 1:
				desenho_vida1.kill()
			


			for i in colnavemae:
				if i.qualidade == 3:
					acertosnavemae += 2
				if i.qualidade == 1:
					acertosnavemae += 1	
			if acertosnavemae >= mortenavemae:
				nave_mae.image = nave_mae.image3
				pontos += 15
				acertosnavemae = 0

			if len(grupo_monstro) == 0 and len(grupo_nave_mae) == 0:

				if C_gameover < 60:
					tela.fill([0,0,0])
					tela.blit(proxnivel,(95,250))
					C_gameover += 1
				if C_gameover >= 60:
					level += 1
					jogoinicial = 0
					C_gameover = 0
					


			if len(grupo_nave) == 0:
				tela_atual = "Gameover"



			grupo_tiros.update()
			grupo_monstro.update()
			grupo_nave_mae.update()
			pygame.display.update()
			grupo_tirosm.update()
			grupo_nave.update(x)
			grupo_boost.update()
			grupo_tirosnavem.update()
			

	elif tela_atual == "sair":
		pygame.quit()
		quit()

		

		pygame.display.flip()
		clock.tick(60)

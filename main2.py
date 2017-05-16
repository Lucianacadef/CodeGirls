#ARRUMAR A POSICAO DO GIF E O TEMPO DE TICK (clock.tick(4))
#COLOCAR ELES NO LUGAR DOS MONSTROS ATUAIS 
#TENTEI ADD MP3 NAO DEU DO MESMO JEITO (mus_inic)
#COLOCAR NAVE MAE NO JOGO -- CONTINUAR (PRECISO COLOCA_LA NO LOOP PRINC)
import pygame , sys
from pygame.locals import *
import random

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



	def desenha(self,nave_topo,nave_esq):
		self.tela.blit(self.image,(nave_topo,
			                        nave_esq))

	def update(self,x):
		self.rect.x = x
	

class monstrosgif(pygame.sprite.Sprite):
	def __init__(self,tela,imagem1,imagem2,bomba):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem1)
		self.image1 = pygame.image.load(imagem1)
		self.image2 = pygame.image.load(imagem2)
		self.image3 = pygame.image.load(bomba)
		self.tela = tela
		self.passo1 = 0
		self.passo2 = 0
		self.passo3 = 0
		self.morreu = 0
		self.direcao = 1
		self.type = 1

	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))


	def update(self):
		if self.image == self.image3:
			self.passo3 +=1
			if self.passo3 >=10:
				self.kill()
				
		if self.image != self.image3:
			if self.passo1 < 15:
				self.image = self.image2
			elif self.passo1 >= 15:
				self.image = self.image1
			if self.passo1 == 30:
				self.passo1 = 0
			else:
				self.passo1 += 1

			if self.passo2 == 10:
				self.direcao = -1
			elif self.passo2 == -10:
				self.direcao = 1
			self.passo2 += self.direcao
			self.rect.x += self.direcao

################### nave mae ############################
class navemae(pygame.sprite.Sprite):
	def __init__(self,tela,imagem):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.tela = tela
		self.passo = 0
		self.direcao = 1
		self.type = 1

	def posicao(self,x,y):
		self.rect = self.image.get_rect() 
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))


	def update(self):
		if self.passo >= 715:
			self.direcao = -3
		elif self.passo <= 0:
			self.direcao = 3
	
		
		self.passo += self.direcao
		self.rect.x += self.direcao


########################################################
class shots(pygame.sprite.Sprite):
	def __init__(self,tela,imagem,imagemG,m,q):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.imageG = pygame.image.load(imagemG)
		self.tela = tela
		self.m = m
		self.qualidade = q

		
	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))
	def update(self):
		if self.m == 1:
			self.rect.y -= 10
			if self.rect.y < 0:
				self.kill()
		if self.m == 2:
			self.rect.y += 10
			if self.rect.y > 600:
				self.kill()

		if self.qualidade == 3:
			self.image = self.imageG
		if self.qualidade == 1:
			self.image = self.image

class premio(pygame.sprite.Sprite):
	def __init__(self,tela,imagem,ajuda):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
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
		self.rect.y += 5
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



clock = pygame.time.Clock()
tela = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space invaders - Code Girls")
desenho_vida = Vida(tela,"nave_vida.png",730,10)
desenho_vida1 = Vida(tela,"nave_vida.png",650,10)
desenho_vida2 = Vida(tela,"nave_vida.png",570,10)
desenho_vida3 = Vida(tela,"nave_vida.png",490,10)
grupo_vida = pygame.sprite.Group()
grupo_vida.add(desenho_vida)
grupo_vida.add(desenho_vida1)
grupo_vida.add(desenho_vida2)
#importanto imgs 
nave1 = jogador(tela,"nova_nave.png")

nave1.posicao(71,67,tela)
grupo_nave = pygame.sprite.Group()
grupo_nave.add(nave1)

background = pygame.image.load("espaco.jpg")
monstrinho = pygame.image.load('monstrinho.png')
mae = navemae(tela,"nave_mae.png")
nave_mae = navemae(tela,"nave_mae.png")
nave_mae.posicao(0,0)
grupo_nave_mae = pygame.sprite.Group()
grupo_nave_mae.add(nave_mae)
tirom = shots(tela,"shot.png","shot.png",2,1)
grupo_tirosm = pygame.sprite.Group()
grupo_boost = pygame.sprite.Group()

ajudas = ["life","tiro3","campodeforca"]
#nave_topo = tela.get_height() - nave.get_height()
#nave_esq = tela.get_width()/2 - nave.get_width()/2
nave_topo = 520
nave_esq = 350


# carregando os sound effects

shoot_sound = pygame.mixer.Sound("laser_shoot.wav")

#shoot_sound.play() só colocar no loop princ

myfont = pygame.font.SysFont('Lucida Console', 30)
myfont1 = pygame.font.SysFont('Lucida Console', 100)
myfont2 = pygame.font.SysFont('Lucida Console', 15)
fim = myfont1.render('Você venceu!!!!!!', False, (255,255,255))
gameover = myfont1.render('Game Over...',False, (255,255,255))


grupo_tiros = pygame.sprite.Group()
tiro = 0
numero = 0
pontos = 0


grupo_monstro = pygame.sprite.Group()
for i in range(100,300,40):
	for j in range(100,700,40):

		novo_monstro = monstrosgif(tela,"m1.png","m3.png","explosion.png")	
		novo_monstro.posicao(j, i)
		grupo_monstro.add(novo_monstro)




#ARRUMAR A POSICAO DO GIF E O TEMPO DE TICK (clock.tick(4))
#COLOCAR ELES NO LUGAR DOS MONSTROS ATUAIS 

contagem = 0
acertosnavemae = 0
c_tirom = 0
c_boost = 0
vida = 3
life = 1
q = 1
protecao = 0
C_protecao = 0
c_tiroG = 0
C_colisoes = 0
####################################################################################

while True:
	pygame.mouse.set_visible(0)
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:

			tiro = shots(tela, "shot.png","shotG.png",1,q)
			tiro.posicao(x+34,nave_topo)
			grupo_tiros.add(tiro)
			shoot_sound.play()

	posicoesmx = []
	posicoesmy = []

	for i in grupo_monstro:
		g = i.rect.x
		f = i.rect.y
		posicoesmx.append(g)
		posicoesmy.append(f)


	c_tirom += 1
	if len(posicoesmx) != 0:
		if c_tirom >= 100:
			g = random.randint(0,len(posicoesmx)-1)
			tirom = shots(tela,"shot_monstro.png","shot_monstro.png",2,1)
			tirom.posicao(posicoesmx[g],posicoesmy[g])
			grupo_tirosm.add(tirom)
			c_tirom = 0

	c_boost += 1
	if len(posicoesmx) != 0:
		if c_boost >= 400:
			a = random.randint(0,len(ajudas)-1)
			g = random.randint(0,len(posicoesmx)-1)
			boost = premio(tela,"monstrinho.png",ajudas[a])
			print(ajudas[a])
			boost.posicao(posicoesmx[g],posicoesmy[g])
			grupo_boost.add(boost)
			c_boost = 0
	ganhaboost = pygame.sprite.groupcollide(grupo_boost,grupo_nave,True,False)
	for i in ganhaboost:
		if vida == 4:
			i.ajuda = "campodeforca"
		if i.ajuda == "life":
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
	if c_tiroG >= 300:
		q = 1
		c_tiroG = 0
	if q == 3:
		mostraarma = myfont2.render('Super tiro ativo!', False, (255,0,0))
		tela.blit(mostraarma,(10,550))

#---------------------------------#
	tela.blit(background, (0, 0))

	x,y = pygame.mouse.get_pos()

	grupo_nave.draw(tela)
	grupo_nave_mae.draw(tela)
	grupo_monstro.draw(tela)
	grupo_tiros.draw(tela)
	grupo_tirosm.draw(tela)
	grupo_vida.draw(tela)
	grupo_boost.draw(tela)


	if q == 3 :
		col = pygame.sprite.groupcollide(grupo_monstro,grupo_tiros,False,False)
		C_colisoes += 1
		if C_colisoes >= 10:
			col = pygame.sprite.groupcollide(grupo_monstro,grupo_tiros,False,True)
			C_colisoes = 0
	if q == 1:
		col = pygame.sprite.groupcollide(grupo_monstro,grupo_tiros,False,True)
	colnavemae = pygame.sprite.groupcollide(grupo_tiros,grupo_nave_mae,True,False)
	if protecao == 0:
		colmatajoga = pygame.sprite.groupcollide(grupo_tirosm,grupo_nave,True,False)
	elif protecao == 1:
		C_protecao +=1
		if C_protecao >= 300:
			C_protecao = 0
			protecao = 0
	if protecao == 1:
		mostracampo = myfont2.render('Campo de força ativo!', False, (255,0,0))
		tela.blit(mostracampo,(10,550))

	for i in col:
		pontos += 1

	for i in grupo_monstro:
		if i in col:
			i.image = i.image3
				
			
	ponto = myfont.render('Pontuação: {0}'.format(pontos), False, (255,255,255))
	tela.blit(ponto,(10,10))

	for i in colmatajoga:
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
	if acertosnavemae >= 10:
		nave_mae.kill()
		pontos += 15
		acertosnavemae = 0

	if len(grupo_monstro) == 0 and len(grupo_nave_mae) == 0:
		#tela.fill([0,0,0])
		#tela.blit(fim,(100,220))
		grupo_monstro = pygame.sprite.Group()
		for i in range(100,300,40):
			for j in range(100,700,40):
				novo_monstro = monstrosgif(tela,"m1.png","m3.png","explosion.png")	
				novo_monstro.posicao(j, i)
				grupo_monstro.add(novo_monstro)

		nave_mae = navemae(tela,"nave_mae.png")
		nave_mae.posicao(0,0)
		grupo_nave_mae = pygame.sprite.Group()
		grupo_nave_mae.add(nave_mae)


	if len(grupo_nave) == 0:
		tela.fill([0,0,0])
		tela.blit(gameover,(100,220))



	grupo_tiros.update()
	grupo_monstro.update()
	grupo_nave_mae.update()
	pygame.display.update()
	grupo_tirosm.update()
	grupo_nave.update(x)
	grupo_boost.update()

	pygame.display.flip()
	clock.tick(60)





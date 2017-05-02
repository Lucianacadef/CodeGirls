import pygame , sys
from pygame.locals import *
class monstros:
	def __init__(self,tela,imagem):
		self.imagem = pygame.image.load(imagem)
		self.tela = tela
		self.topo = tela.get_height() - self.imagem.get_height()
		self.centro = tela.get_width()/2 - self.imagem.get_width()/2

	def desenha(self,x,y):
		self.tela.blit(self.imagem,(self.centro + x,self.topo+y))

def interseccao(s1_x,s1_y,s2_x,s2_y):
	if (s1_x > s2_x - 32) and (s1_y > s2_y - 32) and (s1_x < s2_x - 32) and (s1_y < s2_y - 32):
		return 1
	else:
		return 0



clock = pygame.time.Clock()
tela = pygame.display.set_mode((800,600))
pygame.mouse.set_visible(0)

nave = pygame.image.load("nave_pequena.png")
nave_topo = tela.get_height() - nave.get_height()
nave_esq = tela.get_width()/2 - nave.get_width()/2
pygame.display.set_caption("Space invaders - Code Girls")

tela.blit(nave, (nave_esq,nave_topo))
monstro = monstros(tela,"monstrinho.png")

background = pygame.image.load("espaco.jpg")

tiro = pygame.image.load("shot.png")
atirar_y = 0
monstrosdados = []
monstros = []
for i in range(400,560,40):
	mondic = {}
	num = 0
	for j in range(-300,300,40):
		mon = monstro.desenha(j,-i)
		mondic[num] = [j,-i]
		num = num+1
	monstrosdados.append(mondic)

print(monstrosdados)	
atirar_x = 0
while True:
	monstros = monstrosdados
	clock.tick(60)
	tela.blit(background, (0, 0))
	#tela.fill((0,0,0))
	x,y = pygame.mouse.get_pos()
	tela.blit(nave, (x-nave.get_width()/2,nave_topo))
	#monstro.desenha(0,-500)
	for i in range(400,560,40):
		for j in range(-300,300,40):
			mon = monstro.desenha(j,-i)

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:
			atirar_y = nave_topo
			atirar_x = x
			
					

	if atirar_y > 0:
		tela.blit(tiro, (atirar_x,atirar_y))
		atirar_y -= 15

	for i in range(len(monstrosdados)):
		for j in monstrosdados[i]:
			intersec =interseccao(monstrosdados[i][j][0],monstrosdados[i][j][1],atirar_x,atirar_y)
			if intersec == 1:
				del monstrosdados[i][j]

	

	pygame.display.update()
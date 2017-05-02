import pygame , sys
from pygame.locals import *
class monstros:
	def __init__(self,tela,imagem):
		self.imagem = pygame.image.load(imagem)
		self.tela = tela
		self.topo = tela.get_height() - self.imagem.get_height()
		self.centro = tela.get_width()/2 - self.imagem.get_width()/2

	def desenha(self):
		self.tela.blit(self.imagem,(self.centro,self.topo))

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


while True:
	clock.tick(60)
	tela.blit(background, (0, 0))
	#tela.fill((0,0,0))
	x,y = pygame.mouse.get_pos()
	tela.blit(nave, (x-nave.get_width()/2,nave_topo))
	monstro.desenha()
	

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:
			atirar_y = nave_topo
			atirar_x = x

	if atirar_y > 0:
		tela.blit(tiro, (atirar_x,atirar_y))
		atirar_y -= 10

	pygame.display.update()

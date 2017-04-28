# Para criar texto

#def mensagem_tela (msg, cor, y_displace=0, size = 'small'):
	#smallfont = fpygame.font.SysFont('comicsamsms', 25)
	#medfont = fpygame.font.SysFont('comicsamsms', 50)
	#largefont = fpygame.font.SysFont('comicsamsms', 80)
	#texto_tela = font.render(msg, True, cor)
	#gameDisplay.blit(texto_tela, [display_widht/2, display_height/2])

	
	#caso o jogador perca

	#mensagem_tela('Loser :/', color='red')
	#pygame.display.update()
	#time.sleep(2)


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
#monstro_topo = tela.get_height() - monstro.get_height()
#monstro_centro = tela.get_width()/2 - monstro.get_width()/2

monstro = monstros(tela,"monstrinho.png")

#monstro = pygame.image.load("monstrinho.png")

tela.blit(nave, (nave_esq,nave_topo), )

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

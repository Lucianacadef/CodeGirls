import pygame , sys
from pygame.locals import *

def interseccao(s1_x, s1_y, s2_x, s2_y):
	return (s1_x > s2_x - 10) and \
	       (s1_y > s2_y - 10) and \
	       (s1_x < s2_x + 10) and \
	       (s1_y < s2_y + 10)

class monstros(pygame.sprite.Sprite):
	def __init__(self,tela,imagem, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.tela = tela
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.passo = 0
		self.direcao = 1

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))

	def update(self):
		if self.passo == 10:
			self.direcao = -1
		elif self.passo == -10:
			self.direcao = 1
		self.passo += self.direcao
		self.rect.x += self.direcao
		# self.rect.x += 5
		# pygame.tima.delay(1000)
		# self.rect.x -=5
		# pygame.tima.delay(1000)
		# self.rect.x -=5
		# pygame.tima.delay(1000)
		# self.rect.x += 5


class shots(pygame.sprite.Sprite):
	def __init__(self,tela,imagem):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.tela = tela
		
	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))
	def update(self):
		self.rect.y += 10


clock = pygame.time.Clock()
tela = pygame.display.set_mode((800,600))
pygame.mouse.set_visible(0)


nave = pygame.image.load("nave_pequena.png")
nave_topo = tela.get_height() - nave.get_height()
nave_esq = tela.get_width()/2 - nave.get_width()/2
pygame.display.set_caption("Space invaders - Code Girls")

tela.blit(nave, (nave_esq,nave_topo))

background = pygame.image.load("espaco.jpg")

# lista_monstros = []
# for i in range(400,560,40):
# 	for j in range(-300,300,40):
# 		novo_monstro = monstros(tela,"monstrinho.png", j, -i)
# 		lista_monstros.append(novo_monstro)

for i in range(400,560,40):
	for j in range(-300,300,40):
		novo_monstro = monstros(tela,"monstrinho.png", j, -i)
		grupo_monstro = pygame.sprite.Group()
		grupo_monstro.add(novo_monstro)

tiro = shots(tela,"shot.png")
atirar_y = 0
atirar_x = 0
#tiros = []
grupo_tiros = pygame.sprite.Group()

while True:

	clock.tick(60)
	tela.blit(background, (0, 0))

	x,y = pygame.mouse.get_pos()
	tela.blit(nave, (x-nave.get_width()/2,nave_topo))

	grupo_monstro.update()

	grupo_monstro.draw(tela)

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:
			# tiros.append([event.pos[0],500])
			# for t in tiros:
			tiro.posicao(x,nave_topo)
			grupo_tiros.add(tiro)
			grupo_tiros.draw(tela)

			# for b in range(len(tiros)):
			# 	tiros[b][0]-=10

			# for t in tiros:
			# 	if t[0]<0:
			# 		tiros.remove(t)


			#atirar_y = nave_topo
			#atirar_x = x
					

	#if atirar_y > 0:
		#tela.blit(tiro, (atirar_x,atirar_y))
		#atirar_y -= 15

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
	# monstros_atingidos = pygame.sprite.spritecollide(grupo_tiros,grupo_monstro,True)
	# for monstro in monstros_atingidos:
	# 	grupo_monstro.kill(monstro)


	# lista_sobreviventes = []
	# for k in range(len(grupo_monstro)):
	# 	monstro = grupo_monstro[k]
	# 	if not interseccao(monstro.rect.x, monstro.rect.y, atirar_x, atirar_y):
	# 		lista_sobreviventes.append(k)

	# monstros_restantes = []
	# for k in lista_sobreviventes:
	# 	monstros_restantes.append(lista_monstros[k])

	# lista_monstros = monstros_restantes

	

	pygame.display.update()
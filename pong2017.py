#-*- coding: UTF-8 -*-
# Importamos las bibliotecas.
import pygame
import sys, os
# Desde alli elegimos que importar.
from pygame.locals import *

# Centralizado de ventana (Debe ir antes que la misma).
x = 180
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# FPS (Cuadros por Segundo).
clock = pygame.time.Clock()
FPS = 60

# Establecemos variables para la ventana y creamos la misma con un Nombre.
ancho = 640
alto = 480
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Pong 2017")
pygame.key.set_repeat(1,1)

# Creamos las Paletas.
paletajugador1 = pygame.image.load("02 Imagenes/Paleta Pong.png")
paletajugador2 = pygame.image.load("02 Imagenes/Paleta Pong.png")

# Creamos el Rectangulo para cada Paleta.
sprite_paletajugador1 = pygame.sprite.Sprite()
sprite_paletajugador1.image = paletajugador1
sprite_paletajugador1.rect = paletajugador1.get_rect()
sprite_paletajugador2 = pygame.sprite.Sprite()
sprite_paletajugador2.image = paletajugador2
sprite_paletajugador2.rect = paletajugador2.get_rect()
sprite_paletajugador2.centery = sprite_paletajugador2.rect.height/2
# Posicion y Movimiento.
sprite_paletajugador1.rect.x = 100
sprite_paletajugador1.rect.y = 200
sprite_paletajugador2.rect.x = 550
sprite_paletajugador2.rect.y = 200
paletaJ1_velY = 15
paletaJ2_velY = 15

# Creamos la Pelota.
pelota = pygame.image.load("02 Imagenes/Pelota Pong.png")
sprite_pelota = pygame.sprite.Sprite()
sprite_pelota.image = pelota
sprite_pelota.rect = pelota.get_rect()
# Posicion y Movimiento.
sprite_pelota.rect.x = 200
sprite_pelota.rect.y = 200
pelota_velX = 15
pelota_velY = 15

# Cargamos la imagen para el Fondo.
fondo = pygame.image.load("02 Imagenes/Fondo Pong.jpg")



while True:
	# Relación de eventos y comandos.
	if pygame.event.get(pygame.QUIT):
		break
	if pygame.event.get(pygame.MOUSEMOTION):
		posicion = pygame.mouse.get_pos()
		print "Posicion:",posicion
#	pygame.event.pump()

	for evento in pygame.event.get():
		teclas = pygame.key.get_pressed()
		if evento.type == QUIT:
			sys.exit()
		if evento.type == pygame.KEYDOWN:
			if teclas[K_DOWN]:
				sprite_paletajugador1.rect.y += paletaJ1_velY
			if teclas[K_UP]:
				sprite_paletajugador1.rect.y -= paletaJ1_velY

	# Presentamos la imagen de Fondo.
	pantalla.blit(fondo,(0,0))
	# Presentamos la imagen de la Paleta de Jugadores y su Movimiento.
	# La tupla posiciona el objeto según los valores (X,Y) 
	pantalla.blit(sprite_paletajugador1.image,(sprite_paletajugador1.rect))
	pantalla.blit(sprite_paletajugador2.image,(sprite_paletajugador2.rect))
#	sprite_paletajugador1.rect.y += paletaJ1_velY
#	sprite_paletajugador2.rect.y += paletaJ2_velY
	# Vinculamos la posicion de la pelota con el centro de la Paleta2
	sprite_paletajugador2.rect.centery = sprite_pelota.rect.centery
	# Relacion con los Limites de la pantalla.
	if sprite_paletajugador1.rect.y + sprite_paletajugador1.rect.height > alto:
		sprite_paletajugador1.rect.y = alto-sprite_paletajugador1.rect.height
	if sprite_paletajugador1.rect.y < 0:
		sprite_paletajugador1.rect.y = 0
	if sprite_paletajugador2.rect.y + sprite_paletajugador2.rect.height > alto:
		sprite_paletajugador2.rect.y = alto-sprite_paletajugador2.rect.height
	if sprite_paletajugador2.rect.y < 0:
		sprite_paletajugador2.rect.y = 0
	
	# Presentamos la imagen de la Pelota y su Movimiento.
	pantalla.blit(sprite_pelota.image,(sprite_pelota.rect))
	sprite_pelota.rect.x += pelota_velX
	sprite_pelota.rect.y += pelota_velY
	
	# Relacion con los Limites de la pantalla.
	if sprite_pelota.rect.x + sprite_pelota.rect.width > ancho:
		pelota_velX = pelota_velX*-1
	if sprite_pelota.rect.x < 10:
		pelota_velX = pelota_velX*-1

	if sprite_pelota.rect.y + sprite_pelota.rect.height > alto:
		pelota_velY = pelota_velY*-1
	if sprite_pelota.rect.y < 10:
		pelota_velY = pelota_velY*-1

	# Colision de Sprites.
	if sprite_pelota.rect.colliderect(sprite_paletajugador1):
		pelota_velX = pelota_velX*-1
		print "COLISION 1"
	if sprite_pelota.rect.colliderect(sprite_paletajugador2):
		pelota_velX = pelota_velX*-1
		print "COLISION 2"

	clock.tick(FPS)
	
	# Actualizamos para ver los cambios.
	pygame.display.update()

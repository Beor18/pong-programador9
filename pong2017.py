#-*- coding: UTF-8 -*-
# Importamos las bibliotecas.
import pygame
import sys, os
# Desde alli elegimos que importar.
from pygame.locals import *

#Inicializamos la libreria:
pygame.init()

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

# Cargamos la imagen para el Fondo.
fondo = pygame.image.load("02 Imagenes/Fondo Pong.jpg")

# Creamos las Paletas.
paletajugador1 = pygame.image.load("02 Imagenes/Paleta Pong.png")
paletajugador2 = pygame.image.load("02 Imagenes/Paleta Pong.png")

# Creamos el Rectangulo para cada Paleta.
sprite_paletajugador1 = pygame.sprite.Sprite()
sprite_paletajugador1.image = paletajugador1
sprite_paletajugador1.rect = paletajugador1.get_rect()
sprite_paletajugador1.centery = sprite_paletajugador1.rect.height/2
sprite_paletajugador2 = pygame.sprite.Sprite()
sprite_paletajugador2.image = paletajugador2
sprite_paletajugador2.rect = paletajugador2.get_rect()
sprite_paletajugador2.centery = sprite_paletajugador2.rect.height/2
# Posicion y Movimiento.
sprite_paletajugador1.rect.x = 80
sprite_paletajugador1.rect.y = 200
sprite_paletajugador2.rect.x = 560
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
pelota_velX = 10
pelota_velY = 10

#Inicializamos las fuentes:
pygame.font.init()
fuente = pygame.font.Font(None,30)
texto1 = fuente.render("Puntaje J1",0,(255,255,255))
texto2 = fuente.render("Puntaje J2",0,(255,255,255))
puntosj1 = 0
puntosj2 = 0

while True:
	# Relación de eventos y comandos.
	for evento in pygame.event.get():
		teclas = pygame.key.get_pressed()
		if evento.type == QUIT:
			sys.exit()
		if evento.type == KEYDOWN:
			if teclas[K_s]:
				sprite_paletajugador1.rect.y += paletaJ1_velY
			if teclas[K_w]:
				sprite_paletajugador1.rect.y -= paletaJ1_velY
			if teclas[K_UP]:
				sprite_paletajugador2.rect.y -= paletaJ2_velY
			if teclas[K_DOWN]:
				sprite_paletajugador2.rect.y += paletaJ2_velY
#		if evento.type == MOUSEMOTION:
#			posicion = pygame.mouse.get_pos()

	# Presentamos la imagen de Fondo.
	pantalla.blit(fondo,(0,0))
	# Presentamos la imagen de la Paleta de Jugadores y su Movimiento.
	# La tupla posiciona el objeto según los valores (X,Y) 
	pantalla.blit(sprite_paletajugador1.image,(sprite_paletajugador1.rect))
	pantalla.blit(sprite_paletajugador2.image,(sprite_paletajugador2.rect))
#	sprite_paletajugador1.rect.y += paletaJ1_velY
#	sprite_paletajugador2.rect.y += paletaJ2_velY
	# Vinculamos la posicion Paletas con otra cosa.
#	sprite_paletajugador1.rect.centery = sprite_pelota.rect.centery
#	sprite_paletajugador2.rect.centery = sprite_pelota.rect.centery
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
		puntosj1 += 1
	if sprite_pelota.rect.x < 10:
		pelota_velX = pelota_velX*-1
		puntosj2 += 1
		
	if sprite_pelota.rect.y + sprite_pelota.rect.height > alto:
		pelota_velY = pelota_velY*-1
	if sprite_pelota.rect.y < 10:
		pelota_velY = pelota_velY*-1

	# Colision de Sprites.
	if sprite_pelota.rect.colliderect(sprite_paletajugador1):
		pelota_velX = (pelota_velX-1)*-1
		print "COLISION 1"
		print "VelX:",pelota_velX,"VelY",pelota_velY
	if sprite_pelota.rect.colliderect(sprite_paletajugador2):
		pelota_velX = (pelota_velX+1)*-1
		print "COLISION 2"
		print "VelX:",pelota_velX,"VelY",pelota_velY
	
	#Ubicamos la fuente del Puntaje y el Puntaje:
	pantalla.blit(texto1,(ancho/2-200,10))
	pantalla.blit(texto2,(ancho/2+100,10))
	puntajej1 = fuente.render(str(puntosj1),0,(20,20,255))
	puntajej2 = fuente.render(str(puntosj2),0,(255,20,20))
	pantalla.blit(puntajej1,(ancho/2-90,10))
	pantalla.blit(puntajej2,(ancho/2+210,10))

	clock.tick(FPS)
	
	# Actualizamos para ver los cambios.
	pygame.display.update()

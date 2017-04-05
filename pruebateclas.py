import pygame
pygame.init()
screen = pygame.display.set_mode((680, 460))
clock = pygame.time.Clock()

# use a rect since it will greatly 
# simplify movement and drawing
paddle = pygame.Rect((0, 0, 100, 80))

while True:

    if pygame.event.get(pygame.QUIT): break
    pygame.event.pump()

    # move up/down by checking for pressed keys
    # and moving the paddle rect in-place
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: paddle.move_ip(0, -7)
    if keys[pygame.K_DOWN]: paddle.move_ip(0, 7)
    if keys[pygame.K_RIGHT]: paddle.move_ip(7, 0)
    if keys[pygame.K_LEFT]: paddle.move_ip(-7, 0)

    # ensure the paddle rect does not go out of screen
    paddle.clamp_ip(screen.get_rect())

    screen.fill((0,0,0))    
    pygame.draw.rect(screen, (255,255,255), paddle)
    pygame.display.flip()

    clock.tick(60)

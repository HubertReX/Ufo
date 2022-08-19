from cgi import test
import pygame
from sys import exit

gam_title = "Gra UFO"
napis = "Autor: Mateusz"
pygame.init()

szerokosc = 800
wysokosc  = 400
screen = pygame.display.set_mode((szerokosc,wysokosc) )
pygame.display.set_caption(gam_title)
clock = pygame.time.Clock()

tlo = pygame.image.load('graphics/Sky.png').convert()
ziemia = pygame.image.load('graphics/ground.png').convert()
slimak = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
gracz = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
gracz_rect = gracz.get_rect(midbottom = (80,300))

# test_surface = pygame.Surface((100,200))
# test_surface.fill(pygame.Color(255,166,0))

# dot_surface = pygame.Surface((5,5))
# dot_surface.fill(pygame.Color(0,255,0))

czcionka = pygame.font.Font("font/Pixeltype.ttf", 50)
text = czcionka.render(napis, False, "Green")

pozycja_x = 0
predkosc = 4
kierunek = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    if keys[pygame.K_LEFT]:
        gracz_rect.left -= 5

    if keys[pygame.K_RIGHT]:
        gracz_rect.left += 5

    pozycja_x = pozycja_x + predkosc*kierunek
    if pozycja_x > szerokosc/2 - 100/2:
        #pozycja_x = 0
        kierunek = -1
    
    if pozycja_x < -(szerokosc/2 - 100/2):
        kierunek = 1

    screen.blit(tlo, (0,0))
    screen.blit(ziemia, (0,300))
    screen.blit(text, (300, 50))
    screen.blit(slimak, (pozycja_x + szerokosc/2 -72/2, 265))
    screen.blit(slimak, (pozycja_x + 150 + szerokosc/2 -72/2, 265))
    
    screen.blit(gracz, gracz_rect)
    
    #screen.blit(test_surface, (pozycja_x + szerokosc/2 - 100/2, wysokosc/2 - 200/2))
    #screen.blit(dot_surface, (pozycja_x + szerokosc/2 - 5/2, wysokosc/2 - 5/2))

    pygame.display.update()
    clock.tick(60)


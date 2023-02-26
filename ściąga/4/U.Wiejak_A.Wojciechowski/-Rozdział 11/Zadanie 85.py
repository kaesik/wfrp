import pygame
import time
#zmienne
pygame.font.init()
tytul = "tekst"
czcionka = pygame.font.SysFont("Arial Narrow", 50)
odliczanie = 50

#ekran
okno = pygame.display.set_mode([400,300])
#tytuł
pygame.display.set_caption(tytul)
#kod
while odliczanie > 0:
	okno.fill([0,0,0])
	pygame.draw.circle(okno,[255,255,255],[200,150], odliczanie*2)
	napis = czcionka.render(str(odliczanie), False, [0, 0, 255])
	okno.blit(napis,[185,125])
	pygame.display.flip()
	odliczanie -= 1
	time.sleep(0.2)
#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
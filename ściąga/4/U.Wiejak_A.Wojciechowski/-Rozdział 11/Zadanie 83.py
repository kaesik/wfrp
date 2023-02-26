import pygame
import time
#zmienne
pygame.font.init()
tytul = "tekst"
tekst = input("Co mam wyświtlić: ")
czcionka = pygame.font.SysFont("Arial Narrow", 50)
napis = czcionka.render(tekst, False, [0,0,255])
#ekran
okno = pygame.display.set_mode([400,300])
#tytuł
pygame.display.set_caption(tytul)
#kod

okno.blit(napis,[0,0])
pygame.display.flip()

#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
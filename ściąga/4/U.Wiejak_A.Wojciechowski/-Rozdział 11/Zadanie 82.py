import pygame
import random
import time
'''#zmienne
tytul = "Obraz"
#ekran
okno = pygame.display.set_mode([300,400])
#tytuł
pygame.display.set_caption(tytul)
#obrazek
obrazek = pygame.image.load("sponge.jpg")
okno.blit(obrazek,[0,0])
pygame.display.flip()
#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False'''
#zmienne
tytul = "zmieniające się obrazki"
nazwa = ["image1.jpg","image2.jpg","image3.jpg","image4.jpg","image5.jpg",]
#ekran
okno = pygame.display.set_mode([300,400])
#tytuł
pygame.display.set_caption(tytul)
#obrazek
while True:
	obrazek = pygame.image.load(nazwa[random.randint(0,4)])
	okno.blit(obrazek,[0,0])
	pygame.display.flip()
	time.sleep(3)
#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
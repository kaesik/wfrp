import pygame
import random
import time
#zmienne
tytul = "ruszający się obrazek"
#ważne aby wczytać obrazek
nazwa = pygame.image.load("icon.png")
vx = 1
vy = 1
x = 35
y = 30
#ekran
okno = pygame.display.set_mode([400,300])
#tytuł
pygame.display.set_caption(tytul)
#obrazek
while True:
	x += vx
	y += vy
	if x < 1:
		vx = 1
	elif x > 330:
		vx = -1
	if y < 1:
		vy = 1
	elif y > 240:
		vy = -1
	okno.fill([255,255,255])
	okno.blit(nazwa, [x,y])
	pygame.display.flip()
	time.sleep(0.03)

#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
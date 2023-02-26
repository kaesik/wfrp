import pygame

#initialize the screen
pygame.init()

#zmienne
x = 800
y = 800
title = "tytuł"

#create the screen
screen = pygame.display.set_mode((x, y))

#tile
pygame.display.set_caption(title)

#prostokąt
pygame.draw.rect(screen, [255,255,255], pygame.Rect(100,100,150,250))

#koło
pygame.draw.circle(screen, [0,255, 0], [400,300], 75)

#trójkąt
pygame.draw.polygon(screen, [255,0,0], [[175,175],[400,300],[300,0]])

#update
pygame.display.update()

#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
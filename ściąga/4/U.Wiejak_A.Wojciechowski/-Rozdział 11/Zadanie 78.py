import pygame

#initialize the screen
pygame.init()

#zmienne
wysokość = 800
szerokość = 600
title = "tytuł"

#create the screen
screen = pygame.display.set_mode((szerokość, wysokość))

#tile
pygame.display.set_caption(title)

#prostokąt
#pygame.draw.rect(screen, [255,255,255], pygame.Rect(100,100,150,250))

#koło
pygame.draw.circle(screen, [255,255,255], [300,600], 150)
pygame.draw.circle(screen, [255,255,255], [300,400], 100)
pygame.draw.circle(screen, [255,255,255], [300,275], 50)
pygame.draw.circle(screen, [0,0,0], [300,600], 10)
pygame.draw.circle(screen, [0,0,0], [300,550], 10)
pygame.draw.circle(screen, [0,0,0], [300,500], 10)
pygame.draw.circle(screen, [0,0,0], [300,450], 10)
pygame.draw.circle(screen, [0,0,0], [300,400], 10)
pygame.draw.circle(screen, [0,0,0], [275,250], 5)
pygame.draw.circle(screen, [0,0,0], [325,250], 5)

#trójkąt
pygame.draw.polygon(screen, [255,100,50], [[300,290],[300,270],[400,280]])

#update
pygame.display.update()

#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
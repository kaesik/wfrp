import random
import pygame
import time

#initialize the screen
pygame.init()

#zmienne
wysokość = 600
szerokość = 600
title = "losowe trójkąty"

#create the screen
screen = pygame.display.set_mode((szerokość, wysokość))

#tile
pygame.display.set_caption(title)

#prostokąt
#pygame.draw.rect(screen, [255,255,255], pygame.Rect(100,100,150,250))

while True:
	pygame.draw.polygon(screen, [random.randint(0,255), random.randint(0,255), random.randint(0,255)], [[random.randint(0,600), random.randint(0,600)], [random.randint(0,600), random.randint(0,600)], [random.randint(0,600), random.randint(0,600)], [random.randint(0,600), random.randint(0,600)], [random.randint(0,600), random.randint(0,600)]])
	pygame.display.update()
	time.sleep(1)

#koło
#pygame.draw.circle(screen, [255,255,255], [300,600], 150)

#trójkąt
#pygame.draw.polygon(screen, [255,100,50], [[300,290],[300,270],[400,280]])

#update
#pygame.display.update()

#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


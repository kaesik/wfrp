import pygame

#initialize the screen
pygame.init()

#zmienne
wysokosc = 800
szerokosc = 800
title = "animacja koła"
r = 25
x = 400
y = 25
z = 1
#create the screen
screen = pygame.display.set_mode((szerokosc, wysokosc))

#tile
pygame.display.set_caption(title)

#kształty
#pygame.draw.rect(screen, [255,255,255], pygame.Rect(100,100,150,250))
#pygame.draw.circle(screen, [255,255,255], [300,600], 150)
#pygame.draw.polygon(screen, [255,100,50], [[300,290],[300,270],[400,280]])
while True:
	screen.fill([0,0,0])
	pygame.draw.circle(screen, [255,255,255], [x,y], r)
	pygame.display.update()
	y =+ z
	if y < 25:
		z = 1
	elif y > 775:
		z = -1




#update
#pygame.display.update()

#ważne
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
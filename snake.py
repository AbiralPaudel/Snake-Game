import pygame
import random
import sys

width=25
tw=500
win=pygame.display.set_mode((tw,tw))
pygame.display.set_caption("Snake game")
dx=1
dy=0
f=tw//width
green=(0,255,0)
pygame.init()
body = [[10,10],[9,10]]
l=0


def redrawall(pos):
	global win
	win.fill((0,0,0))
	# x=0
	# y=0
	# for l in range(tw//width + 1):
	# 	pygame.draw.line(win,(255,255,255),(0,width*y),(tw,width*y))
	# 	pygame.draw.line(win,(255,255,255),(x*width,0),(x*width,tw))
	# 	x+=1
	# 	y+=1

	draw()

	draw_snack(pos)
	
	pygame.display.update()



def draw_snake(pos,eyes=False):
	global dx,dy
	dnx=pos[0]
	dny=pos[1]
	pygame.draw.rect(win,(0,255,0),(dnx*width+1,dny*width+1,width-2,width-2))

	if eyes:

		if dx == 1 and dy == 0:
			c1=((dnx+1)*width-8,(dny+1)*width-8)
			c2=((dnx+1)*width-8,(dny+1)*width-16)

		elif dx == -1 and dy == 0:
			c1=((dnx)*width+8,(dny)*width+8)
			c2=((dnx)*width+8,(dny)*width+16)

		elif dx == 0 and dy == 1:
			c1=((dnx+1)*width-8,(dny+1)*width-8)
			c2=((dnx+1)*width-16,(dny+1)*width-8)

		elif dx  == 0 and dy == -1:
			c1=((dnx)*width+8,(dny)*width+8)
			c2=((dnx)*width+16,(dny)*width+8)
	
		pygame.draw.circle(win,(0,0,255),c1,3)
		pygame.draw.circle(win,(0,0,255),c2,3)

	#pygame.display.update()



def get_dirn_snake():

	global dx,dy,body,f
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		pygame.init()

		keys = pygame.key.get_pressed()

		for key in keys:
			if keys[pygame.K_LEFT]:
				dx = -1
				dy = 0
				
			elif keys[pygame.K_RIGHT]:
				dx = 1
				dy = 0
			elif keys[pygame.K_UP]:
				dy = -1
				dx = 0
			elif keys[pygame.K_DOWN]:
				dy = 1
				dx = 0
	# l=len(body)
	# l-=1

	# for i in range(l,0,-1):
	# 	body[i][0]=body[i-1][0]
	# 	body[i][1]=body[i-1][1]

	# body[0][0] += dx
	# body[0][1] += dy

	endgamefortcube()

	#endgameaftertcube()


	if body[0][0]>=f:
		body[0][0]=0
		#game_over()
	elif body[0][0]<0:
		body[0][0]=f-1
		#game_over()
	if body[0][1]>=f:
		body[0][1]=0
		#game_over()
	elif body[0][1]<0:
		body[0][1]=f-1
		#game_over()		



def ran_snack():
	global body
	f = tw // width
	
	while True:
		x=random.randint(1,f-1)
		y=random.randint(1,f-1)
		flag=0
		for i,pos in enumerate(body):
			if pos == [x,y]:
				flag=1

		if flag==0:
			break

	return ([x,y])



def addcube():
	global body
	l=len(body)
	l-=1
	y=body[l][1]
	x=body[l][0]

	if body[l][1] < body[l-1][1]:
		if (y-1) == -1:
			y = width
		body.append([x,y-1])
	elif body[l][1] > body[l-1][1]:
		if (y+1) == width+1:
			y=-1
		body.append([x,y+1])
	elif body[l][0] < body[l-1][0]:
		if (x-1) == -1:
			x=width
		body.append([x-1,y])
	elif body[l][0] > body[l-1][0]:
		if (x+1) == width+1:
			x=-1
		body.append([x+1,y])


def draw():
	global body

	for i,pos in enumerate(body):
		if i == 0:
			draw_snake(pos,True)
		else:
			draw_snake(pos)


def draw_snack(pos):
	dnx=pos[0]
	dny=pos[1]
	pygame.draw.rect(win,(0,0,255),(dnx*width+2,dny*width+2,width-4,width-4))


def game_over():

	global win,tw,l,body,dx,dy
	pygame.init()
	win.fill((255,255,255))
	font = pygame.font.Font(None , 72)
	f = pygame.font.Font(None , 32)
	fo = pygame.font.Font(None , 22)
	text = font.render("Game Over",True,green)
	score = f.render("Score:  ",True,green)
	print_score = f.render(str(l),True,green)
	text_playagain = fo.render("Play again",True,(0,0,0))
	text_exit = f.render("Exit",True,(0,0,0))

	while True:

		get_event()

		win.fill((255,255,255))

		win.blit(text,(tw//2 - text.get_width()//2 ,tw//2-200))

		win.blit(score,(tw//2 - score.get_width()//2 ,tw//2-100))

		win.blit(print_score,(tw//2 + score.get_width()//2 ,tw//2-100))

		pygame.draw.rect(win,(0,255,0),(tw//2-40,tw//2,80,40))

		pygame.draw.rect(win,(255,0,0),(tw//2-40,tw//2+80,80,40))

		win.blit(text_playagain,(tw//2-35,tw//2+15))

		win.blit(text_exit,(tw//2-23,tw//2+90))

		pos = pygame.mouse.get_pos()

		click = pygame.mouse.get_pressed()

		if pos[0] >= 210 and pos[0] <= 290 and pos[1] >= 250  and pos[1] <= 290:
			pygame.draw.rect(win,(150,250,0),(tw//2-40,tw//2,80,40))

			win.blit(text_playagain,(tw//2-35,tw//2+15))

			if click[0] == 1:
				l=0
				dx=1
				dy=0
				body = [[10,10],[9,10]]
				start_game()



		if pos[0] >= 210 and pos[0] <= 290 and pos[1] >= 330 and pos[1] <= 370:
			pygame.draw.rect(win,(255,150,0),(tw//2-40,tw//2+80,80,40))
			win.blit(text_exit,(tw//2-23,tw//2+90))

			if click[0] == 1:
				exit_game()
				print(click)

		pygame.display.update()

		pygame.time.delay(50)




def start_menu():
	global win, tw, font
	pygame.init()

	win.fill((255,255,255))
	font = pygame.font.Font(None , 52)
	f = pygame.font.Font(None , 32)
	text = font.render("Welcome to Snake Game",True,green)
	tyes = f.render("Play",True,(0,0,0))
	tno = f.render("Exit",True,(0,0,0))
	image = pygame.image.load("download.jpg") 

	while True:

		get_event()
		
		win.fill((255,255,255))

		win.blit(text,(tw//2 - text.get_width()//2 ,tw//2-150))

		win.blit(image,(tw//2-90,tw//2-100))

		pos = pygame.mouse.get_pos()

		click = pygame.mouse.get_pressed()

		pygame.draw.rect(win,(0,255,0),(100,400,75,35))

		pygame.draw.rect(win,(255,0,0),(350,400,75,35))

		win.blit(tyes,(115 , 410))

		win.blit(tno,(365 , 410))

		if pos[0] >= 100 and pos[0] <= 175 and pos[1] >=400 and pos[1] <= 435:
			pygame.draw.rect(win,(150,250,0),(100,400,75,35))
			win.blit(tyes,(115 , 410))


			if click[0] == 1:
				return 1

		if pos[0] >= 350 and pos[0] <= 425 and pos[1] >=400 and pos[1] <= 435:
			pygame.draw.rect(win,(255,150,0),(350,400,75,35))
			win.blit(tno,(365 , 410))


			if click[0] == 1:
				return 0

		pygame.display.update()
		pygame.time.delay(50)



def start_game():
	global body,l
	pos = ran_snack()
	redrawall(pos)

	clock = pygame.time.Clock()

	while True:
		get_event()

		pygame.time.delay(50)

		clock.tick(12)

		get_dirn_snake()

		draw()

		if body[0][0] == pos[0] and body[0][1] == pos[1]:
			addcube()
			l+=1
			pos = ran_snack()
			draw_snack(pos)

		# a = body[0]

		# for i,p in enumerate(body):
		# 	if a == p and i!=0:
		# 		game_over()
		
		redrawall(pos)


def exit_game():
	pygame.init()
	pygame.quit()
	sys.exit()


def get_event():
	pygame.init()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				break


def endgamefortcube():
	global body,dx,dy
	l=len(body)
	l-=1

	c = body[0][0]
	d = body[0][1]


	body[0][0] += dx
	body[0][1] += dy
	a = body[0][0]
	b = body[0][1]

	for i,p in enumerate(body):
		if [a,b] == p and i!=0:
			game_over()

	for i in range(l,0,-1):
		body[i][0]=body[i-1][0]
		body[i][1]=body[i-1][1]

	body[1][0] = c
	body[1][1] = d


def endgameaftertcube():
	l=len(body)
	l-=1

	for i in range(l,0,-1):
		body[i][0]=body[i-1][0]
		body[i][1]=body[i-1][1]

	body[0][0] += dx
	body[0][1] += dy

	a = body[0]

	for i,p in enumerate(body):
		if a == p and i!=0:
			game_over()	


def main():

	s = start_menu()

	if  s == 0:
		exit_game()

	start_game()



main()
import pygame
print("")
print("Pynt! by Cass Gibson")
print("A really simple etch-a-sketch program that I made after")
print("watching the first episode in a Pygame tutorial series")
print("and nothing else. It's buggy, but it works, and I was")
print("able to write it in like an hour or two when I was drunk.")
print("")
print("")
print("Arrow keys move")
print("1-2-3 control size")
print("Q-W-E control white-red-black")
print("escape to clear")


# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pynt!')
running = True

#defines colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#drawing geometry parameters
x = 50
y = 50
width = 3
height = 3
vel = 2
size = 1
width1 = 2
height1 = 2

#color juggling
wantedcolor = white
dotcolor = wantedcolor

#gameloop
while running:
    #frame delay
    pygame.time.delay(64)

    #set the dot color to red for visibility
    dotcolor = (255, 0, 0)

    #Quit program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    #dot size
    if keys[pygame.K_1]:
        width = 3
        height = 3
        width1 = 2
        height1 = 2
        dotcolor = wantedcolor
        #sets small
        
    if keys[pygame.K_2]:
        width = 5
        height = 5
        width1 = 3
        height1 = 3
        dotcolor = wantedcolor
        #sets med

    if keys[pygame.K_3]:
        width = 9
        height = 9
        width1 = 5
        height1 = 5
        dotcolor = wantedcolor
        #sets large
        
    #dot color
    if keys[pygame.K_q]:
        wantedcolor = white

    if keys[pygame.K_w]:
        wantedcolor = red

    if keys[pygame.K_e]:
        wantedcolor = black        

    #dot move
    if keys[pygame.K_LEFT]:
        pygame.draw.rect(screen, wantedcolor, (x, y, width, height))
        x -= vel
        
    if keys[pygame.K_RIGHT]:
        pygame.draw.rect(screen, wantedcolor, (x, y, width, height))
        x += vel
        
    if keys[pygame.K_UP]:
        pygame.draw.rect(screen, wantedcolor, (x, y, width, height))
        y -= vel
        
    if keys[pygame.K_DOWN]:
        pygame.draw.rect(screen, wantedcolor, (x, y, width, height))
        y += vel

    if keys[pygame.K_ESCAPE]:
        screen.fill((0,0,0))
        x = 10
        y = 10
        
    #draw stuff
    if wantedcolor == red:  #sets cursor to white so that it's visible when using red
        pygame.draw.rect(screen, white, ((x + 1), (y + 1), width1, height1))
    if wantedcolor != red:
        pygame.draw.rect(screen, red, ((x + 1), (y + 1), width1, height1))
    pygame.display.update()
    
pygame.quit()

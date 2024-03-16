import pygame

# --- pygame setup ---

pygame.init()
canvas = pygame.Surface((560, 400))
screen = pygame.display.set_mode((640,480))
cursor = pygame.image.load('gfx\curs.png')

brush_sml = pygame.image.load('gfx/brush_small.png')
brush_sml_pressed = pygame.image.load('gfx/brush_small_pressed.png')

brush_med = pygame.image.load('gfx/brush_med.png')
brush_med_pressed = pygame.image.load('gfx/brush_med_pressed.png')

brush_lg = pygame.image.load('gfx/brush_large.png')
brush_lg_pressed = pygame.image.load('gfx/brush_large_pressed.png')

pynt_logo = pygame.image.load('gfx/pynt_logo.png')

sqicon_blank = pygame.image.load('gfx/sqicon_blank.png')
sqicon_blank_pressed = pygame.image.load('gfx/sqicon_blank_pressed.png')

pynt_icon = pygame.image.load('gfx/pynt_icon.png')

pygame.display.set_icon(pynt_icon)

pygame.display.set_caption('Pynt!')
running = True

canvas.fill((255,255,255,255))
screen.fill((125, 125, 125, 255))

#defines color palette
white = (255, 255, 255, 255)
red = (255, 0, 0, 255)
yellow = (255, 201, 14, 255)
black = (0, 0, 0, 255)
blank = (0, 0, 0, 0)
#drawing geometry parameters
vel = 2
size = 2
oldsize = 2

#color juggling
wantedcolor = black
dotcolor = wantedcolor

pygame.mouse.set_visible(False)

#gameloop!
#This is where the program actually runs.
while running:
    #blank UI layer
    screen.fill((200, 200, 200))

    #get mouse data
    mx, my = pygame.mouse.get_pos()

    #frame delay
    pygame.time.delay(1)

    #Quit program-
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check keys and mouse buttons being pressed!
    keys = pygame.key.get_pressed()
    mbtn = pygame.mouse.get_pressed()

    #dot size
    if keys[pygame.K_1]:
        size = 2
        oldsize = 2
        dotcolor = wantedcolor
        #sets small
        
    if keys[pygame.K_2]:
        size = 3
        oldsize = 3
        dotcolor = wantedcolor
        #sets med

    if keys[pygame.K_3]:
        size = 5
        oldsize = 5
        dotcolor = wantedcolor
        #sets large
        
    #dot color
    if keys[pygame.K_q]:
        wantedcolor = black

    if keys[pygame.K_w]:
        wantedcolor = white

    if keys[pygame.K_e]:
        wantedcolor = red
        
    if keys[pygame.K_r]:
        wantedcolor = yellow


    if keys[pygame.K_ESCAPE]:
        canvas.fill(white)

    #detect mouse presses
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        #if click on small button
        if (mx > 5 and mx < 37) and (my > 45 and my < 77):
            size = 2
            oldsize = 2
            dotcolor = wantedcolor
            #sets small

        #if click on med button
        if (mx > 5 and mx < 37) and (my > 82 and my < 114):
            size = 3
            oldsize = 3
            dotcolor = wantedcolor
            #sets med

        #if click on large button
        if (mx > 5 and mx < 37) and (my > 119 and my < 151):
            size = 5
            oldsize = 5
            dotcolor = wantedcolor
            #sets large

        #if click on black button
        if (mx > 5 and mx < 37) and (my > 156 and my < (156 + 32)):
            wantedcolor = black

        #if click on white button
        if (mx > 5 and mx < 37) and (my > 193 and my < (193 + 32)):
            wantedcolor = white

        #if click on red button
        if (mx > 5 and mx < 37) and (my > 230 and my < (230 + 32)):
            wantedcolor = red

        #if click on yellow button
        if (mx > 5 and mx < 37) and (my > 267 and my < (267 + 32)):
            wantedcolor = yellow

        pygame.draw.circle(canvas, wantedcolor, (mx - 40, my - 40), (size))
 
    if pygame.mouse.get_pressed(num_buttons=3)[2]:
        oldsize = size
        size = 9
        pygame.draw.circle(canvas, white, (mx - 40, my - 40), (size))

    screen.blit(canvas, (40, 40))
    screen.blit(pynt_logo, (0, 0))

    #set icons for size

    screen.blit(brush_sml, (5, 45))
    screen.blit(brush_med, (5, 82))
    screen.blit(brush_lg, (5, 119))
    screen.blit(sqicon_blank, (5, 156)) #black color button
    screen.blit(sqicon_blank, (5, 193)) #white color button
    screen.blit(sqicon_blank, (5, 230)) #red color button
    screen.blit(sqicon_blank, (5, 267)) #yellow color button
    
    #sets selected icon depending on size
    if (size == 2):
        screen.blit(brush_sml_pressed, (5, 45))
    if (size == 3):
        screen.blit(brush_med_pressed, (5, 82))
    if (size == 5):
        screen.blit(brush_lg_pressed, (5, 119))

    #sets selected icon depending on color
    if (wantedcolor == black):
        screen.blit(sqicon_blank_pressed, (5, 156)) #black color select
    if (wantedcolor == white):
        screen.blit(sqicon_blank_pressed, (5, 193)) #white color select
    if (wantedcolor == red):
        screen.blit(sqicon_blank_pressed, (5, 230)) #red color select
    if (wantedcolor == yellow):
        screen.blit(sqicon_blank_pressed, (5, 267)) #yellow color select


    pygame.draw.rect(screen, black, (9, 160, 24, 24))
    pygame.draw.rect(screen, white, (9, 197, 24, 24))
    pygame.draw.rect(screen, red, (9, 234, 24, 24))
    pygame.draw.rect(screen, yellow, (9, 271, 24, 24))
    #draw cursor for visibility
    pygame.draw.circle(screen, red, (mx, my), (size + 2), 2)
    pygame.draw.circle(screen, white, (mx, my), (size + 1), 2)


    size = oldsize

    screen.blit(cursor, (mx, my))
    pygame.display.flip()
    
pygame.quit()

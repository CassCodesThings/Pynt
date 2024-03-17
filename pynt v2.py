import pygame

# --- pygame setup ---

#sets surfaces and windows
pygame.init()
canvas = pygame.Surface((560, 400))
screen = pygame.display.set_mode((640,480))
cursor = pygame.image.load('gfx\curs.png')

#loading up all of the UI GFX
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

#set window icon and title

pygame.display.set_icon(pynt_icon)

pygame.display.set_caption('Pynt!')
running = True

#begin with a blank screen
canvas.fill((255,255,255,255))
screen.fill((125, 125, 125, 255))

#defines color palette
white = (255, 255, 255, 255)
red = (255, 0, 0, 255)
yellow = (255, 201, 14, 255)
black = (0, 0, 0, 255)
blank = (0, 0, 0, 0)
blue = (0, 123, 255, 255)

#drawing geometry parameters
vel = 2
size = 2
oldsize = 2

#color juggling
wantedcolor = black
dotcolor = wantedcolor

#sets the mouse to invisible for the custom cursor
pygame.mouse.set_visible(False)

# --- gameloop! ---
#This is where the program actually runs.
while running:

    #blank UI layer
    screen.fill((200, 200, 200))

    #get mouse data
    mx, my = pygame.mouse.get_pos()

    #frame delay
    pygame.time.delay(1)

    #Allows program to quit when the X button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check keys and mouse buttons being pressed
    keys = pygame.key.get_pressed()
    mbtn = pygame.mouse.get_pressed()

    #set dot size with keyboard
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

    if keys[pygame.K_t]:
        wantedcolor = blue

    if keys[pygame.K_ESCAPE]:
        canvas.fill(white)

    # - detect mouse presses -
    #
    #I want to clarify that the way that I have "clicking on buttons" set up is kind of horrifying.
    #This is almost definitely going to be reworked if and when I get around to the next version.
        
    #I need to set it up so that each button is a predefined object that has a location attribute and size
    #and then I need to make a simple function to check if it's pressed because the way it's done here
    #is just kind of if/then gore.
        
    #at any rate, most of the mx/my location checks are structured around the particular screen
    #location of the UI buttons with a lot of very conspicuous offsets and discrepancies allowing for
    #the spacing between the buttons as well as images and objects that are set within the buttons.
        
    #But it works for the time being.
    
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

        #if click on blue button
        if (mx > 5 and mx < 37) and (my > 304 and my < (304 + 32)):
            wantedcolor = blue

        pygame.draw.circle(canvas, wantedcolor, (mx - 40, my - 40), (size))
 
    #makes a big eraser brush when you right click
    if pygame.mouse.get_pressed(num_buttons=3)[2]:
        oldsize = size
        size = 9 #has to juggle the brush size here so that it can make the brush big while erasing but return it to normal
        pygame.draw.circle(canvas, white, (mx - 40, my - 40), (size))

    #blits the canvas and whatnot to the screen
    screen.blit(canvas, (40, 40))
    screen.blit(pynt_logo, (0, 0))

    screen.blit(brush_sml, (5, 45))
    screen.blit(brush_med, (5, 82))
    screen.blit(brush_lg, (5, 119))
    screen.blit(sqicon_blank, (5, 156)) #black color button
    screen.blit(sqicon_blank, (5, 193)) #white color button
    screen.blit(sqicon_blank, (5, 230)) #red color button
    screen.blit(sqicon_blank, (5, 267)) #yellow color button
    screen.blit(sqicon_blank, (5, 304)) #blue color button
    
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
    if (wantedcolor == blue):
        screen.blit(sqicon_blank_pressed, (5, 304)) #blue color select

    #draw colors on the color buttons
    pygame.draw.rect(screen, black, (9, 160, 24, 24))
    pygame.draw.rect(screen, white, (9, 197, 24, 24))
    pygame.draw.rect(screen, red, (9, 234, 24, 24))
    pygame.draw.rect(screen, yellow, (9, 271, 24, 24))
    pygame.draw.rect(screen, blue, (9, 308, 24, 24))

    #draw brush outline for visibility
    pygame.draw.circle(screen, red, (mx, my), (size + 2), 2)
    pygame.draw.circle(screen, white, (mx, my), (size + 1), 2)

    #reset size to the intended one after using the eraser
    size = oldsize

    screen.blit(cursor, (mx, my)) #draws custom cursor
    pygame.display.flip() #displays the frame
    
pygame.quit() #quits program when the loop is broken

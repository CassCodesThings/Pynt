import pygame
import random
# --- pygame setup ---

#sets surfaces and windows
pygame.init()
canvas = pygame.Surface((640-84, 400))
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
mystery_icon = pygame.image.load('gfx/mystery.png')

#set window icon and title
pygame.display.set_icon(pynt_icon)
pygame.display.set_caption('Pynt!')
running = True

#begin with a blank screen
canvas.fill((255,255,255,255))
screen.fill((125, 125, 125, 255))

#defines color palette as (r,g,b,a)
white = (255, 255, 255, 255)
red = (255, 0, 0, 255)
yellow = (255, 201, 14, 255)
black = (0, 0, 0, 255)
blank = (0, 0, 0, 0)
blue = (0, 123, 255, 255)
mysterycolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
#drawing geometry parameters
vel = 2
size = 2
oldsize = 2

#for random color generation
colorgen = False

#color juggling
wantedcolor = black
dotcolor = wantedcolor

#sets the mouse to invisible for the custom cursor
pygame.mouse.set_visible(False)

#let's create some UI classes!

#Okay, so, we're going to create a class for small UI buttons.
#This should make it much easier to define and work with clickable
#UI elements.
class smallButton:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

#And here's the clickcheck routine. It checks if a given button
#has been left-clicked. It returns True if it has, and False if it hasn't.
def clickcheck(button):
    x = button.x
    y = button.y
    width = button.width
    height = button.height
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        if ((mx > x and mx < x + width) and (my > y and my < y + height)):
            return True
        elif ((mx > x and mx < x + width) and (my > y and my < y + height)):
            return False

        
#Now let's set up some buttons to be used.
brushsmall = smallButton(5, 45, 32, 32)
brushmed = smallButton(5, 82, 32, 32)
brushlarge = smallButton(5, 119, 32, 32)
paintblack = smallButton(5, 156, 32, 32)
paintwhite = smallButton(5, 193, 32, 32)
paintred = smallButton(5, 230, 32, 32)
paintyellow = smallButton(5, 267, 32, 32)
paintblue = smallButton(5, 304, 32, 32)
paintmystery = smallButton(5, 341, 32, 32)
# --- gameloop! ---
#
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

    #let's draw some icons :3
    screen.blit(brush_sml, (5, 45))
    screen.blit(brush_med, (5, 82))
    screen.blit(brush_lg, (5, 119))
    screen.blit(sqicon_blank, (5, 156)) #black color button
    screen.blit(sqicon_blank, (5, 193)) #white color button
    screen.blit(sqicon_blank, (5, 230)) #red color button
    screen.blit(sqicon_blank, (5, 267)) #yellow color button
    screen.blit(sqicon_blank, (5, 304)) #blue color button
    screen.blit(sqicon_blank, (5, 341)) #MyStErY color


    #This defines a bunch of keyboard shortcuts for things
    #for dot size
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
    #for dot color
    if wantedcolor != mysterycolor:
        colorgen = False

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

    if keys[pygame.K_z]:
        if colorgen == False: #This basically makes it so that the mystery color doesn't regenerate after every frame, only when you first switch to Mystery
            mysterycolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
            colorgen = True
        wantedcolor = mysterycolor

    if keys[pygame.K_ESCAPE]:
        canvas.fill(white)

    # - detect mouse presses -
    if clickcheck(brushsmall) == True:
        size = 2
        oldsize = 2
        dotcolor = wantedcolor

    if clickcheck(brushmed) == True:
        size = 3
        oldsize = 3
        dotcolor = wantedcolor

    if clickcheck(brushlarge) == True:
        size = 5
        oldsize = 5
        dotcolor = wantedcolor

    if clickcheck(paintblack) == True:
        wantedcolor = black

    if clickcheck(paintwhite) == True:
        wantedcolor = white

    if clickcheck(paintred) == True:
        wantedcolor = red

    if clickcheck(paintyellow) == True:
        wantedcolor = yellow

    if clickcheck(paintblue) == True:
        wantedcolor = blue

    if clickcheck(paintmystery) == True:
        if colorgen == False: #This basically makes it so that the mystery color doesn't regenerate after every frame, only when you first switch to Mystery
            mysterycolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
            colorgen = True
        wantedcolor = mysterycolor

    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        #this offset is because the canvas surface is offset from the screen overall
        #and smaller than it. Without the 40-pixel offset, the brush dot would be put in the wrong place.
        pygame.draw.circle(canvas, wantedcolor, (mx - 42, my - 40), (size))

    #makes a big eraser brush when you right click
    if pygame.mouse.get_pressed(num_buttons=3)[2]:
        oldsize = size
        size = 9 #has to juggle the brush size here so that it can make the brush big while erasing but return it to normal
        pygame.draw.circle(canvas, white, (mx - 42, my - 40), (size))

    #blits the canvas and whatnot to the screen
    screen.blit(canvas, (42, 40))
    screen.blit(pynt_logo, (0, 0))

    #highlights icon depending on size
    if (size == 2):
        screen.blit(brush_sml_pressed, (brushsmall.x, brushsmall.y))
    if (size == 3):
        screen.blit(brush_med_pressed, (brushmed.x, brushmed.y))
    if (size == 5):
        screen.blit(brush_lg_pressed, (brushlarge.x, brushlarge.y))

    #highlights icon depending on color
    if (wantedcolor == black):
        screen.blit(sqicon_blank_pressed, (paintblack.x, paintblack.y)) #black color select
    if (wantedcolor == white):
        screen.blit(sqicon_blank_pressed, (paintwhite.x, paintwhite.y)) #white color select
    if (wantedcolor == red):
        screen.blit(sqicon_blank_pressed, (paintred.x, paintred.y)) #red color select
    if (wantedcolor == yellow):
        screen.blit(sqicon_blank_pressed, (paintyellow.x, paintyellow.y)) #yellow color select
    if (wantedcolor == blue):
        screen.blit(sqicon_blank_pressed, (paintblue.x, paintblue.y)) #blue color select
    if (wantedcolor == mysterycolor):
            screen.blit(sqicon_blank_pressed, (paintmystery.x, paintmystery.y))

    #draw colors on the color buttons
    #(I really need to set this up differently)
    #as it stands right now it just draws a colored square in a location that I happened to know
    #is inset within the intended buttons, but it just looks like arbitrary gobbledygook
    pygame.draw.rect(screen, black, (9, 160, 24, 24))
    pygame.draw.rect(screen, white, (9, 197, 24, 24))
    pygame.draw.rect(screen, red, (9, 234, 24, 24))
    pygame.draw.rect(screen, yellow, (9, 271, 24, 24))
    pygame.draw.rect(screen, blue, (9, 308, 24, 24))
    screen.blit(mystery_icon, (5, 341)) #mystery question mark

    #draw brush outline for visibility
    pygame.draw.circle(screen, red, (mx, my), (size + 2), 2)
    pygame.draw.circle(screen, white, (mx, my), (size + 3), 2)
    pygame.draw.circle(screen, wantedcolor, (mx, my), (size + 1), 3)

    #reset size to the intended one after using the eraser
    size = oldsize

    screen.blit(cursor, (mx, my)) #draws custom cursor
    pygame.display.flip() #displays the frame

pygame.quit() #quits program when the loop is broken
# uhh pygame 
# me 
# how is it 2026 :pensive

import pygame

def game():
    pygame.init() 

# screen
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("pluh")

# variables

# running = True 
# clock = pygame.time.Clock() 

# loop

# while running:
    # for event in pygame.event.get():
        # if event.type == pygame.QUIT:
            # running = False

            # something fill screen

#    pygame.display.flip()  # Update the display
    # clock.tick(60)  # Limit to 60 FPS    

# a rough burger

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("burg")
clock = pygame.time.Clock()
running = True

def burger():   

    pygame.draw.ellipse(screen, (210, 180, 140), (200, 120, 200, 60))
    pygame.draw.rect(screen, (0, 200, 0), (200, 170, 200, 10))
    pygame.draw.rect(screen, (90, 60, 30), (200, 180, 200, 25))
    pygame.draw.rect(screen, (255, 200, 0), (200, 205, 200, 10))
    pygame.draw.ellipse(screen, (210, 180, 140), (200, 210, 200, 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))
    burger()
    pygame.display.flip()
    clock.tick(60) 
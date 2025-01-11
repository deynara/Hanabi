#source venv/bin/activate
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Hanabi!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    cards_deck = []
    cards_discard = []


    pygame.display.init()
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #make quitbutton actually work
                return
        screen.fill((0,0,0)) #fill screen black

if __name__ == "__main__":
    main()
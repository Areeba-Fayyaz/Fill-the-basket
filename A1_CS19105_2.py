
import pygame
import os
import sys,time
import warnings
from A1_CS19105_3 import button
from A1_CS19105_4 import name
from A1_CS19105_5 import frame_for_highscore
from A1_CS19105_8 import score
#warnings.filterwarnings('ignore',category=DeprecationWarning)
pygame.init()


def mainmenu():
    '''This function displays the mainmenu'''
    
    #defining colors
    antique=pygame.Color('steelblue')
    grey=pygame.Color('grey65')
    clock=pygame.time.Clock()
    #setting screen size
    screen=pygame.display.set_mode((1000,800))
    #setting title
    pygame.display.set_caption('Fill the basket')
    #loading picture for the background
    background_image=pygame.image.load('A1_CS19105_9/stage.png').convert()

    #to force game to stay open long enough to be visible we have to use
    #a loop otherwise it will only last for a few milliseconds only.
    main=True
    while main==True:
        #drawing Play and highscore buttons with the help of class button.
        play_button=button(370,500,270,90,'Play',screen,antique,change_c=grey)
        play_button.drawbutton()
        highscores_button=button(370,600,270,95,'Highscores',screen,antique,change_c=grey)
        highscores_button.drawbutton()
        
        for event in pygame.event.get():
            #if user chooses to quit
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if user chooses to minimize   
            if event.type==0:
                pygame.display.iconify()

            pos=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEMOTION:
                if play_button.isOver(pos):
                    play_button.changecolor()
                if highscores_button.isOver(pos):
                    highscores_button.changecolor()
                    
            if event.type==pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos):
                    score.scores=0
                    enter_name=name(screen)
                    if enter_name.menu=='Exit':
                        mainmenu()
                if highscores_button.isOver(pos):
                    highscores=frame_for_highscore(screen)
                    if highscores.exit=='Exit':
                        mainmenu()
    
        pygame.display.flip()
        clock.tick(10)
        screen.blit(background_image,(0,0))




        



    
        

        

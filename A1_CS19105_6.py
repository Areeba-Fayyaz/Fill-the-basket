#this file contains classes used in the game Frame
import pygame,sys,time
pygame.init()
from A1_CS19105_8 import *
from A1_CS19105_3 import button



#______________CLASS frame_for_game_____________       
        
class frame_for_game:
    '''this is a class for performing operations on frame for game'''
    level=1
    
    def __init__(self,s):
        self.screen=s
        self.white=[255,255,255]
        
        pygame.mixer.init()
        music=pygame.mixer.music.load('A1_CS19105_11\\gameMusic.ogg')
        pygame.mixer.music.play(-1)
        
        self.lives=Lives(self.screen)
        self.mainmenu=back_to_mainmenu(self.screen)
        self.pause_button=pause(self.screen)
        self.create_level=createLevel(self.screen,self.lives)
        self.exit=self.create_frame()
        
    def create_frame(self):
        '''function which runs the loop for game frame'''
        main=True
        while main==True:
            exit_=self.mainloop()
            if exit_=='Exit':
                return 'Exit',score.scores
            self.screen.fill([255,255,255])
            self.scores=score(self.screen)#printscores
            levels=self.create_level.createlevel_insideloop(self.scores,frame_for_game.level)
            to_do=levels(self.scores)
            if to_do=='again':
                f=frame_for_game(self.screen)
                if f.exit[0]=='Exit':
                    return 'Exit',score.scores
            #if point touches the basket then level will be upgraded 
            if to_do: 
                frame_for_game.level+=1
                message.count=0
                if frame_for_game.level==10:
                    self.endGame=End_game(self.screen,frame_for_game.level-1,'Congratulations!You have completed all the levels :D',score.scores,x1=206,sound='A1_CS19105_11\\kidsCheering.ogg',picture='A1_CS19105_9/partyEmoji.png')
                    if self.endGame.exit=='Exit':
                        return 'Exit',score.scores
                
            self.createline()
            self.place_level(self.create_level.lvl)
           
            self.mainmenu.print_button()
            self.pause_button.print_button()
            l=self.lives.print_lives(score.scores,self.create_level.lvl)#print_lives
            if l=='Exit':
                return 'Exit',score.scores
            

    def mainloop(self):
        '''function where event based desicions are taken'''
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==0:
                    pygame.display.iconify()
                
                Event(event,self.level,self.create_level)
                pos=pygame.mouse.get_pos()
                
                if event.type==pygame.MOUSEMOTION:
                    if self.mainmenu.isOver(pos) :
                        
                        self.mainmenu.changecolor()
                        self.mainmenu.message()
                        
                    if self.pause_button.isOver(pos) :
                        self.pause_button.changecolor()
                        self.pause_button.message()
    
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.mainmenu.isOver(pos):
                        self.endGame=End_game(self.screen,self.create_level.lvl,'You have pressed the Main Menu button! :((',score.scores,x1=260)
                        if self.endGame.exit=='Exit':
                            return 'Exit'
                    if self.pause_button.isOver(pos) :
                        pygame.mixer.music.pause()
                        self.pause_button.paused()
        pygame.display.flip()
                
    def createline(self):
        '''function for drawing a line'''
        pygame.draw.line(self.screen,[0,0,0],[0,42],[1100,42],2)
        
    def place_level(self,levelno):
        '''function for displaying level number on the top of the frame
        Parameters:
        levelno(int): current level'''
        font=pygame.font.SysFont('calibri',32,True)
        text=font.render('Level '+str(levelno),1,[0,0,0],[255,255,255])
        self.screen.blit(text,(450,5))


        
                    
#________________CLASS Lives_________________________
        
class Lives:
    '''this is a class for performing operations on lives in the game'''
    lives=3
    
    def __init__(self,sc):
        self.screen=sc
        self.heart_image=pygame.image.load('A1_CS19105_9/heart.png').convert()
        self.heart_imagesm=pygame.transform.scale(self.heart_image,(38,38))
        
    def print_lives(self,scores,level):
        '''function to print lives
        Parameter:
        scores(int): current scores
        level(int): current level number'''
        self.levelno=level
        self.score=scores
        self.screen.blit(self.heart_imagesm,(140,2))
        self.print_livenum()
        e=self.endgame()
        if e=='Exit':
            return 'Exit'
        
    def print_livenum(self):
        '''function to print number of lives left'''
        font=pygame.font.SysFont('calibri',20)
        if Lives.lives<0:
            Lives.lives=0
        text=font.render(str(Lives.lives),1,[0,0,0],[255,255,255])
        self.screen.blit(text,(130,17))
        
    def decrement_lives(self):
        '''function to decrement lives'''
        Lives.lives-=1
        
    def endgame(self):
        '''function to end the game if no lives left'''
        if Lives.lives<=0:
            self.endGame=End_game(self.screen,self.levelno,'You have no lives left! :((',self.score)
            if self.endGame.exit=='Exit':
                return 'Exit'





            
#___________CLASS End_game___________      

class End_game:
    '''this is a class for maintaining frame when game ends'''

    def __init__(self,sc,lvlno,msg,score,x1=340,y1=300,sound='A1_CS19105_11\\losingSound.ogg',picture='A1_CS19105_9/brokenheart.png'):
        '''class constructor
        Parameters:
        sc: screen on which end game frame is displayed
        lvlno(int): current level number
        msg(str): message to be displayed in the frame
        score(int): current scores
        x1: x position of  the frame
        y1: y position of the  frame
        sound(str): sound to be played
        picture(str): picture to be displayed on the frame
        '''
        self.x=x1
        self.y=y1
        self.picture=picture
        self.screen=sc
        self.level=lvlno
        self.msg=msg
        self.scores=score
        pygame.mixer.init()
        music=pygame.mixer.music.load(sound)
        pygame.mixer.music.play(1)
        self.exit=self.create_frame()

    def create_frame(self):
        '''function which runs the loop when game ends'''
        main=True
        while main==True:
            self.frame()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==0:
                    pygame.display.iconify()
                pos=pygame.mouse.get_pos()
                if event.type==pygame.MOUSEMOTION:
                    if self.ok_button.isOver(pos) :
                        self.ok_button.changesqcolor()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.ok_button.isOver(pos):
                        Lives.lives=3
                        return 'Exit'
            pygame.display.flip()
            
    def place_text(self,backcolor,x,y,msg,f,bold=False):
        '''function for placing text
        Parameters:
        backcolor: background  color of the text
        x(int): x position of text
        y(int): y position of text
        msg(str): text to be displayed
        f(int or float): font size'''
        font=pygame.font.SysFont('calibri',f,bold)
        text=font.render(msg,1,[0,0,0],backcolor)
        self.screen.blit(text,(x,y))
        
    def frame(self):
        '''function for making frame'''
        pygame.draw.rect(self.screen,[255,239,219,255],(200,180,600,500))
        pygame.draw.rect(self.screen,[0,0,0],(200,180,600,500),4)
        pygame.draw.line(self.screen,[0,0,0],[200,230],[800,230],2)
        self.place_text([255,239,219,255],450,190,'Level '+str(self.level),32,True)
        self.message()
        self.image()
        self.score()
        self.OK()
        
    def OK(self):
        '''function for making OK button'''
        antique=pygame.Color('antiquewhite2')
        grey=pygame.Color('grey65')
        self.ok_button=button(450,600,90,36,'OK',self.screen,antique,20,'arial',2,grey)
        self.ok_button.drawsqbutton()
        
    def message(self):
        '''function for displaying message'''
        color=pygame.Color('lightsalmon1')
        self.place_text(color,self.x,self.y,self.msg,28)
        
    def score(self):
        '''function for displaying scores'''
        self.place_text([255,239,219,255],440,420,'Score(s) :',34)
        pygame.draw.rect(self.screen,[255,255,255],(400,470,200,40))
        self.place_text([255,255,255],450,480,str(self.scores),25)

    def image(self):
        '''function for loading and displaying image'''
        self.emoji=pygame.image.load(self.picture).convert()
        self.emoji_image=pygame.transform.scale(self.emoji,(40,40))
        self.screen.blit(self.emoji_image,(465,350))
    






#__________CLASS back_to_mainmenu__________
        
class back_to_mainmenu:
    '''This is a class which contains all the functionality of a mainmenu button'''

    def __init__(self,sc):
        self.screen=sc
        self.button()
        
    def button(self):
        '''function for loading images for main menu button'''
        self.backto_mainmenu=pygame.image.load('A1_CS19105_9/backto_mainmenu.png').convert()
        self.backto_mainmenu_image=pygame.transform.scale(self.backto_mainmenu,(100,30))
        self.chmainmenu=pygame.image.load('A1_CS19105_9/changemainmenu.png').convert()
        self.change_mainmenu_image=pygame.transform.scale(self.chmainmenu,(100,30))       
        self.fill_=pygame.draw.rect(self.screen,[0,0,0],[0,48,710,20])

    def print_button(self):
        '''function for displaying button'''
        self.drawoutline()
        self.screen.blit(self.backto_mainmenu_image,(7,8))
            
    def drawoutline(self):
        '''function for making button prettier by drawing outline'''
        pygame.draw.rect(self.screen,[0,0,0],[6,7,105,32],2)
        
    def fill(self):
        '''function which fills that region where message was displayed when
        the cursor was on the mainmenu button'''
        self.screen.fill([255,255,255],self.fill_)
        pygame.display.update(self.fill_)
        
    def isOver(self, pos):
        '''this function checks whether the position of cursor is
        outside the button(returns False) or on the button(returns True).
        Parameters:
        pos: pos is the mouse position or a tuple of (x,y) coordinates'''
        if (pos[0]>7)and pos[0]<(7+105):
            if pos[1]>8 and pos[1]<(8+32):
                return True
            
    def changecolor(self):
        '''it changes the color of the main menu button'''
        self.screen.blit(self.change_mainmenu_image,(7,8))
        self.drawoutline()
        pygame.display.flip()
        
    def message(self):
        '''function of displaying message, this function is called when the
        cursor is on the main menu button'''
        font=pygame.font.SysFont('calibri',15)
        text=font.render('Going back to main menu will end your Game!',1,[0,0,0],[238,223,204,255])
        self.screen.blit(text,(10,48))
        pygame.display.flip()
        time.sleep(0.6)
        
        
          




#_____________CLASS pause________________
        
class pause:
     '''This is a class which contains all the functionality of a pause button'''

     def __init__(self,sc):
        self.screen=sc
        self.button()
        
     def button(self):
        '''function for loading images for pause button'''
        self.pause=pygame.image.load('A1_CS19105_9/pause.png').convert()
        self.pause_image=pygame.transform.scale(self.pause,(30,30))
        self.chpause=pygame.image.load('A1_CS19105_9/changepause.png').convert()
        self.change_pause=pygame.transform.scale(self.chpause,(30,30))       
        self.fill_=pygame.draw.rect(self.screen,[0,0,0],[710,48,300,20])
          
     def print_button(self):
        '''function for displaying button'''
        self.screen.blit(self.pause_image,(710,8))
            
     def fill(self):
        '''function which fills that region where message was displayed when
        the cursor was on the pause button'''
        self.screen.fill([255,255,255],self.fill_)
        pygame.display.update(self.fill_)
        
     def isOver(self, pos):
        '''this function checks whether the position of cursor is
        outside the button(returns False) or on the button(returns True).
        Parameters:
        pos: pos is the mouse position or a tuple of (x,y) coordinates'''
        if (pos[0]>710)and pos[0]<(710+40):
            if pos[1]>8 and pos[1]<(8+32):
                return True
            
     def changecolor(self):
        '''it changes the color of the pause button'''
        self.screen.blit(self.change_pause,(710,8))
        pygame.display.flip()
        
     def message(self):
        '''function for displaying message of 'pause'  '''
        font=pygame.font.SysFont('calibri',15)
        text=font.render('Pause',1,[0,0,0],[238,223,204,255])
        self.screen.blit(text,(710,48))
        pygame.display.flip()
        time.sleep(0.6)
        
     def message_when_paused(self,msg,x,y,f):
        '''function for displaying message when pause  button is pressed
        x(int): x position of text
        y(int): y position of text
        msg(str): text to be displayed
        f(int or float): font size'''
        font=pygame.font.SysFont('calibri',f)
        text=font.render(msg,1,[0,0,0])
        self.screen.blit(text,(x,y))
   
     def paused(self):
        '''function which runs loop and called when the pause button is pressed'''
        paused_=True
        while paused_:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        pygame.mixer.music.unpause()
                        paused_=False
            self.message_when_paused('Paused',430,350,60)
            self.message_when_paused('Press "c" to continue',360,400,40)
            pygame.display.flip()
        

        
        
        
        

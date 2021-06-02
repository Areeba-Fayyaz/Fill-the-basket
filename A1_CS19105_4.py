#this file contains classes used in the frame for inputing name
import sys
import pygame,time
pygame.init()
from A1_CS19105_3 import button
from A1_CS19105_6 import *

#___________CLASS frame_for_entername__________

class frame_for_entername:
    '''this is a class to make a frame for inputing user's name if user
    presses the play button'''
    
    def __init__(self,screen):
        '''class constructor
        Parameters:
        screen: screen  on which the frame is displayed'''
        self.screen=screen
        self.white=[255,255,255]
        self.black=[0,0,0]
        self.user_input=''
        self.exit=self.create_frame()
        
    def create_frame(self):
        '''function for running the loop until user enters name and presses
        the  done button'''
        main=True
        while main==True:
            
            self.frame()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==0:
                    pygame.display.iconify()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_BACKSPACE:
                        self.user_input=self.user_input[0:-1]
                    else:
                        if self.check()==True:
                            self.user_input+=event.unicode
                    
                pos=pygame.mouse.get_pos()
                if event.type==pygame.MOUSEMOTION:
                    if self.done_button.isOver(pos) :
                        self.done_button.changesqcolor()
                    if self.cancel_button.isOver(pos) :
                        self.cancel_button.changesqcolor()
                        
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.done_button.isOver(pos):
                        if self.check_for_no_input()==True:
                            frame_for_game.level=1
                            start_game=frame_for_game(self.screen)
                            if start_game.exit[0]=='Exit':
                                return 'Exit',start_game.exit[1]
                    if self.cancel_button.isOver(pos):
                        return 'Exit' 
                            
            pygame.display.flip()
    
    def place_text(self,txt=0,x=338,y=420,f=32):
        '''function for placing text
        Parameters:
        txt(string):text to be displayed 
        x(int): x position of text
        y(int): y position of text
        f(int or float): font size'''
        if txt==0:
            txt=self.user_input
        font=pygame.font.SysFont('calibri',f)
        text=font.render(txt,1,self.black,self.white)
        self.screen.blit(text,(x,y))

    def frame(self):
        '''function for the setup of the frame'''
        pygame.draw.rect(self.screen,self.white,(300,350,400,160))
        pygame.draw.rect(self.screen,self.black,(300,350,400,160),4)
        pygame.draw.line(self.screen,self.black,[300,390],[700,390],2)
        pygame.draw.line(self.screen,self.black,[340,455],[660,455],3)
        font=pygame.font.SysFont('calibri',26)
        text=font.render('Enter your Name',1,self.black,self.white)
        self.screen.blit(text,(400,357))
        self.place_text()
        self.done()
        self.cancel()


    def check(self):
        '''function to check the user input's length '''
        if (len(self.user_input))>20:
            main=True
            start_time=time.time()
            while main==True:
                self.place_text("Cannot enter more than '20' characters!",330,460,20)
                if int(time.time()-start_time)>0.1:
                    break
                pygame.display.flip()
            return False
        return True

    def check_for_no_input(self):
        '''function to chech whether user enters something (returns True)
        or not (asks to enter name first and returns False) '''
        if (len(self.user_input))<=0:
            main=True
            start_time=time.time()
            while main==True:
                self.place_text("Please Enter Your Name First!",370,460,20)
                if int(time.time()-start_time)>0.1:
                    break
                pygame.display.flip()
            return False
        return True

    def done(self):
        '''function to create done button'''
        antique=pygame.Color('antiquewhite2')
        grey=pygame.Color('grey65')
        self.done_button=button (580,465,90,36,'Done',self.screen,antique,20,'arial',2,grey)
        self.done_button.drawsqbutton()

    def cancel(self):
        '''function to create cancel button'''
        antique=pygame.Color('antiquewhite2')
        grey=pygame.Color('grey65')
        self.cancel_button=button (330,465,90,36,'Cancel',self.screen,antique,20,'arial',2,grey)
        self.cancel_button.drawsqbutton()
        
     


#___________CLASS file___________
        
class file:
    '''this is a class to perform operations on a file'''
    
    def save_name_with_score(self,name,score,filename):
        '''write records to a file
        Parameters:
        name(str): name of the user
        score(int): final scores of the user
        filename(str): name of the file'''
        
        self.read_name_with_score(filename)
        if self.check_name(name,score)==False:
            self.namescore_list.append([name,score])
        self.namescore_list.sort(key=lambda x:x[1],reverse=True)
        f=open(filename,'w+')
        for record in self.namescore_list:
            f.write(str(record)+'\n')
        f.close()
        
    def read_name_with_score(self,filename):
        '''reads and returns as list all records from a file
        Each record is itself a list'''
        with open(filename,'a+') as f:
            self.namescore_list=[]
            f.seek(0)
            for record in f:
                try:
                    rec=eval(record.strip())
                    self.namescore_list+=[rec]
                except:
                    self.namescore_list=[]
                    
    def check_name(self,name,score):
        '''function to check whether the same name already exists in the file
        if True then it will update the score for that name, returns False otherwise 
        Parameters:
        name(str): name of the user
        score(int): final scores of the user'''
        i=0
        for rec in self.namescore_list:
            i+=1
            if name in rec:
                self.namescore_list[i-1][1]=score
                return True
        return False
        

#________________CLASS name__________________
    
class name(file):
    '''this class maintains the users name and score and saves in the file'''

    def __init__(self,sc,score=0):
        '''class constructor
        Parameters:
        sc: screen to perform operation on
        score(int): scores'''
        self.Score=score
        self.screen=sc
        self.menu=self.enternameFrame()
        
    def enternameFrame(self):#####
        '''create frame for inputing name from the user using class
        frame_for_entername and saves user's name with score in a file'''
        input_name=frame_for_entername(self.screen)
        name.playing=input_name.user_input
        self.Name=name.playing
        if input_name.exit[0]=='Exit':
            if input_name.exit[1]!=0:
                self.save_name_with_score(self.Name,input_name.exit[1],'A1_CS19105_10\\name_score_file.txt')
            return 'Exit'

    




    

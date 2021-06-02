#this file contains classes used in the highscore frame
import pygame,sys
pygame.init()
from A1_CS19105_6 import back_to_mainmenu
from A1_CS19105_4 import file

#________CLASS frame_for_highscore_________________

class frame_for_highscore:
    '''this is a class for displaying highscore frame if user presses the
    highscore button'''

    def __init__(self,sc):
        '''class constructor
        Parameters:
        sc: screen on which frame is displayed'''
        self.screen=sc
        self.mainmenu=back_to_mainmenu(self.screen)
        self.white=[255,255,255]
        
        self.highscores=operations_of_highscore(self.screen)
        self.exit=self.create_frame()
        
    def create_frame(self):
        '''this function contains theloop for displaying highscore screen'''
        self.screen.fill(self.white)
        self.createline()
        pygame.display.flip()
        main=True
        while main==True:
            exit_=self.mainloop()
            if exit_=='Exit':
                return 'Exit'
            self.mainmenu.print_button()
            pygame.display.flip()
            
    def mainloop(self):
        '''function where all the event based operations are performed which
        needs to be called inside the loop'''
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==0:
                    pygame.display.iconify()
                pos=pygame.mouse.get_pos()
                if event.type==pygame.MOUSEMOTION:
                    if self.mainmenu.isOver(pos) :
                        self.mainmenu.changecolor()
                    else:
                        self.mainmenu.fill()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.mainmenu.isOver(pos):
                        return 'Exit'
        self.highscores.print_highscores()
        
    def createline(self):
        '''draws the line in the highscore frame'''
        pygame.draw.line(self.screen,[0,0,0],[0,42],[1100,42],2)



#_____________CLASS operations_of_highscore________________

class operations_of_highscore:
    '''this class contains all the operations needs to be performed at the
    backend and on the front end of the frame for the highscores '''

    def __init__(self,sc):
        self.screen=sc
        
        self.f=file()
        self.f1=file()
        self.read()
        
    def read(self):
        '''reads from highscores.txt (where first five highscores with
        player names are stored) and  name_score_file.txt (where all players
        with their scores are stored)in highscoreRec_list and namescore_list
        respectively'''
        self.f.read_name_with_score('A1_CS19105_10\\name_score_file.txt')
        self.namescore_list=self.f.namescore_list
        if len(self.namescore_list)>5:
            for i in range(len(self.namescore_list)-5):
                self.namescore_list.pop()
        self.f1.read_name_with_score('A1_CS19105_10\\highscores.txt')
        self.highscoreRec_list=self.f1.namescore_list
        self.highscore_list=self.highscoreRec_list
        self.finalize_list()
        
    
    def check(self,name,score):
        '''function to check if highscoreRec_list's  name with score
        already exists in namescore_list then it will remove it from the
        highscoreRec_list'''
        i=0
        for rec in self.namescore_list :
            i+=1
            if name in rec and  score in rec:
                self.rem.append([name,score])
                
                
    def finalize_list(self):
        '''this function perform operations in order to get final highscoreRec_list
        with first five highscores with name'''
        self.rem=[]
        #if highscoreRec_list is empty or if both highscoreRec_list and
        #namescore_list are empty.
        if len(self.highscoreRec_list)==0:
            self.highscoreRec_list=self.namescore_list
           
        #if highscoreRec_list is not empty
        else:
            for record in self.highscore_list:
                self.check(record[0],record[1])
            for rec in self.rem:
                self.highscoreRec_list.remove(rec)
                
            #now after having all the unique names and scores in highscoreRec_list
            #we will append it in the namescore_list in order to get five max scores
            #from the list (i.e:namescore_list).
            self.namescore_list.extend(self.highscoreRec_list)
            self.highscoreRec_list=[]
            if len(self.namescore_list)>5:
                for i in range(5):
                    rec=max(self.namescore_list,key=lambda x:x[1])
                    self.highscoreRec_list.append(rec)
                    self.namescore_list.remove(rec)
            else:
                for i in range (len(self.namescore_list)):
                    rec=max(self.namescore_list,key=lambda x:x[1])
                    self.highscoreRec_list.append(rec)
                    self.namescore_list.remove(rec)
                    
                    
    def save_highscores(self):
        '''write records from highscoreRec_list to the file A1_CS19105_9.txt,
        each record is itself a list'''
        f=open('A1_CS19105_10\\highscores.txt','w+')
        for rec in self.highscoreRec_list:
            f.write(str(rec)+'\n')
        f.close()
        

    def highscore_heading(self):
        '''function to display highscores heading'''
        font=pygame.font.SysFont('calibri',40)
        text=font.render('Highscores',1,[0,0,0],[255,255,255])
        self.screen.blit(text,(400,300))
        
        
    def print_highscores (self):
        '''function to print highscores in the frame from highscoreRec_list'''
        i=1
        j=1
        self.save_highscores()
        self.highscore_heading()
        if len(self.highscoreRec_list)==0:
            font=pygame.font.SysFont('calibri',25)
            text=font.render('Play to make new highscores',1,[0,0,0],[238,223,204,255])
            self.screen.blit(text,(360,400))
            
        else:
            for rec in self.highscoreRec_list:
                font=pygame.font.SysFont('calibri',25)
                text=font.render((f'{j}. {rec[0]:2}  :   {rec[1]}'),1,[0,0,0],[255,255,255])
                self.screen.blit(text,(400,400+i))
                i+=26
                j+=1
            
        
        
        


                


            
                    
                    
                
                
            
            






        
                
    

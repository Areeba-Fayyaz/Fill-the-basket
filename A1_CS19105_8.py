#this file constains all the classes whichh is used in making levels
import pygame,sys,time
pygame.init()
from A1_CS19105_7 import *

#________________CLASS level1__________________

class level1:
    '''class for making level 1'''
    
    def __init__(self,sc,lives,msg):
        '''class constructor
        Parameters:
        sc: screen on which level should be displayed
        lives: object of class Lives
        msg: message to be displayed on the start of level'''
        self.screen=sc
        self.lives=lives

        self.outsideloop()
        self.Point=point(self.screen,msg,130,550)
        
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        self.basket=basket(self.screen,800,485)
        self.updown_obs1=updown_obstacle(self.screen,speed_y=4,steps=45)
        
    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_obs1=self.updown_obs1.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_basket=self.basket.print_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.createMaze()
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p or self.collision_with_walls() or self.collision_with_obs1:
            return True
        
    def createMaze(self):
        '''function to create maze'''
        pygame.draw.line(self.screen,[0,0,0],[100,600],[700,600],3)#1
        pygame.draw.line(self.screen,[0,0,0],[100,600],[100,500],3)#2
        pygame.draw.line(self.screen,[0,0,0],[100,500],[200,500],3)#3
        pygame.draw.line(self.screen,[0,0,0],[200,500],[200,555],3)#4
        pygame.draw.line(self.screen,[0,0,0],[200,555],[270,555],3)#5
        pygame.draw.line(self.screen,[0,0,0],[270,555],[270,380],3)#6
        pygame.draw.line(self.screen,[0,0,0],[270,380],[800,380],3)#7
        pygame.draw.line(self.screen,[0,0,0],[700,600],[700,430],3)#8
        pygame.draw.line(self.screen,[0,0,0],[750,430],[750,555],3)#9
        pygame.draw.line(self.screen,[0,0,0],[700,430],[750,430],3)#10
        pygame.draw.line(self.screen,[0,0,0],[800,380],[800,470],3)#11
        pygame.draw.line(self.screen,[0,0,0],[800,470],[900,470],3)#12
        pygame.draw.line(self.screen,[0,0,0],[750,555],[900,555],3)#13
        pygame.draw.line(self.screen,[0,0,0],[900,470],[900,555],3)#14

    def collision_with_walls(self):
        '''function which returns True and decrement life if collision of maze
        with point takes place'''
        for x1 in range (100,701):
            if self.Point.point_rect.collidepoint((x1,600)):
                    self.lives.decrement_lives()
                    return True
        for y2 in range (500,601):
            if self.Point.point_rect.collidepoint((100,y2)):
                    self.lives.decrement_lives()
                    return True
        for x3 in range (100,201):
            if self.Point.point_rect.collidepoint((x3,500)):
                    self.lives.decrement_lives()
                    return True
        for y4 in range (500,556):
            if self.Point.point_rect.collidepoint((200,y4)):
                    self.lives.decrement_lives()
                    return True
        for x5 in range (200,271):
            if self.Point.point_rect.collidepoint((x5,555)):
                    self.lives.decrement_lives()
                    return True
        for y6 in range (380,556):
            if self.Point.point_rect.collidepoint((270,y6)):
                    self.lives.decrement_lives()
                    return True
        for x7 in range (270,800):
            if self.Point.point_rect.collidepoint((x7,380)):
                    self.lives.decrement_lives()
                    return True
        for y8 in range (430,601):
            if self.Point.point_rect.collidepoint((700,y8)):
                    self.lives.decrement_lives()
                    return True
        for y9 in range (431,556):
            if self.Point.point_rect.collidepoint((750,y9)):
                    self.lives.decrement_lives()
                    return True
        for x10 in range (700,751):
            if self.Point.point_rect.collidepoint((x10,430)):
                    self.lives.decrement_lives()
                    return True
        for y11 in range (380,471):
            if self.Point.point_rect.collidepoint((800,y11)):
                    self.lives.decrement_lives()
                    return True
        for x12 in range (800,901):
            if self.Point.point_rect.collidepoint((x12,470)):
                    self.lives.decrement_lives()
                    return True
        for x13 in range (750,901):
            if self.Point.point_rect.collidepoint((x13,555)):
                    self.lives.decrement_lives()
                    return True
        for y14 in range (470,556):
            if self.Point.point_rect.collidepoint((900,y14)):
                    self.lives.decrement_lives()
                    return True





#________________CLASS level2__________________

class level2(level1):
    '''class for making level 2'''
    
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        level1.outsideloop(self)
        self.updown_obs2=updown_obstacle(self.screen,x1=500,speed_y=6,steps=31)

    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_obs1=self.updown_obs1.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.updown_obs2.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_basket=self.basket.print_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.createMaze()
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p or self.collision_with_walls() or self.collision_with_obs1 or self.collision_with_obs2:
            return True






#________________CLASS level3__________________

class level3(level1):
    '''class for making level 3'''
    
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        level1.outsideloop(self)
        self.updown_obs2=updown_obstacle(self.screen,x1=500,speed_y=6,steps=31)
        self.leftright_obs3=leftright_obstacle(self.screen,270,560,speed_x=5,steps=78)
        self.leftright_obs4=leftright_obstacle(self.screen,270,400,speed_x=3,steps=131)

    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_obs1=self.updown_obs1.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.updown_obs2.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs3=self.leftright_obs3.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs4=self.leftright_obs4.move_obs(self.Point.point_rect,self.lives)

        self.collision_with_basket=self.basket.print_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.createMaze()
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p or self.collision_with_walls() or self.collision_with_obs1 or self.collision_with_obs2 or self.collision_with_obs3 or self.collision_with_obs4:
            return True

    


#________________CLASS level4__________________

class level4:
    '''class for making level 4'''
    
    def __init__(self,sc,lives,msg):
        '''class constructor
        Parameters:
        sc: screen on which level should be displayed
        lives: object of class Lives
        msg: message to be displayed on the start of level'''
        self.screen=sc
        self.lives=lives
        
        self.Point=point(self.screen,msg,130,550)
        self.outsideloop()
        
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        self.basket=basket(self.screen,800,485)
        self.following_obs1=following_obstacle(self.screen)
        self.following_obs2=following_obstacle(self.screen,400,200)
        self.following_obs3=following_obstacle(self.screen,700,600)
  
    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_basket=self.basket.moving_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.collision_with_obs1=self.following_obs1.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.following_obs2.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs3=self.following_obs3.follow_point(self.Point.point_rect,self.lives)
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p or self.collision_with_obs1 or self.collision_with_obs2 or self.collision_with_obs3:
            return True





#________________CLASS level5__________________

class level5(level4):
    '''class for making level 5'''
    
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        level4.outsideloop(self)
        self.targeting_obs4=targeting_obstacle(self.screen)
        
    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_basket=self.basket.moving_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.collision_with_obs1=self.following_obs1.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.following_obs2.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs3=self.following_obs3.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs4=self.targeting_obs4.target_point(self.Point.point_rect,self.lives)
        
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p or self.collision_with_obs1 or self.collision_with_obs2 or self.collision_with_obs3 or self.collision_with_obs4 :
            return True
        
    


#________________CLASS level6__________________

class level6:
    '''class for making level 6'''
    
    def __init__(self,sc,lives,msg):
        '''class constructor
        Parameters:
        sc: screen on which level should be displayed
        lives: object of class Lives
        msg: message to be displayed on the start of level'''
        self.screen=sc
        self.lives=lives
      
        self.Point=point(self.screen,msg,130,550)
        self.outsideloop()
        
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        self.basket=basket(self.screen,860,470)
        self.following_obs1=following_obstacle(self.screen)
        self.following_obs2=following_obstacle(self.screen,400,200)
        self.following_obs3=following_obstacle(self.screen,700,600)
        self.updown_obs4=updown_obstacle(self.screen,730,speed_y=5,steps=40)
        self.leftright_obs5=leftright_obstacle(self.screen,770,580,speed_x=2,steps=90)
        self.leftright_obs6=leftright_obstacle(self.screen,770,380,speed_x=4,steps=50)
        self.rain_obs7=rain_obstacle(self.screen)
        self.rain_obs8=rain_obstacle(self.screen,3)
        self.rain_obs9=rain_obstacle(self.screen,4)
        self.rain_obs10=rain_obstacle(self.screen,6)
        self.rain_obs11=rain_obstacle(self.screen,6)
  
        
    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_basket=self.basket.print_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.collision_with_obs1=self.following_obs1.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.following_obs2.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs3=self.following_obs3.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs4=self.updown_obs4.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs5=self.leftright_obs5.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs6=self.leftright_obs6.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs7=self.rain_obs7.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs8=self.rain_obs8.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs9=self.rain_obs9.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs10=self.rain_obs10.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs11=self.rain_obs11.move_obs(self.Point.point_rect,self.lives)
       
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p or self.collision_with_obs1 or self.collision_with_obs2 or self.collision_with_obs3 or self.collision_with_obs4 or self.collision_with_obs5 or self.collision_with_obs6 or self.collision_with_obs7 or self.collision_with_obs8 or self.collision_with_obs9 or self.collision_with_obs10 or self.collision_with_obs11 :  
            return True





#________________CLASS level7__________________

class level7:
    '''class for making level 7'''
    
    def __init__(self,sc,lives,msg):
        '''class constructor
        Parameters:
        sc: screen on which level should be displayed
        lives: object of class Lives
        msg: message to be displayed on the start of level'''
        self.screen=sc
        self.lives=lives
      
        self.Point=point(self.screen,msg,130,550)
        self.outsideloop()
        
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        self.basket=basket(self.screen,860,470)
        self.following_obs1=following_obstacle(self.screen)
        self.following_obs2=following_obstacle(self.screen,400,200)
        self.following_obs3=following_obstacle(self.screen,700,600)
        self.rain_obs4=rain_obstacle(self.screen)
        self.rain_obs5=rain_obstacle(self.screen,3)
        self.rain_obs6=rain_obstacle(self.screen,4)
        self.rain_obs7=rain_obstacle(self.screen,6)
        self.rain_obs8=rain_obstacle(self.screen,2)
        self.rain_obs9=rain_obstacle(self.screen,10)
        self.rain_obs10=rain_obstacle(self.screen,5)
  
        
    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_basket=self.basket.moving_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.collision_with_obs1=self.following_obs1.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.following_obs2.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs3=self.following_obs3.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs4=self.rain_obs4.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs5=self.rain_obs5.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs6=self.rain_obs6.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs7=self.rain_obs7.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs8=self.rain_obs8.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs9=self.rain_obs9.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs10=self.rain_obs10.move_obs(self.Point.point_rect,self.lives)
       
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p  or self.collision_with_obs1 or self.collision_with_obs2 or self.collision_with_obs3 or self.collision_with_obs4 or self.collision_with_obs5 or self.collision_with_obs6 or self.collision_with_obs7 or self.collision_with_obs8 or self.collision_with_obs9 or self.collision_with_obs10:
            return True






#________________CLASS level8__________________

class level8:
    '''class for making level 8'''
    
    def __init__(self,sc,lives,msg):
        '''class constructor
        Parameters:
        sc: screen on which level should be displayed
        lives: object of class Lives
        msg: message to be displayed on the start of level'''
        self.screen=sc
        self.lives=lives
        
        self.Point=point(self.screen,msg,130,550)
        self.outsideloop()
        
    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        self.basket=basket(self.screen,860,470)
        self.following_obs1=following_obstacle(self.screen)
        self.following_obs2=following_obstacle(self.screen,400,200)
        self.targeting_obs3=targeting_obstacle(self.screen)   

    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_basket=self.basket.moving_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.collision_with_obs1=self.following_obs1.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.following_obs2.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs3=self.targeting_obs3.target_point(self.Point.point_rect,self.lives)
        self.laser=laser(self.screen)
        self.collision_with_obs4=self.laser.collision(self.lives,self.Point.point_rect)
     
        if self.Return():
            return 'again'

    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p  or self.collision_with_obs1 or self.collision_with_obs2 or self.collision_with_obs3 or self.collision_with_obs4:
            return True





#________________CLASS level9__________________

class level9:
    '''class for making level 9'''
    
    def __init__(self,sc,lives,msg):
        '''class constructor
        Parameters:
        sc: screen on which level 9 should be displayed
        lives: object of class Lives
        msg: message to be displayed on the start of level'''
        self.screen=sc
        self.lives=lives
        
        self.Point=point(self.screen,msg,130,550)
        self.outsideloop()

    def outsideloop(self):
        '''function which loads objects to be used in the level and will be
        called outside the loop'''
        self.basket=basket(self.screen,860,470)
        self.following_obs1=following_obstacle(self.screen)
        self.following_obs2=following_obstacle(self.screen,400,200)
        self.target_obs3=targeting_obstacle(self.screen,700,600)
        self.rain_obs4=rain_obstacle(self.screen)
        self.rain_obs5=rain_obstacle(self.screen,8)
        self.rain_obs6=rain_obstacle(self.screen,4)
        self.rain_obs7=rain_obstacle(self.screen,6)
        self.rain_obs8=rain_obstacle(self.screen,3)
        self.rain_obs9=rain_obstacle(self.screen,4)
        self.rain_obs10=rain_obstacle(self.screen,2)
  
    def insideloop(self,score):
        '''function to be called inside the loop'''
        self.scores=score
        self.p=self.Point.point_(self.lives)
        self.collision_with_basket=self.basket.moving_basket(self.Point.point_rect)
        if self.collision_with_basket:
            score.update_score(int(self.Point.number))
            return True
        self.collision_with_obs1=self.following_obs1.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs2=self.following_obs2.follow_point(self.Point.point_rect,self.lives)
        self.collision_with_obs3=self.target_obs3.target_point(self.Point.point_rect,self.lives)
        self.collision_with_obs4=self.rain_obs4.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs5=self.rain_obs5.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs6=self.rain_obs6.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs7=self.rain_obs7.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs8=self.rain_obs8.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs9=self.rain_obs9.move_obs(self.Point.point_rect,self.lives)
        self.collision_with_obs10=self.rain_obs10.move_obs(self.Point.point_rect,self.lives)
        self.laser=laser(self.screen)
        self.collision_with_obs11=self.laser.collision(self.lives,self.Point.point_rect)
    
        
        if self.Return():
            return 'again'
      
    def Return (self):
        '''function which returns True on any of the collision with point'''
        if self.p  or self.collision_with_obs1 or self.collision_with_obs2 or self.collision_with_obs3 or self.collision_with_obs4 or self.collision_with_obs5 or self.collision_with_obs6 or self.collision_with_obs7 or self.collision_with_obs8 or self.collision_with_obs9 or self.collision_with_obs10 or self.collision_with_obs11:
            return True

    
    






#________________CLASS createLevel__________________

class createLevel:
    '''this is class for maintaining levels'''
    def __init__(self,sc,lives):
        '''class constructor
        Parameter:
        sc: screen on which the levels should be displayed
        lives : object of class Lives'''
        self.screen =sc
        self.lives=lives
     
        self.level1=level1(self.screen,self.lives,'Use arrow keys and try not to cross the walls')
        self.level2=level2(self.screen,self.lives,'Pretty simple right? ;)')
        self.level3=level3(self.screen,self.lives,"Here's another!!")
        self.level4=level4(self.screen,self.lives,"Basket is moving away")
        self.level5=level5(self.screen,self.lives,"Avoid the cross sign")
        self.level6=level6(self.screen,self.lives,"Watch out the obstacle rain")
        self.level7=level7(self.screen,self.lives,"you are doing really well :D")
        self.level8=level8(self.screen,self.lives,"Watch out the deadly laser !!!")
        self.level9=level9(self.screen,self.lives,"Great job! You have reached the last level :D")
 
    def createlevel_insideloop(self,score,level):
        '''function which will be called inside the loop'''
        self.lvl=level
        if self.lvl ==1:
            return self.level1.insideloop# 
        if self.lvl==2:
            return self.level2.insideloop
        if self.lvl==3:
            return self.level3.insideloop
        if self.lvl==4:
            return self.level4.insideloop
        if self.lvl==5:
            return self.level5.insideloop
        if self.lvl==6:
            return self.level6.insideloop
        if self.lvl==7:
            return self.level7.insideloop
        if self.lvl==8:
            return self.level8.insideloop
        if self.lvl==9:
            return self.level9.insideloop
            




def Event(event,level,create_level):
    '''function to make point move in every level'''
    if level ==1:
        create_level.level1.Point.move(event)#
    if level ==2:
        create_level.level2.Point.move(event)
    if level ==3:
        create_level.level3.Point.move(event)
    if level ==4:
        create_level.level4.Point.move(event)
    if level ==5:
        create_level.level5.Point.move(event)
    if level ==6:
        create_level.level6.Point.move(event)
    if level ==7:
        create_level.level7.Point.move(event)
    if level ==8:
        create_level.level8.Point.move(event)
    if level ==9:
        create_level.level9.Point.move(event)
        
    
            


        
#________________CLASS score__________________

class score:
    '''class to perform functionality on scores'''
    scores=0
    def __init__ (self,Screen):
        self.screen=Screen
        self.print_score_on_top()
        
    def print_score_on_top (self):
        '''fucntion to print scores'''
        font=pygame.font.SysFont('calibri',20)
        text=font.render('Score(s) : '+str(score.scores),1,[0,0,0],[255,255,255])
        self.screen.blit(text,(750,17))

    def update_score(self,pointNo):
        '''function to calculate score'''
        score.scores+=pointNo*50
     
        

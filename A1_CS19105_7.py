#this file contains all the classes which is used in  the game frame for
#making levels.
import pygame ,sys,time,threading,random
pygame.init()
import math


#________________CLASS point_______________

class point:
    '''this is a class for performing functionality on the point'''
    
    def __init__(self,sc,msg,x1=100,y1=400):
        '''class constructor
        Parameters:
        sc(str): screen on which the point is displayed
        msg(str): message to appear on the start of every level
        x1(int): x position of point
        y1(int): y position of point'''
        
        self.screen=sc
        self.x=x1
        self.y=y1
        self.Msg=msg

        self.load_image()
        self.clock=pygame.time.Clock()
        self.x_change=0
        self.y_change=0
        
    def load_image(self):
        '''function to load image of a point'''
        points=['10','20','30','40','50']
        self.number=random.choice(points)
        self.point=pygame.image.load('A1_CS19105_9\\point'+self.number+'.png').convert()
        self.point_image=pygame.transform.scale(self.point,(30,30))
     
    def point_(self,lives):
        '''function for printing point on every new position
        Parameters:
        lives: object of class Lives'''
        self.x+=self.x_change
        self.y+=self.y_change
        msg=message(self.screen,self.Msg,self.x-70,self.y-30)
        self.print_point()
        #if point goes out of the frame of the screen then decrement lives
        if self.x>1000-30 or self.x<0 or self.y>800-30 or self.y<45:
            lives.decrement_lives()
            return True
        self.clock.tick(40)
        
    def print_point(self):
        '''function to display point image'''
        self.point_rect=pygame.Rect([self.x,self.y,30,30])
        #every image in the game is displayed on a rectangle of the same
        #size as image because of a builtin function to check collisions between
        #rectangles.
        pygame.draw.rect(self.screen,[0,0,0],self.point_rect)
        self.screen.blit(self.point_image,(self.x,self.y))

    def move(self,event):
        '''function which contains all the keyboard events to move point
        accordingly'''
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                self.x_change=-5
            if event.key==pygame.K_RIGHT:
                self.x_change=5
            if event.key==pygame.K_UP:
                self.y_change=-5
            if event.key==pygame.K_DOWN:
                self.y_change=5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT  or  event.key==pygame.K_RIGHT:
                self.x_change=0
            if event.key==pygame.K_UP  or  event.key==pygame.K_DOWN:
                self.y_change=0     





#__________CLASS message__________

class message:
    '''this is a class for displaying custom instruction in the game'''
    count=0
    i=0
    def __init__(self,sc,msg,X=120,Y=500):
        '''class constructor
        Paramters:
        sc(str): screen on which the message is displayed
        msg(str) : custom message
        X(int): x position of message
        Y(int): y position of message'''
        self.screen =sc
        self.x=X
        self.y=Y
        self.txt=msg

        message.count+=1
        if message.count<150:
            self.place_text()
            
    def place_text(self):
        '''function to place and display message '''
        font=pygame.font.SysFont('calibri',25)
        text=font.render(self.txt,1,[255,255,255],[0,0,0])
        self.screen.blit(text,(self.x,self.y))
       



#_________CLASS basket________________

class basket:
    '''This is a class for performing functionality on basket'''
    
    x_speed=2.75
    y_speed=2.75
    
    def __init__(self,sc,x1=700,y1=100):
        '''class constructor
        Parameters:
        sc(str): screen on which the basket is displayed
        x1(int): x position of basket
        y1(int): y position of basket'''
        
        basket.x_speed=4
        basket.y_speed=4
        self.screen=sc
        self.x=x1
        self.y=y1
        self.load_image()
        self.clock=pygame.time.Clock()
        
    def load_image(self):
        '''function to load image of a basket'''
        self.basket=pygame.image.load('A1_CS19105_9\\basket.png').convert()
        self.basket_image=pygame.transform.scale(self.basket,(58,58))
        
    def print_basket(self,other_rect):#for  static basket
        '''function for printing basket
        Parameters:
        other_rect: rectangle on which point image is displayed '''
        self.other_rect=other_rect
        self.basket_rect=pygame.Rect([self.x,self.y,58,58])
        pygame.draw.rect(self.screen,[0,0,0],self.basket_rect)
        self.screen.blit(self.basket_image,(self.x,self.y))
        if self.collision_with_point():
            return True
        
    def moving_basket(self,other_rect):#for movingbasket
        ''''function for making the basket move
        Parameters:
        other_rect: rectangle on which point image is displayed '''
        self.x+=basket.x_speed
        self.y+=basket.y_speed
        if self.print_basket(other_rect):
            return True
        
        if self.basket_rect.right>=1000 or self.basket_rect.left<=0:
            basket.x_speed*=-1
        if self.basket_rect.bottom>=800 or self.basket_rect.top<=36:
            basket.y_speed*=-1
           
        if abs(self.other_rect.right-self.basket_rect.left)<30:
            basket.x_speed+=0.2
        if abs(self.other_rect.left-self.basket_rect.right)<30:
            basket.x_speed-=0.2

        if abs(self.basket_rect.top-self.other_rect.bottom)<30:
            basket.y_speed+=0.2
        if abs(self.basket_rect.bottom-self.other_rect.top)<30:
            basket.y_speed-=0.2
        self.clock.tick(60)
        
    def collision_with_point(self):
        '''function  which returns True if there is a collision between basket
        and point'''
        if self.basket_rect.colliderect(self.other_rect):
            return True
        

            

#______________CLASS following_obstacle________________
            
class  following_obstacle:
    '''this is a class for performing functionality on obstacle which follows
    the point''' 
    x_speed=3
    y_speed=3
    
    def __init__(self,sc,x1=500,y1=300):
        '''class constructor
        Parameters:
        sc(str): screen on which the obstacle is displayed
        x1(int): x position of obstacle
        y1(int): y position of obstacle'''
        
        self.screen=sc
        self.x=x1
        self.y=y1
        self.load_image()
        
    def load_image(self):
        '''function to load image of obstacle'''
        self.obs=pygame.image.load('A1_CS19105_9\\obsSquare.png').convert()
        self.followobs_image=pygame.transform.scale(self.obs,(35,35))
        
    def print_obs(self):
        '''function for displaying obstacle'''
        self.obs_rect=pygame.Rect([self.x,self.y,35,35])
        pygame.draw.rect(self.screen,[0,0,0],self.obs_rect)
        self.screen.blit(self.followobs_image,(self.x,self.y))
        if self.collision_with_point():
            return True
        
    def follow_point(self,other_rect,lives):
        '''function for making the obstacle follow
        other_rect: rectangle on which point image is displayed
        lives: Lives class object'''
        self.lives=lives
        self.point_rect=other_rect
        dx,dy=self.point_rect.x-self.x,self.point_rect.y-self.y
        dist=math.hypot(dx,dy)
        dx,dy=dx/dist,dy/dist
        self.x+=dx*following_obstacle.x_speed
        self.y+=dy*following_obstacle.y_speed
        if self.print_obs():
            return True
        
    def collision_with_point(self):
        '''function  which returns True if there is a collision between obstacle
        and point'''
        if self.obs_rect.colliderect(self.point_rect):
            self.lives.decrement_lives()
            return True


    
#___________CLASS targeting_obstacle______________
            
class  targeting_obstacle:
    '''This is a class for performing functionality on the obstacle which targets
    the point'''
    
    def __init__(self,sc,x1=500,y1=700):
        '''class constructor
        Parameters:
        sc(str): screen on which the obstacle is displayed
        x1(int): x position of obstacle
        y1(int): y position of obstacle'''
        
        self.i=0
        self.x_speed=15
        self.y_speed=15
        self.obsx=0
        self.obsy=0
        self.screen=sc
        self.x=x1
        self.y=y1
        self.dx=0
        self.dy=0
        self.load_image()
        
    def load_image(self):
        '''function to load image of obstacle'''
        self.obs=pygame.image.load('A1_CS19105_9\\obsX.png').convert()
        self.targetobs_image=pygame.transform.scale(self.obs,(30,30))
        
    def print_obs(self):
        '''function to print obstacle'''
        self.obs_rect=pygame.Rect([self.x,self.y,30,30])
        pygame.draw.rect(self.screen,[0,0,0],self.obs_rect)
        self.screen.blit(self.targetobs_image,(self.x,self.y))
        if self.collision_with_point():
            return True
   
    def get_position(self):
        '''function to get position of a point'''
        if self.obsx==0 :
            self.obsx=self.point_rect.x
            self.obsy=self.point_rect.y
            dx,dy=self.obsx-self.x,self.obsy-self.y
            dist=math.hypot(dx,dy)
            try:
                self.dx,self.dy=dx/dist,dy/dist
            except ZeroDivisionError:
                self.dx,self.dy=dx/1,dy/1
                
    def againtarget_point(self):
        '''function to make the obstacle get the position and target again'''
        self.obsx=0
        self.obsy=0
        self.i=0
        self.target_point(self.point_rect,self.lives)
        
    def target_point(self,other_rect,lives):
        '''function to make the obstacle target
        Parameters:
        other_rect: rectangle on which the point image is displayed
        lives: object of class Lives'''
        self.lives=lives
        self.point_rect=other_rect
        self.get_position()
        if self.print_obs():
            return True
        if abs(self.obs_rect.x-self.obsx)<=8:
            self.i+=1
            self.x+=0
            self.y+=0
            if self.i==70:
                self.againtarget_point()
        else:
            self.x+=self.x_speed*self.dx
            self.y+=self.y_speed*self.dy
            if self.obs_rect.right>=1000 or self.obs_rect.left<=0:
                self.x+=0
                self.y+=0
                self.againtarget_point()
            if self.obs_rect.bottom>=800 or self.obs_rect.top<=36:
                self.x+=0
                self.y+=0
                self.againtarget_point()   
            
    def collision_with_point(self):
        '''function  which returns True if there is a collision between obstacle
        and point'''
        if self.obs_rect.colliderect(self.point_rect):
           self.lives.decrement_lives()
           return True





#_____________CLASS updown_obstacle____________
         
class updown_obstacle:
    '''this is a class which performs functionaly on a obstacle which moves up
    and down'''
    
    def __init__(self,sc,x1=590,y1=380,speed_y=3,steps=100):
        '''class constructor
        Parameters:
        sc(str): screen on which the obstacle is displayed
        x1(int): x position of obstacle
        y1(int): y position of obstacle
        speed_y(int or float): y speed of obstacle
        steps (int): steps the obstacle move'''
        self.count=0
        self.i=0
        self.screen=sc
        self.x=x1
        self.y=y1
        self.dx=3
        self.dy=speed_y
        self.steps=steps
        self.load_image()
        
    def load_image(self):
        '''function for loading image of obstacle'''
        self.obs=pygame.image.load('A1_CS19105_9\\obsPurple.png').convert()
        self.updownobs_image=pygame.transform.scale(self.obs,(40,40))
        
    def print_obs(self):
        '''function for printing obstacle'''
        self.obs_rect=pygame.Rect([self.x,self.y,40,40])
        pygame.draw.rect(self.screen,[0,0,0],self.obs_rect)
        self.screen.blit(self.updownobs_image,(self.x,self.y))
        collision=self.collision_with_point()
        if collision:
            return True
        
    def move_obs(self,other_rect,lives):
        '''function for making the obstacle to move
        other_rect: rectangle on which the point image is displayed
        lives: object of class Lives'''
        self.lives=lives
        self.point_rect=other_rect
        if self.y<380:
            self.y=380
        if self.y>600:
            self.y=380
       
        if self.i==self.steps:
            self.x-=0
            self.y-=self.dy
            self.count+=1
            if  self.count==self.steps:
                    self.i=0
                    self.count=0
        else:
            self.x+=0
            self.y+=self.dy
            self.i+=1
        collision=self.print_obs()
        if collision:
            return True
        
    def collision_with_point(self):
        '''function  which returns True if there is a collision between obstacle
        and point'''
        if self.obs_rect.colliderect(self.point_rect):
            self.lives.decrement_lives()
            return True







#_____________CLASS leftright_obstacle____________
 
class leftright_obstacle:
    '''this is a class which performs functionaly on a obstacle which moves left
    and right'''
    def __init__(self,sc,x1=500,y1=300,speed_x=3,steps=100):
        '''class constructor
        Parameters:
        sc(str): screen on which the obstacle is displayed
        x1(int): x position of obstacle
        y1(int): y position of obstacle
        speed_x(int or float): x speed of the obstacle
        steps(int): steps for the obstacle to move'''
        
        self.screen=sc
        self.count=0
        self.i=0
        self.x=x1
        self.y=y1
        self.dx=speed_x
        self.dy=3
        self.steps=steps
        self.load_image()
        
    def load_image(self):
        '''function for loading image of obstacle'''
        self.obs=pygame.image.load('A1_CS19105_9\\obsOrange.png').convert()
        self.leftrightobs_image=pygame.transform.scale(self.obs,(40,40))
        
    def print_obs(self):
        '''function for displaying obstacle'''
        self.obs_rect=pygame.Rect([self.x,self.y,40,40])
        pygame.draw.rect(self.screen,[0,0,0],self.obs_rect)
        self.screen.blit(self.leftrightobs_image,(self.x,self.y))
        if self.collision_with_point():
            return True
        
    def move_obs(self,other_rect,lives):
        '''function for moving obstacle
        other_rect: rectangle on which the point image is displayed
        lives: object of class Lives'''
        self.lives=lives
        self.point_rect=other_rect
        if self.i==self.steps:
            self.x-=self.dx
            self.y-=0
            self.count+=1
            if  self.count==self.steps:
                    self.i=0
                    self.count=0
        else:
            self.x+=self.dx
            self.y+=0
            self.i+=1
        if self.print_obs():
            return True
        
    def collision_with_point(self):
        '''function  which returns True if there is a collision between obstacle
        and point'''
        if self.obs_rect.colliderect(self.point_rect):
            self.lives.decrement_lives()
            return True


        
        

#_____________CLASS laser____________
 
class laser :
    i=0
    appear_count=0
    disappear_count=0
    def __init__(self,sc):
        '''class constructor
        Parameters:
        sc(str): screen on which the laser is displayed
        '''
        self.screen=sc
        self.count=0
        self.i=0
        self.x1=2
        self.x2=2
        self.counter()
        
    def random (self):
        '''function for choosing random x co-ordinate'''
        self.x1=random.randint(100,900)
        self.x2=random.randint(100,900)
        
    def counter(self):
        '''function for displaying laser after a  particular interval of time'''
        laser.appear_count+=1
        if laser.appear_count>200:
            self.random()
            pygame.draw.line(self.screen,[255,0,0],[self.x1,50],[self.x2,800],10)
            laser.disappear_count+=1
            if laser.disappear_count==5:
                laser.appear_count=0
                laser.disappear_count=0
            
    def collision(self,lives,other_rect):
        '''function  which returns True if there is a collision between laser
        and point'''
        self.point_rect=other_rect
        for x in range(self.x1,self.x2+1):
            for y in range (50,801):
                if self.point_rect.collidepoint((x,y)):
                    lives.decrement_lives()
                    return True



        

#_____________CLASS rain_obstacle____________
                 
class rain_obstacle:
    i=0
    count=0
    def __init__(self,sc,speed_y=6):
        '''class constructor
        Parameters:
        sc(str): screen on which the basket is displayed
        speed_y(int or float): y speed of the obstacle'''
        self.screen=sc
        self.y=40
        self.dy=speed_y
        
        self.load_image()
        self.random_x()
        
    def random_x(self):
        '''function for choosing random x co_ordinate'''
        self.x=random.randint(2,970)
        
    def load_image(self):
        '''function for loading image of obstacle'''
        self.obs=pygame.image.load('A1_CS19105_9\\obsTeeth.png').convert()
        self.rainobs_image=pygame.transform.scale(self.obs,(40,40))
        
    def print_obs(self):
        '''function for printing obstacle'''
        self.obs_rect=pygame.Rect([self.x,self.y,40,40])
        pygame.draw.rect(self.screen,[0,0,0],self.obs_rect)
        self.screen.blit(self.rainobs_image,(self.x,self.y))
        if self.collision_with_point():
            return True
        
    def move_obs(self,other_rect,lives):
        '''function for moving obstacle
        other_rect: rectangle on which the point image is displayed
        lives: object of class Lives'''
        self.lives=lives
        self.point_rect=other_rect
        
        self.x+=0
        self.y+=self.dy
        if self.print_obs():
            return True
        if self.y>800:
            self.y=40
            self.random_x()
            
    def collision_with_point(self):
        '''function  which returns True if there is a collision between obstacle
        and point'''
        if self.obs_rect.colliderect(self.point_rect):
            self.lives.decrement_lives()
            return True
        
        



















        


           



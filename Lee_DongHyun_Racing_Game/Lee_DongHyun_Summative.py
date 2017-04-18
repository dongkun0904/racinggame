_author_ = "Dong Hyun Lee"
_date_ = "Friday, January 22nd, 2016"
_version_ = "23.0"
_filename_ = "Lee_DongHyun_Summative.py"
_description_ = "Racing Game"

#import
import pygame, sys, time, math
from pygame.locals import *

#Classes
class RacingGame(pygame.sprite.Sprite): #class foor racing game program
    """This class is a parent class of all classes"""
    def __init__(self):
        """Creates a class RacingGame"""
        pygame.sprite.Sprite.__init__(self)

class Map(RacingGame): #creates curb or booster charger
    """This class creates map class"""
    def __init__(self,image,x,y):
        """Creates a map"""
        super(Map,self).__init__()
        self.__x = x #x coordinate
        self.__y = y #y coordinate
        self.__image = image #image of the map
        self.rect = self.__image.get_rect(center=(self.__x,self.__y)) #to detect collision

    def get_x(self): #Accessor method
        """Returns x"""
        return self.__x

    def set_x(self,x): #Mutator method
        """Changes x"""
        self.__x = x
        
    def get_y(self): #Accessor method
        """Returns y"""
        return self.__y
    
    def set_y(self,y): #Mutator method
        """Changes y"""
        self.__y = y
        
class Car(RacingGame): #creates cars
    """This class creates an information of the car"""
    def __init__(self,image,x,y,direction=0,speed=0):
        """Creates a class Car"""
        super(Car,self).__init__()
        self.__x = x #x coordinate
        self.__y = y #y coordinate
        self.__direction = direction #in degrees
        self.__image = image #color of the car
        self.__speed = speed #in m/s
        self.rect = self.__image.get_rect(center=(self.__x+26,self.__y+14)) #to detect collision

    def get_x(self): #Accessor method
        """Returns x"""
        return self.__x

    def set_x(self,x): #Mutator method
        """Changes x"""
        self.__x = x
        
    def get_y(self): #Accessor method
        """Returns y"""
        return self.__y
    
    def set_y(self,y): #Mutator method
        """Changes y"""
        self.__y = y
        
    def get_direction(self): #Accessor method
        """Returns direction"""
        return self.__direction

    def set_direction(self,direction): #Mutator method
        """Changes direction"""
        self.__direction = direction

    def get_speed(self): #Accessor method
        """Returns speed"""
        return self.__speed

    def set_speed(self,speed): #Mutator method
        """Changes speed"""
        self.__speed = speed

    def moveSpeed(self,speed): #Adding speed
        """Adds speed"""
        self.__speed += speed
        
    def rotate(self): #Rotate the image of the car
        """Rotates the car"""
        playerRot = pygame.transform.rotate(self.__image,self.__direction)
        return playerRot

    def moveX(self):
        """Move(x coordinate)"""
        movex = self.__x - math.cos(self.__direction/57.29)*self.__speed
        return movex

    def moveY(self):
        """Move(y coordinate)"""
        movey = self.__y + math.sin(self.__direction/57.29)*self.__speed
        return movey

    def minX(self): #Returnin the minimum value of x
        """Returns the min x coordinate"""
        angle = self.__direction/(180/math.pi)
        while angle > math.pi/2:
            angle -= (math.pi/2)
        while angle < 0:
            angle += (math.pi/2)
        tempX = self.__x + ((28 * math.cos(angle)) + (52 * math.sin(angle)))
        if self.__x <= tempX:
            return self.__x
        else:
            return tempX
        
    def maxX(self): #Returnin the maximum value of x
        """Returns the max x coordinate"""
        angle = self.__direction/(180/math.pi)
        while angle > math.pi/2:
            angle -= (math.pi/2)
        while angle < 0:
            angle += (math.pi/2)
        tempX = self.__x + ((28 * math.sin(angle)) + (52 * math.cos(angle)))
        if self.__x >= tempX:
            return self.__x
        else:
            return tempX

    def minY(self): #Returnin the minimum value of y
        """Returns the min y coordinate"""
        angle = self.__direction/(180/math.pi)
        while angle > math.pi/2:
            angle -= (math.pi/2)
        while angle < 0:
            angle += (math.pi/2)
        tempY = self.__y + ((28 * math.cos(angle)) + (52 * math.sin(angle)))
        if self.__y <= tempY:
            return self.__y
        else:
            return tempY

    def maxY(self): #Returnin the maximum value of y
        """Returns the max y coordinate"""
        angle = self.__direction/(180/math.pi)
        while angle > math.pi/2:
            angle -= (math.pi/2)
        while angle < 0:
            angle += (math.pi/2)
        tempY = self.__y + ((28 * math.sin(angle)) + (52 * math.cos(angle)))
        if self.__y >= tempY:
            return self.__y
        else:
            return tempY

    def changeAngle(self,direction,limit,cornering): #Making a linear relationship between speed and angle
        """Changes the direction depending on speed"""
        angle = -self.__speed*(direction)/(6-cornering)
        if angle > limit:
            angle = limit
        elif angle < -limit:
            angle = -limit
        self.__direction += angle
        if self.__direction > 360:
            self.__direction -= 360
        elif self.__direction < -360:
            self.__direction += 360

    def collision(self,other):
        """Checks the collision"""
        col = pygame.sprite.collide_rect(self,other)
        return col

    def settingRect(self):
        """Changes the location of rect"""
        self.rect = self.__image.get_rect(center=(self.__x+26,self.__y+14))

    def hazardPlace(self):
        """Decreases the speed when enters hazard"""
        if self.__speed > 0:
            self.__speed -= 0.2
        elif self.__speed < 0:
            self.__speed += 0.2

class SpeedCar(Car):
    """This class creates a speed-type car"""

    #Variables
    __ACCEL = 0.4 #in m/s
    __CORNERING = 4 #rate of angle change
    __CORNERLIMIT = 4.5 #maximum angle

    def __init__(self,image,x,y,direction=0,speed=0):
        """This method creates a speed-type car"""
        super(SpeedCar,self).__init__(image,x,y,direction,speed)

    @staticmethod #Function decorator
    def get_accel():
        """Accessor method for speed"""
        return SpeedCar.__ACCEL
        
    @staticmethod #Function decorator
    def get_corner():
        """Accessor method for cornering"""
        return SpeedCar.__CORNERING
        
    @staticmethod #Function decorator
    def get_maxCorner():
        """Accessor method for cornerLimit"""
        return SpeedCar.__CORNERLIMIT

    @staticmethod #Function decorator
    def get_speedLimit():
        """Accessor method for speedLimit"""
        return SpeedCar.__speedLimit

    def moveSpeedF(self):
        """Changes speed when keys are pressed"""
        if self.get_speed() <= 12:
            self.moveSpeed(SpeedCar.__ACCEL)
        else:
            self.set_speed(12)
            
    def moveSpeedB(self):
        """Changes speed when keys are pressed"""
        if self.get_speed() >= -12:
            self.moveSpeed(-SpeedCar.__ACCEL)
        else:
            self.set_speed(-12)

    def returnSpeedF(self):
        """Accelerates negatively"""
        if self.get_speed() > 0:
            self.moveSpeed(-SpeedCar.__ACCEL)
        if abs(self.get_speed()) <= 0.5:
            self.set_speed(0)
            
    def returnSpeedB(self):
        """Accelerates negatively"""
        if self.get_speed() < 0:
            self.moveSpeed(SpeedCar.__ACCEL)
        if abs(self.get_speed()) <= 0.5:
            self.set_speed(0)

    def cornering(self,direction): #angle of rotation depending on speed
        """Cornering with direction"""
        self.changeAngle(direction,SpeedCar.__CORNERLIMIT,SpeedCar.__CORNERING)
                
class CorneringCar(Car):
    """This class creates a cornering-type car"""

    #Constant variables
    __ACCEL = 0.3 #in m/s
    __CORNERING = 5 #rate of angle change
    __CORNERLIMIT = 5.5 #maximum angle

    def __init__(self,image,x,y,direction=0,speed=0):
        """This method creates a cornering-type car"""
        super(CorneringCar,self).__init__(image,x,y,direction,speed)

    @staticmethod #Function decorator
    def get_accel():
        """Accessor method for speed"""
        return CorneringCar.__ACCEL

    @staticmethod #Function decorator
    def get_corner():
        """Accessor method for cornering"""
        return CorneringCar.__CORNERING

    @staticmethod #Function decorator
    def get_maxCorner():
        """Accessor method for cornerLimit"""
        return CorneringCar.__CORNERLIMIT
        
    def moveSpeedF(self):
        """Changes speed when keys are pressed"""
        if self.get_speed() <= 10:
            self.moveSpeed(CorneringCar.__ACCEL)
        else:
            self.set_speed(10)
        
    def moveSpeedB(self):
        """Changes speed when keys are pressed"""
        if self.get_speed() >= -10:
            self.moveSpeed(-CorneringCar.__ACCEL)
        else:
            self.set_speed(-10)

    def returnSpeedF(self):
        """Accelerates negatively"""
        if self.get_speed() > 0:
            self.moveSpeed(-CorneringCar.__ACCEL)
        if abs(self.get_speed()) <= 0.5:
            self.set_speed(0)
            
    def returnSpeedB(self):
        """Accelerates negatively"""
        if self.get_speed() < 0:
            self.moveSpeed(CorneringCar.__ACCEL)
        if abs(self.get_speed()) <= 0.5:
            self.set_speed(0)

    def cornering(self,direction): #angle of rotation depending on speed
        """Cornering with direction"""
        self.changeAngle(direction,CorneringCar.__CORNERLIMIT,CorneringCar.__CORNERING)
                
class BalanceCar(Car):
    """This class creates a balance-type car"""

    #Constant variables
    __ACCEL = 0.35 #in m/s
    __CORNERING = 4.5 #rate of angle change
    __CORNERLIMIT = 5 #maximum angle

    def __init__(self,image,x,y,direction=0,speed=0):
        """This method creates a balance-type car"""
        super(BalanceCar,self).__init__(image,x,y,direction,speed)

    @staticmethod #Function decorator
    def get_accel():
        """Accessor method for speed"""
        return BalanceCar.__ACCEL

    @staticmethod #Function decorator
    def get_corner():
        """Accessor method for cornering"""
        return BalanceCar.__CORNERING

    @staticmethod #Function decorator
    def get_maxCorner():
        """Accessor method for cornerLimit"""
        return BalanceCar.__CORNERLIMIT
        
    def moveSpeedF(self):
        """Changes speed when keys are pressed"""
        if self.get_speed() <= 11:
            self.moveSpeed(BalanceCar.__ACCEL)
        else:
            self.set_speed(11)
        
    def moveSpeedB(self):
        """Changes speed when keys are pressed"""
        if self.get_speed() >= -11:
            self.moveSpeed(-BalanceCar.__ACCEL)
        else:
            self.set_speed(-11)

    def returnSpeedF(self):
        """Accelerates negatively"""
        if self.get_speed() > 0:
            self.moveSpeed(-BalanceCar.__ACCEL)
        if abs(self.get_speed()) <= 0.5:
            self.set_speed(0)
            
    def returnSpeedB(self):
        """Accelerates negatively"""
        if self.get_speed() < 0:
            self.moveSpeed(BalanceCar.__ACCEL)
        if abs(self.get_speed()) <= 0.5:
            self.set_speed(0)

    def cornering(self,direction): #angle of rotation depending on speed
        """Cornering with direction"""
        self.changeAngle(direction,BalanceCar.__CORNERLIMIT,BalanceCar.__CORNERING)
                
#Choice function
def choice():
    global arrow1,arrow2,screen,square,carB,carR,carY,startText,startSquare,choiceChecking,gamingChecking,uChoices,carOrder1,carOrder2,title
    global speedType,balanceType,corneringType,typeOrder1,typeOrder2

    mouseLoc = pygame.mouse.get_pos() #get the coordinate of the mouse
    
    carList1 = [carB,carR,carY] #list of the colors of the car for player 1
    carList2 = [carB,carR,carY] #list of the colors of the car for player 2
    typeList1 = [speedType,balanceType,corneringType] #list of the types of the car for player 1
    typeList2 = [speedType,balanceType,corneringType] #list of the types of the car for player 2
    showCar1 = carList1[carOrder1] #appear on the screen
    showCar2 = carList2[carOrder2] #appear on the screen
    showType1 = typeList1[typeOrder1] #appear on the screen
    showType2 = typeList2[typeOrder2] #appear on the screen
    uChoices = [[showCar1,showType1],[showCar2,showType2]] #users' choices that goes through to gaming()

    #showing on the screen    
    screen.fill((255,255,255))
    screen.blit(title,(200,50))
    screen.blit(arrow1,(56,200))
    screen.blit(arrow2,(356,200))
    screen.blit(square,(156,150)) #square to show player 1's car
    screen.blit(arrow1,(512+56,200))
    screen.blit(arrow2,(512+356,200))
    screen.blit(square,(512+156,150)) #square to show player 2's car
    screen.blit(showCar1,(191,210))
    screen.blit(showCar2,(512+191,210))
    screen.blit(startText,(400,600))
    screen.blit(startSquare,(350,600))
    screen.blit(arrow1,(56,400))
    screen.blit(arrow2,(356,400))
    screen.blit(arrow1,(512+56,400))
    screen.blit(arrow2,(512+356,400))
    screen.blit(showType1,(156,425))
    screen.blit(showType2,(156+512,425))
    pygame.display.update()
    time.sleep(0.02)

    #checking keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #starting the game
        if event.type == pygame.MOUSEBUTTONUP:
            #Checking if the user is ready to play
            if mouseLoc[0] >= 350 and mouseLoc[0] <= 700:
                if mouseLoc[1] >= 600 and mouseLoc[1] <= 700:
                    choiceChecking = False
                    gamingChecking = True

            #users' color choices
            if mouseLoc[0] >= 56 and mouseLoc[0] <= 156:
                if mouseLoc[1] >= 200 and mouseLoc[1] <= 300:
                    carOrder1 -= 1
                    if carOrder1 <= -3:
                        carOrder1 += 3
                elif mouseLoc[1] >= 400 and mouseLoc[1] <= 500:
                    typeOrder1 -= 1
                    if typeOrder1 <= -3:
                        typeOrder1 += 3
                        
            if mouseLoc[0] >= 356 and mouseLoc[0] <= 456:
                if mouseLoc[1] >= 200 and mouseLoc[1] <= 300:
                    carOrder1 += 1
                    if carOrder1 >= 3:
                        carOrder1 -= 3
                elif mouseLoc[1] >= 400 and mouseLoc[1] <= 500:
                    typeOrder1 += 1
                    if typeOrder1 >= 3:
                        typeOrder1 -= 3

            #users' type choices
            if mouseLoc[0] >= 56+512 and mouseLoc[0] <= 156+512:
                if mouseLoc[1] >= 200 and mouseLoc[1] <= 300:
                    carOrder2 -= 1
                    if carOrder2 <= -3:
                        carOrder2 += 3
                elif mouseLoc[1] >= 400 and mouseLoc[1] <= 500:
                    typeOrder2 -= 1
                    if typeOrder2 <= -3:
                        typeOrder2 += 3

            if mouseLoc[0] >= 356+512 and mouseLoc[0] <= 456+512:
                if mouseLoc[1] >= 200 and mouseLoc[1] <= 300:
                    carOrder2 += 1
                    if carOrder2 >= 3:
                        carOrder2 -= 3
                elif mouseLoc[1] >= 400 and mouseLoc[1] <= 500:
                    typeOrder2 += 1
                    if typeOrder2 >= 3:
                        typeOrder2 -= 3

#Gaming function
def gaming():
    global keys1,keys2,keysChecking1,keysChecking2,player1,player2,collisionCheck1,collisionCheck2,screen,startTime,middleMap,lap1,lap2
    global middleMap,xpos1,xpos2y,pos1,ypos2,trackx,tracky,track,uChoices,gamingChecking,rankingChecking,collisionCheckBoth,checkingLap1,checkingLap2
    global count3,count2,count1,goText,timing,timeChecking,timeText,myFont2,timeMin,timeRecord,recordChecking,instruction,itemBox
    global booster1,booster2,boosterTimeCheck1,boosterTimeCheck2,haveBooster1,haveBooster2,itemBoxImg,itemSlot,boosterTime1,boosterTime2,uRecord

    gameDone = False

    #update the laps everytime
    lapText1 = myFont2.render("Lap: %d" %(lap1),1,(BLACK))
    lapText2 = myFont2.render("Lap: %d" %(lap2),1,(BLACK))

    #Checking keys
    #Rotating
    if keys1[0] == True and keysChecking1 == True:
        player1.cornering(-1)
    if keys1[1] == True and keysChecking1 == True:
        player1.cornering(1)
                
    #Checking speed
    if keys1[2] == True and keysChecking1 == True:
        if not booster1:
            player1.moveSpeedF()
    else:
        if player1.get_speed() >= 0:
            player1.returnSpeedF()
    if keys1[3] == True and keysChecking1 == True:
        player1.moveSpeedB()
    else:
        if player1.get_speed() <= 0:
            player1.returnSpeedB()

    #Rotating depending on speed
    if keys2[0] == True and keysChecking2 == True:
        player2.cornering(1)
    if keys2[1] == True and keysChecking2 == True:
        player2.cornering(-1)

    #Checking speed
    if keys2[2] == True and keysChecking2 == True:
        if not booster2:
            player2.moveSpeedB()
    else:
        if player2.get_speed() <= 0:
            player2.returnSpeedB()
    if keys2[3] == True and keysChecking2 == True:
            player2.moveSpeedF()
    else:
        if player2.get_speed() >= 0:
            player2.returnSpeedF()

    #Move
    player1.set_x(player1.moveX())
    player1.set_y(player1.moveY())
    player1.settingRect()
    player2.set_x(player2.moveX())
    player2.set_y(player2.moveY())
    player2.settingRect()

    #Collision check - curb
    if collisionCheck1: #collision check between player 1 and a curb
        if player1.collision(middleMap):
            player1.set_speed(player1.get_speed()*-1) #Going backward
            collisionCheck1 = True
            startTime = time.time()

            #resetting the coordinate of the car when it collides            
            if player1.maxX() > 512-264 and player1.maxX() < 512+264:
                player1.set_x(player1.get_x()-1)
            elif player1.minX() < 512+264 and player1.minX() > 512-264:
                player1.set_x(player1.get_x()+1)
            if player1.maxY() > 372-142 and player1.maxY() < 372+142:
                player1.set_y(player1.get_y()-1)
            elif player1.minY() < 372+142 and player1.minY() > 372-142:
                player1.set_y(player1.get_y()+2)
            keys1 = [False,False,False,False]
            booster1 = False
            boosterTimeCheck1 = True

    if collisionCheck2: #collision check between player 2 and a curb
        if player2.collision(middleMap):
            player2.set_speed(player2.get_speed()*-1) #Going backward
            collisionCheck2 = True
            startTime = time.time()

            #resetting the coordinate of the car when it collides  
            if player2.maxX() > 512-264 and player2.maxX() < 512+264:
                player2.set_x(player2.get_x()-1)
            elif player2.minX() < 512+264 and player2.minX() > 512-264:
                player2.set_x(player2.get_x()+1)
            if player2.maxY() > 372-142 and player2.maxY() < 372+142:
                player2.set_y(player2.get_y()-1)
            elif player2.minY() < 372+142 and player2.minY() > 372-142:
                player2.set_y(player2.get_y()+2)
            keys2 = [False,False,False,False]
            booster2 = False
            boosterTimeCheck2 = True

    #Collision check - cars
    if collisionCheckBoth: #collision check between player 1 and player 2
        checkingCol = player1.collision(player2)
        if checkingCol:
            player1.set_speed(player1.get_speed()*-1) #Going backward
            player2.set_speed(player2.get_speed()*-1) #Going backward
            collisionCheckBoth = False
            startTime = time.time()

            #resetting the coordinate of the cars when they collide            
            if player1.get_x() > player2.get_x():
                player1.set_x(player1.get_x()+1)
                player2.set_x(player2.get_x()-1)
            elif player1.get_x() < player2.get_x():
                player1.set_x(player1.get_x()-1)
                player2.set_x(player2.get_x()+1)
            if player1.get_y() > player2.get_y():
                player1.set_y(player1.get_y()+1)
                player2.set_y(player2.get_y()-1)
            elif player1.get_y() < player2.get_y():
                player1.set_y(player1.get_y()-1)
                player2.set_y(player2.get_y()+1)

            keys1 = [False,False,False,False]
            keys2 = [False,False,False,False]
            booster1 = False
            boosterTimeCheck1 = True
            booster2 = False
            boosterTimeCheck2 = True

    ##Collision check - booster
    collisionBoost1 = player1.collision(itemBox)
    collisionBoost2 = player2.collision(itemBox)
    
    if collisionBoost1:
        haveBooster1 = True
    if collisionBoost2:
        haveBooster2 = True

    #Collision check - sides of the map
    if player1.minX() < 0 or player1.maxX() > 1024:
        player1.set_speed(player1.get_speed()*-1) #Going backward
        collisionCheck1 = False
        startTime = time.time()
        keys1 = [False,False,False,False]
    elif player1.minY() < 0 or player1.maxY() > 770:
        player1.set_speed(player1.get_speed()*-1) #Going backward
        collisionCheck1 = False
        startTime = time.time()
        keys1 = [False,False,False,False]
    if player2.minX() < 0 or player2.maxX() > 1024:
        player2.set_speed(player2.get_speed()*-1) #Going backward
        collisionCheck2 = False
        startTime = time.time()
        keys2 = [False,False,False,False]
    elif player2.minY() < 0 or player2.maxY() > 770:
        player2.set_speed(player2.get_speed()*-1) #Going backward
        collisionCheck2 = False
        startTime = time.time()
        keys2 = [False,False,False,False]

    #restriction to go outside of the map
    if player1.minX() < 0:
        player1.set_x(0)
    elif player1.maxX() > 1024:
        player1.set_x(1024+(player1.get_x()-player1.maxX()))
    if player1.minY() < 0:
        player1.set_y(0)
    elif player1.maxY() > 770:
        player1.set_y(770+(player1.get_y()-player1.maxY()))
        
    if player2.minX() < 0:
        player2.set_x(0)
    elif player2.maxX() > 1024:
        player2.set_x(1024+(player2.get_x()-player2.maxX()))
    if player2.minY() < 0:
        player2.set_y(0)
    elif player2.maxY() > 770:
        player2.set_y(770+(player2.get_y()-player2.maxY()))

    #Hazard
    #0-90, 944-1024, 0-90, 690-770
    if player1.minX() < 90:
        hazard1 = True
    elif player1.maxX() > 944:
        hazard1 = True
    elif player1.minY() < 90:
        hazard1 = True
    elif player1.maxY() > 690:
        hazard1 = True
    else:
        hazard1 = False

    if player2.minX() < 90:
        hazard2 = True
    elif player2.maxX() > 944:
        hazard2 = True
    elif player2.minY() < 90:
        hazard2 = True
    elif player2.maxY() > 690:
        hazard2 = True
    else:
        hazard2 = False
    
    if hazard1:
        player1.hazardPlace()
        #Limit max speed
        if abs(player1.get_speed()) > 2:
            player1.set_speed(2*(abs(player1.get_speed())/player1.get_speed()))

    if hazard2:
        player2.hazardPlace()
        #Limit max speeds
        if abs(player2.get_speed()) > 2:
            player2.set_speed(2*(abs(player2.get_speed())/player2.get_speed()))
        
    #Setting not to detect collision for 0.1 second
    if not collisionCheckBoth or not collisionCheck1:
        if time.time() - startTime >= 0.1:
            collisionCheck1 = True
            collisionCheckBoth = True

    if not collisionCheckBoth or not collisionCheck2:
        if time.time() - startTime >= 0.1:
            collisionCheck2 = True
            collisionCheckBoth = True

    #Checking laps
    #when a car goes through a certain place, checkingLap becomes True
    if player1.minX() >= 1024-250 and player1.minY() <= 355:
        checkingLap1 = True

    if player2.maxX() <= 250 and player1.minY() <= 355:
        checkingLap2 = True

    if checkingLap1:
        if player1.maxY() <= 250 and player1.minX() <= 512:
            lap1 += 1
            checkingLap1 = False
    elif not checkingLap1:
        if player1.maxY() <= 250 and player1.minX() >= 512:
            lap1 -= 1
            checkingLap1 = True

    if checkingLap2:
        if player2.maxY() <= 250 and player2.maxX() >= 512:
            lap2 += 1
            checkingLap2 = False
    elif not checkingLap2:
        if player2.maxY() <= 250 and player2.maxX() <= 512:
            lap2 -= 1
            checkingLap2 = True

    #Checking booster            
    if booster1:
        player1.set_speed(20)       
        if boosterTimeCheck1:
            boosterTime1 = time.time()
            boosterTimeCheck1 = False
        else:
            #checking time - 1 second
            if time.time() - boosterTime1 >= 1:
                booster1 = False
                boosterTimeCheck1 = True

    if booster2:
        player2.set_speed(-20)
        if boosterTimeCheck2:
            boosterTime2 = time.time()
            boosterTimeCheck2 = False
        else:
            #checking time - 1 second
            if time.time() - boosterTime2 >= 1:
                booster2 = False
                boosterTimeCheck2 = True

    #showing on the screen   
    screen.fill((255,255,255))
    screen.blit(track,(trackx,tracky))
    screen.blit(player1.rotate(),(player1.get_x(),player1.get_y()))
    screen.blit(player2.rotate(),(player2.get_x(),player2.get_y()))
    screen.blit(lapText1,(50,790))
    screen.blit(lapText2,(50+712,790))
    screen.blit(itemSlot,(350,790))
    screen.blit(itemSlot,(550,790))
    screen.blit(itemBoxImg,(512-20,550))
    
    if haveBooster1 == True:
        screen.blit(itemBoxImg,(353,793))
    if haveBooster2 == True:
        screen.blit(itemBoxImg,(553,793))
    if time.time()-timing > 0 and time.time()-timing < 0.8:
        screen.blit(count3,(512-40,320))
    if time.time()-timing > 1 and time.time()-timing < 1.8:
        screen.blit(count2,(512-40,320))
    if time.time()-timing > 2 and time.time()-timing < 2.8:
        screen.blit(count1,(512-40,320))
    if time.time()-timing > 3 and time.time()-timing < 3.8:
        screen.blit(goText,(512-80,320))
        keysChecking1 = True
        keysChecking2 = True
        timeChecking = True
    if timeChecking:
        uRecord = time.time()-timing-3
        timeMili = (uRecord-(uRecord//1))*100 #in milisecond
        timeSec = uRecord - (timeMili/100) #in second
        timeMin = 0
        while timeSec >= 60:
            timeSec -= 60
            timeMin =+ 1
        uTime = "%d:%.2d:%.2d" %(timeMin,timeSec,timeMili)
        timeText = myFont2.render(uTime,1,(0,0,0))
    
    if lap1 < 3 and lap2 < 3:
        screen.blit(timeText,(512-80,790))
    else:
        if recordChecking:
            if lap1 == 3:
                record = "Player1: "+uTime
            elif lap2 == 3:
                record = "Player2: "+uTime
            recordChecking = False
            timeRecord = myFont2.render(record,1,(255,255,255))
        keysChecking1 = False
        keysChecking2 = False
        timeChecking = False
        screen.blit(timeRecord,(512-110,350))
        screen.blit(instruction,(512-250,450))
        gameDone = True

    pygame.display.update()

    #checking keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                keys1[0] = True
            elif event.key == K_d:
                keys1[1] = True
            elif event.key == K_w:
                keys1[2] = True
            elif event.key == K_s:
                keys1[3] = True
            elif event.key == K_LSHIFT:
                if haveBooster1 and not booster1:
                    booster1 = True
                    boosterTimeCheck1 = True
                    haveBooster1 = False
                
            if event.key == K_LEFT:
                keys2[0] = True
            elif event.key == K_RIGHT:
                keys2[1] = True
            elif event.key == K_UP:
                keys2[2] = True
            elif event.key == K_DOWN:
                keys2[3] = True
            elif event.key == K_RSHIFT:
                if haveBooster2 and not booster2:
                    booster2 = True
                    boosterTimeCheck2 = True
                    haveBooster2 = False

        if event.type == pygame.KEYUP:
            if event.key == K_a:
                keys1[0] = False
            elif event.key == K_d:
                keys1[1] = False
            elif event.key == K_w:
                keys1[2] = False
                if booster1:
                    booster1 = False
                    boosterTimeCheck1 = True
            elif event.key == K_s:
                keys1[3] = False

            if event.key == K_LEFT:
                keys2[0] = False
            elif event.key == K_RIGHT:
                keys2[1] = False
            elif event.key == K_UP:
                keys2[2] = False
                if booster2:
                    booster2 = False
                    boosterTimeCheck2 = True
            elif event.key == K_DOWN:
                keys2[3] = False

        if gameDone:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                gamingChecking = False
                rankingChecking = True

def ranking():
    global rankingListText,rankingChecking,choiceChecking,uRecord,num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,rankingText,restartButton

    mouseLoc = pygame.mouse.get_pos() #get the coordinate of the mouse

    #showing on the screen
    screen.fill((255,255,255))
    screen.blit(rankingText,(350,20))
    screen.blit(num1,(50,120))
    screen.blit(num2,(50,170))
    screen.blit(num3,(50,220))
    screen.blit(num4,(50,270))
    screen.blit(num5,(50,320))
    screen.blit(num6,(50,370))
    screen.blit(num7,(50,420))
    screen.blit(num8,(50,470))
    screen.blit(num9,(50,520))
    screen.blit(num10,(50,570))

    #ranking
    for i in range(len(rankingListText)):
        screen.blit(rankingListText[i],(100,120+(i*50)))
        
    screen.blit(restartButton,(350,670))
    pygame.display.update()

    #checking keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #checking the button
        if event.type == pygame.MOUSEBUTTONUP:
            if mouseLoc[0] >= 350 and mouseLoc[0] <= 350+363:
                if mouseLoc[1] >= 670 and mouseLoc[1] <= 670+112:
                    rankingChecking = False
                    choiceChecking = True

def selectionSort(myList):
    """Arranges the values in order."""
    for top in range(len(myList)-1,0,-1):
        #locate largest item and then swap it with item at list[top]
        largeLoc = 0 #location of largest element assume myList[0] to start
        for i in range(1,top+1): #check myList[1] to myList[top]
            if float(myList[i][1]) > float(myList[largeLoc][1]):
                largeLoc = i
        temp = myList[top] #temporary storage
        myList[top] = myList[largeLoc]
        myList[largeLoc] = temp
    return myList
       
#Colors
BLACK = (0,0,0)
GRAY = (100,100,100)
NAVYBLUE = (60,60,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
PURPLE = (255,0,255)
CYAN = (0,255,255)

#Variables
pygame.init()
carB = pygame.image.load("car1.png") #blue car
carB = pygame.transform.scale(carB,(130,70)) 
carR = pygame.image.load("car2.png") #red car
carR = pygame.transform.scale(carR,(130,70)) 
carY = pygame.image.load("car3.png") #yellow car
carY = pygame.transform.scale(carY,(130,70)) 
track = pygame.image.load("track.png")
arrow1 = pygame.image.load("arrow.png") #left arrow
arrow2 = pygame.image.load("arrow.png") #right arrow
arrow1 = pygame.transform.scale(arrow1,(100,100))
arrow2 = pygame.transform.scale(arrow2,(100,100))
arrow1 = pygame.transform.flip(arrow2,True,False)
itemBoxImg = pygame.image.load("itemBox.jpg") #item box
itemBoxImg = pygame.transform.scale(itemBoxImg,(40,40))
square = pygame.image.load("square.png") #square to cover the car in choice section
square = pygame.transform.scale(square,(200,200))
itemSlot = pygame.transform.scale(square,(45,45))
restartButton = pygame.image.load("restart.png") #restart button
screen = pygame.display.set_mode((1024,870))
middleMap = pygame.image.load("middle.png") #curb in the middle
middleMap = pygame.transform.scale(middleMap,(500,250))
myFont1 = pygame.font.SysFont("monospace",80) #title font
myFont2 = pygame.font.SysFont("monospace",26) #detail font
myFont3 = pygame.font.SysFont("monoscpae",50) #ranking font
startText = myFont1.render("Start",1,(BLACK))
startSquare = pygame.image.load("square.png") #button
startSquare = pygame.transform.scale(startSquare,(350,100))
speedType = myFont2.render("Speed Type",1,(BLACK))
balanceType = myFont2.render("Balance Type",1,(BLACK))
corneringType = myFont2.render("Corner Type",1,(BLACK))
title = myFont1.render("Racing Game!!",1,(BLACK))
count3 = myFont1.render("3",1,(WHITE))
count2 = myFont1.render("2",1,(WHITE))
count1 = myFont1.render("1",1,(WHITE))
goText = myFont1.render("Go!!",1,(WHITE))
timeText = myFont2.render("0:00:00",1,(BLACK))
instruction = myFont2.render("Prees any keys to see results.",1,(WHITE))
carOrder1 = 0 #player1's color choice
carOrder2 = 0 #player2's color choice
typeOrder1 = 0 #player1's type choice
typeOrder2 = 0 #player2's type choice
lap1 = 0 #number of laps for p1
lap2 = 0 #number of laps for p2
timeMin = 0 #minute of time
rankingText = myFont1.render("Ranking",1,(BLACK))

#numbers for ranking page
num1 = myFont3.render("1. ",1,(BLACK))
num2 = myFont3.render("2. ",1,(BLACK))
num3 = myFont3.render("3. ",1,(BLACK))
num4 = myFont3.render("4. ",1,(BLACK))
num5 = myFont3.render("5. ",1,(BLACK))
num6 = myFont3.render("6. ",1,(BLACK))
num7 = myFont3.render("7. ",1,(BLACK))
num8 = myFont3.render("8. ",1,(BLACK))
num9 = myFont3.render("9. ",1,(BLACK))
num10 = myFont3.render("10. ",1,(BLACK))

trackx = 0
tracky = 0
xPos1 = 452
yPos1 = 136
xPos2 = 519
yPos2 = 136
keys1 = [False,False,False,False]
keys2 = [False,False,False,False]

middleMap = Map(middleMap,512,372)
itemBox = Map(itemBoxImg,512,550+20)

keysChecking1 = False
keysChecking2 = False
collisionCheck1 = True
collisionCheck2 = True
collisionCheckBoth = True
checkingLap1 = False
checkingLap2 = False
timeChecking = False
recordChecking = True
booster1 = False
booster2 = False
boosterTimeCheck1 = False
boosterTimeCheck2 = False
haveBooster1 = False
haveBooster2 = False
rankingList = []
nameAndTimeList = []
rankingListText = []

choiceChecking = True
gamingChecking = False
rankingChecking = False
pygame.display.set_caption("Racing Game")
screen.fill(WHITE)

while True:
    if choiceChecking:
        choice()
        car1 = uChoices[0][0]
        car2 = uChoices[1][0]
        car1 = pygame.transform.scale(car1,(52,28))
        car1 = pygame.transform.flip(car1,True,False)
        car2 = pygame.transform.scale(car2,(52,28))
        timing = time.time()
        
        if uChoices[0][1] == speedType:
            player1 = SpeedCar(car1,xPos1,yPos1)
        elif uChoices[0][1] == balanceType:
            player1 = BalanceCar(car1,xPos1,yPos1)
        elif uChoices[0][1] == corneringType:
            player1 = CorneringCar(car1,xPos1,yPos1)

        if uChoices[1][1] == speedType:
            player2 = SpeedCar(car2,xPos2,yPos2)
        elif uChoices[1][1] == balanceType:
            player2 = BalanceCar(car2,xPos2,yPos2)
        elif uChoices[1][1] == corneringType:
            player2 = CorneringCar(car2,xPos2,yPos2)

    elif gamingChecking:
        gaming()
        if not gamingChecking:
            name = raw_input("What is the winner's name?: ")
            name.strip()
            try:
                inpFile = open("ranking.txt", "r")
                
            except:
                nameAndTimeList.append(name)
                nameAndTimeList.append(uRecord)
                rankingList.append(nameAndTimeList)
                
            else:
                for line in inpFile:
                    val = line.split()
                    rankingList.append(val)
                nameAndTimeList.append(name)
                nameAndTimeList.append(uRecord)
                rankingList.append(nameAndTimeList)
                rankingList = selectionSort(rankingList)
                inpFile.close()
                if len(rankingList) > 10:
                    rankingList.pop()
            try:
                outFile = open("ranking.txt", "w")

            except IOError,e:
                print "Failed to open %s for reading %s" %("ranking.txt",e)

            else:
                for i in range(len(rankingList)):
                    outFile.write(str(rankingList[i][0]))
                    outFile.write(" ")
                    outFile.write(str(rankingList[i][1]))
                    if i < len(rankingList):
                        outFile.write("\n")
                    
                    timeMili = (float(rankingList[i][1])-(float(rankingList[i][1])//1))*100 #in milisecond
                    timeSec = float(rankingList[i][1]) - (timeMili/100) #in second
                    timeMin = 0
                    while timeSec >= 60:
                        timeSec -= 60
                        timeMin =+ 1
                    uTime = "%s (%d:%.2d:%.2d)" %(rankingList[i][0],timeMin,timeSec,timeMili)
                    uTimeText = myFont3.render(uTime,1,(BLACK))
                    rankingListText.append(uTimeText)
                    
                outFile.close()
  
    elif rankingChecking:
        ranking()

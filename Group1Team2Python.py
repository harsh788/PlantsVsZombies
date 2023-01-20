import pygame
import random

# Initialising pygame
pygame.init()
width = 900
height = 600
screen = pygame. display.set_mode((width, height))

# Clock
clock = pygame.time.Clock()
spawnStatTime = pygame.time.get_ticks()     # for spawning zombies
bulStatTime = pygame.time.get_ticks()       # for moving the bullet
hitStatTime = pygame.time.get_ticks()       # for damaging a plant
shootStatTime = pygame.time.get_ticks()     # for shooting
zomStatTime = pygame.time.get_ticks()       # for moving the zombies
sunStatTime = pygame.time.get_ticks()       # for sun
sunflowerStatTime = pygame.time.get_ticks() # for spawning sun by sunflower
errorStatTime = -750                        # for diplaying error, -750 as it shouldn't be displayed in starting


# Important Variables
position = 0        # to select which plant is placed
game_over = False   # to detect if user lost the game
sun = 50            # initial sun
level = 1           # level
zombieCounter = 0   # number of zombies spawned
occupiedList = [[0 for i in range(1,10)] for i in range(5)]     # to prevent user to place one plant on the other
err = False         # to displat error

# Title and Icon
pygame.display.set_caption("PlantsVsZombiesFromIIITB")
icon = pygame.image.load('ZombieIcon.png')
pygame.display.set_icon(icon)

# Super Class
class Entity:

    def __init__(self, x, y, row):
        self.xCoor = x
        self.yCoor = y
        self.row = row
    
    # display the entity
    def Disp(self):
        screen.blit(self.Img, (self.xCoor, self.yCoor))
    
    # move the entity
    def Move(self):
        self.xCoor += self.moveAmt
    
    # damage the entity
    def Damage(self):
        self.health -= 1
    
    # add element to the list
    @classmethod
    def addEl(cls, el):
        cls.List.append(el)

# Zombie Class
class Zombie(Entity):
    Img = pygame.image.load('ClassicZombieEdit.png')
    Img = pygame.transform.scale(Img, (50, 81))

    healthBar5 = pygame.image.load('healthBar5.png')
    healthBar5 = pygame.transform.scale(healthBar5,(50,10))

    healthBar4 = pygame.image.load('healthBar4.png')
    healthBar4 = pygame.transform.scale(healthBar4,(50,10))

    healthBar3 = pygame.image.load('healthBar3.png')
    healthBar3 = pygame.transform.scale(healthBar3,(50,10))

    healthBar2 = pygame.image.load('healthBar2.png')
    healthBar2 = pygame.transform.scale(healthBar2,(50,10))

    healthBar1 = pygame.image.load('healthBar1.png')
    healthBar1 = pygame.transform.scale(healthBar1,(50,10))

    healthBarList = [healthBar1, healthBar2, healthBar3, healthBar4, healthBar5]

    List = []

    def __init__(self, x, y, row):
        super().__init__(x, y, row)
        self.health = 5
        self.moveAmt = -1
        self.Moving = True
        Zombie.addEl(self)
    
    def Disp(self):
        super().Disp()
        screen.blit(self.healthBarList[self.health-1],(self.xCoor,self.yCoor-10))

# Bullet Class
class Bullet(Entity):
    Img = pygame.image.load('Pea.png')
    Img = pygame.transform.scale(Img,(20,20))

    List = []

    def __init__(self, x, y, row):
        super().__init__(x, y, row)
        self.moveAmt = 3
        Bullet.addEl(self)

# Shooter Class
class Shooter(Entity):
    Img = pygame.image.load('PeashooterEdit.png')
    Img = pygame.transform.scale(Img, (57, 57))

    List = []

    def __init__(self, x, y, row):
        super().__init__(x, y, row)
        self.health = 2
        Shooter.addEl(self)

# Barrier Class
class Barrier(Entity):
    Img = pygame.image.load('WallnutEdit.png')
    Img = pygame.transform.scale(Img,(57,57))

    List = []

    def __init__(self, x, y, row):
        super().__init__(x, y, row)
        self.health = 10
        Barrier.addEl(self)

# Sunflower Class
class Sunflower(Entity):

    Img = pygame.image.load('SunflowerEdit.png')
    Img = pygame.transform.scale(Img, (57, 57))

    List = []

    def __init__(self,x,y,row):
        super().__init__(x, y, row)
        self.health = 2
        self.active = False
        Sunflower.addEl(self)
    
    def SpawnSun(self, currency, stattime, curtime):
        if curtime - stattime > 5000:
            return currency + 25, True
        else:
            return currency, False

# plant positioning
def plants(x, y):
    # row 1
    if y in range(0, 120):
        y = 28
        if x in range(90, 180):
            x = 90 + 13
        elif x in range(180, 270):
            x = 180 + 13
        elif x in range(270, 360):
            x = 270 + 13
        elif x in range(360, 450):
            x = 360 + 13
        elif x in range(450, 540):
            x = 450 + 13
        elif x in range(540, 630):
            x = 540 + 13
        elif x in range(630, 720):
            x = 630 + 13
        elif x in range(720, 810):
            x = 720 + 13

    # row 2
    elif y in range(120, 240):
        y = 148
        if x in range(90, 180):
            x = 90 + 13
        elif x in range(180, 270):
            x = 180 + 13
        elif x in range(270, 360):
            x = 270 + 13
        elif x in range(360, 450):
            x = 360 + 13
        elif x in range(450, 540):
            x = 450 + 13
        elif x in range(540, 630):
            x = 540 + 13
        elif x in range(630, 720):
            x = 630 + 13
        elif x in range(720, 810):
            x = 720 + 13

    # row 3
    elif y in range(240, 360):
        y = 268
        if x in range(90, 180):
            x = 90 + 13
        elif x in range(180, 270):
            x = 180 + 13
        elif x in range(270, 360):
            x = 270 + 13
        elif x in range(360, 450):
            x = 360 + 13
        elif x in range(450, 540):
            x = 450 + 13
        elif x in range(540, 630):
            x = 540 + 13
        elif x in range(630, 720):
            x = 630 + 13
        elif x in range(720, 810):
            x = 720 + 13

    # row 4
    if y in range(360, 480):
        y = 388
        if x in range(90, 180):
            x = 90 + 13
        elif x in range(180, 270):
            x = 180 + 13
        elif x in range(270, 360):
            x = 270 + 13
        elif x in range(360, 450):
            x = 360 + 13
        elif x in range(450, 540):
            x = 450 + 13
        elif x in range(540, 630):
            x = 540 + 13
        elif x in range(630, 720):
            x = 630 + 13
        elif x in range(720, 810):
            x = 720 + 13

    # row 5
    if y in range(480, 600):
        y = 508
        if x in range(90, 180):
            x = 90 + 13
        elif x in range(180, 270):
            x = 180 + 13
        elif x in range(270, 360):
            x = 270 + 13
        elif x in range(360, 450):
            x = 360 + 13
        elif x in range(450, 540):
            x = 450 + 13
        elif x in range(540, 630):
            x = 540 + 13
        elif x in range(630, 720):
            x = 630 + 13
        elif x in range(720, 810):
            x = 720 + 13


    # returning x, y and row
    return x, y, x//90, y//120

# display bgcolor, default plants on the left
def permanent_display(game_over):
    if game_over == False:
        bg = pygame.image.load('LawnEdit.jpeg')
        bg = pygame.transform.scale(bg,(720, 600))
        bgSidewalk = pygame.image.load('LawnSidewalk.jpeg')
        bgSidewalk = pygame.transform.scale(bgSidewalk,(90, 600))
        screen.blit(bgSidewalk, (810, 0))
        screen.blit(bgSidewalk, (0, 0))
        screen.blit(bg, (90, 0))
        screen.blit(Shooter.Img, (13, 28))
        screen.blit(Sunflower.Img, (13, 148))
        screen.blit(Barrier.Img, (13, 268))
    else:
        gameOverIMG = pygame.image.load('GameOver.jpg')
        gameOverIMG = pygame.transform.scale(gameOverIMG,(900, 600))

        # deleting all instances
        delInst()
        screen.blit(gameOverIMG,(0,0))

# deletes all instances of all classes
def delInst():
        for shooter in Shooter.List:
            del shooter
        Shooter.List = []
        for barrier in Barrier.List:
            del barrier
        Barrier.List = []
        for sunflower in Sunflower.List:
            del sunflower
        Sunflower.List = []
        for bullet in Bullet.List:
            del bullet
        Bullet.List = []
        for zombie in Zombie.List:
            del zombie
        Zombie.List = []

# moves all zombies once they accumulate near a plant
def move_zombie(zombie):
    for zombie2 in Zombie.List:
        if zombie2.row == zombie.row and zombie2.xCoor - zombie.xCoor in range(-40,40):
            zombie2.Moving = True
    zombie.Moving = True

# when a zombie comes near a plant
def interact(entityLst):
    for zombie in Zombie.List:
        for ent in entityLst:
            if zombie.row == ent.row:
                if ent.xCoor > zombie.xCoor:
                    pass
                elif ent.xCoor + 57 >= zombie.xCoor:
                    zombie.Moving = False
                    if curTime - hitStatTime > 1000:
                        ent.Damage()

                    if ent.health == 0:
                        move_zombie(zombie)
                        entityLst.remove(ent)
                        del ent

# displays all instances of a list
def display_entities(EntList):
    for ent in EntList:
        ent.Disp()

# display error
def disErr():
    font = pygame.font.Font('freesansbold.ttf', 16)
    insuffMoney = font.render('Insufficient Sun', True, (0, 0, 0))
    screen.blit(insuffMoney, (425, 300))

def disText(font):
    TextX = 5
    CurrY = 520
    curr = font.render('Sun: ' + str(sun), True, (0, 0, 0))
    zombiesSpawned1 = font.render('Zombies', True, (0, 0, 0))
    zombiesSpawned2 = font.render('Spawned: ' + str(zombieCounter) + '/' + str(10*level), True, (0, 0, 0))
    levelDis = font.render('Level: ' + str(level) + '/2', True, (0, 0, 0))
    ShooterCost1 = font.render('Peashooter', True, (0, 0, 0))
    ShooterCost2 = font.render('Cost: 100 Sun', True, (0, 0, 0))

    SunflowerCost1 = font.render('Sunflower', True, (0, 0, 0))
    SunflowerCost2 = font.render('Cost: 50 Sun', True, (0, 0, 0))

    BarrierCost1 = font.render('Wall Nut', True, (0, 0, 0))
    BarrierCost2 = font.render('Cost: 50 Sun', True, (0, 0, 0))

    screen.blit(ShooterCost1, (TextX + 5, 90))
    screen.blit(ShooterCost2, (TextX, 100))

    screen.blit(SunflowerCost1, (TextX + 10, 120 + 90))
    screen.blit(SunflowerCost2, (TextX, 120 + 100))

    screen.blit(BarrierCost1, (TextX + 15, 240 + 90))
    screen.blit(BarrierCost2, (TextX, 240 + 100))

    screen.blit(curr, (TextX, CurrY))
    screen.blit(zombiesSpawned1, (TextX, CurrY + 20))
    screen.blit(zombiesSpawned2, (TextX, CurrY + 30))
    screen.blit(levelDis, (TextX, CurrY + 50))

    screen.blit(Shooter.Img, (13, 28))
    screen.blit(Sunflower.Img, (13, 148))
    screen.blit(Barrier.Img, (13, 268))

running = True

# game loop
while running:

    permanent_display(game_over)

    curTime = pygame.time.get_ticks()

    # Natural sun spawning
    if curTime - sunStatTime > 7500:
        sunStatTime = curTime
        sun += 50

    # Sunflower spawns sun
    spawnSunFlag = False
    for sunflower in Sunflower.List:
        sun, spawnSunFlag = sunflower.SpawnSun(sun, sunflowerStatTime, curTime)
    if spawnSunFlag:
        sunflowerStatTime = curTime
    font = pygame.font.Font('freesansbold.ttf', 12)
    
    # displaying currency and other info
    if game_over == False:
        disText(font)
    
    # Highlight
    hoverX, hoverY = pygame.mouse.get_pos()
    if hoverX <= 90 and game_over == False:
        if hoverY >= 0 and hoverY <= 120:
            if sun >= 100:      # Sufficient Sun
                pygame.draw.rect(screen, (0, 255, 0), [0, 0, 90, 120])
                disText(font)
            elif sun < 100:     # Insufficient Sun
                pygame.draw.rect(screen, (255, 0, 0), [0, 0, 90, 120])
                disText(font)
        
        elif hoverY > 120 and hoverY <= 240:
            if sun >= 50:      # Sufficient Sun
                pygame.draw.rect(screen, (0, 255, 0), [0, 121, 90, 119])
                disText(font)
            elif sun < 50:     # Insufficient Sun
                pygame.draw.rect(screen, (255, 0, 0), [0, 121, 90, 119])
                disText(font)

        elif hoverY > 240 and hoverY <= 360:
            if sun >= 50:      # Sufficient Sun
                pygame.draw.rect(screen, (0, 255, 0), [0, 241, 90, 119])
                disText(font)
            elif sun < 50:     # Insufficient Sun
                pygame.draw.rect(screen, (255, 0, 0), [0, 241, 90, 119])
                disText(font)

    # events
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            running = False

        # Selecting and Placing Plants
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if x <= 90:
                # selecting peashooter
                if y >= 0 and y <= 120:
                    if sun >= 100:
                        position = 1
                    elif sun < 100:
                        err = True

                # selecting sunflower
                elif y > 120 and y <= 240:
                    if sun >= 50:
                        position = 2
                    elif sun < 50:
                        err = True

                # selecting barrier
                elif y > 240 and y <= 360:
                    if sun >= 50:
                        position = 3
                    elif sun < 50:
                        err = True
                               
            # placing the plant
            elif x > 90 and x <= 810:
                x, y, col, row = plants(x, y)
                if occupiedList[row][col] == 0 and position != 0:
                    occupiedList[row][col] = 1
                    if position == 1:
                        sun -= 100
                        shooter = Shooter(x, y, row)
                        position = 0
                    elif position == 2:
                        sun -= 50
                        sunflower = Sunflower(x, y, row)
                        position = 0
                    elif position == 3:
                        sun -= 50
                        barrier = Barrier(x, y, row)
                        position = 0
                elif occupiedList[row][col] == 1:
                    position = 0
            
            # when clicked elsewhere
            else:
                position = 0

    if err == True:
        errorStatTime = curTime
        err = False
    
    if curTime - errorStatTime < 750:
        disErr()

    # zombie spawning
    zombieSpawnInterval = 7500 if level == 1 else 6000
    if curTime - spawnStatTime > zombieSpawnInterval and zombieCounter < 10*level:
        spawnStatTime = curTime
        rowSelRand = random.randint(0, 1000)
        rowSelRand = rowSelRand%5
        zom = Zombie(810, rowSelRand * 120 + 19, rowSelRand)
        zombieCounter += 1

    # collision detection
    for bullet in Bullet.List:
        for zom in Zombie.List:
            if bullet.row == zom.row:
                if bullet.xCoor >= zom.xCoor:
                    # removing bullet from list and deleting instance
                    Bullet.List.remove(bullet)
                    del bullet

                    # damaging zombie
                    zom.Damage()
                    # deleting zombie if health becomes zero
                    if zom.health == 0:
                        Zombie.List.remove(zom)
                        del zom
                        if zombieCounter == 10*level and level == 1:
                            spawnStatTime = pygame.time.get_ticks()     # for spawning zombies
                            bulStatTime = pygame.time.get_ticks()       # for moving the bullet
                            hitStatTime = pygame.time.get_ticks()       # for damaging a plant
                            shootStatTime = pygame.time.get_ticks()     # for shooting
                            zomStatTime = pygame.time.get_ticks()       # for moving the zombies
                            sunStatTime = pygame.time.get_ticks()       # for sun
                            sunflowerStatTime = pygame.time.get_ticks() # for spawning sun by sunflower

                            position = 0        # to select which plant is placed
                            game_over = False   # to detect if user lost the game
                            sun = 50            # initial sun
                            level = 2           # level
                            zombieCounter = 0   # number of zombies spawned
                            delInst()
                            occupiedList = [[0 for i in range(1,10)] for i in range(5)]

                        elif zombieCounter == 10*level and level == 2:
                            game_over = True

                    break

    # zombie-pant interaction
    interact(Shooter.List)
    interact(Barrier.List)
    interact(Sunflower.List)
    
    # shooter shooting
    for shooter in Shooter.List:
        for zombie in Zombie.List:
            if shooter.row == zombie.row:
                if curTime - shootStatTime > 2000 :
                    bull = Bullet(shooter.xCoor + 30, shooter.yCoor + 10, shooter.row)
                    break

    # zombie hitting (every 1 sec)
    if curTime - hitStatTime > 1000:
        hitStatTime = curTime

    # plant shooting (every 1 sec)
    if curTime - shootStatTime > 2000:
        shootStatTime = curTime

    # tasks to be done each loop
    # zombie moving
    if (curTime - zomStatTime) > 50:
        zomStatTime = curTime
        for i in Zombie.List:
            if i.Moving:
                i.Move()
            if i.xCoor <= 90:
                game_over = True
    
    # bullet moving
    if (curTime - bulStatTime) > 10:
        bulStatTime = curTime
        for i in Bullet.List:
            i.Move()

            # deletes bullet if out of screen
            if i.xCoor >= 900:
                Bullet.List.remove(i)
                del i
    
    # displaying instances
    display_entities(Zombie.List)
    display_entities(Shooter.List)
    display_entities(Barrier.List)
    display_entities(Sunflower.List)
    display_entities(Bullet.List)
    
    if err == True:
        errorStatTime = curTime
        err = False
    
    if curTime - errorStatTime < 750:
        disErr()

    pygame.display.update()
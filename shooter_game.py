from pygame import *
from random import randint

with open("localization.txt", "r", encoding = "utf-8") as file:
    localization = file.read(1).lower()

esc = False

window = display.set_mode((700, 500))
display.set_caption("Galaxy Shooter")
clock = time.Clock()

mixer.init()

run = True

pul = []
enemies = []
meteories = []
hearts = []


gg = 0
ggg = 0
wait = 0 
score = 0
gggg = 0
pop = 0
f11 = False
pisun = True
pyk = True

font.init()
font1 = font.SysFont("Times new roman", 59)
if localization == "r":
    welcome = font1.render("Счет: 0", True, (255, 215, 0))

elif localization == "k":
    welcome = font1.render("Lik: 0", True, (255, 215, 0))
    
elif localization == "a":
    welcome = font1.render("Śkora: 0", True, (255, 215, 0))

elif localization == "p":
    welcome = font1.render("Shet: 0", True, (255, 215, 0))

else:
    welcome = font1.render("Score: 0", True, (255, 215, 0))
    
    


class Player(sprite.Sprite):
    def __init__(self, filename, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (75, 75))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def left(self):
        self.rect.x -= self.speed
    
    def right(self):
        self.rect.x += self.speed

    def up(self):
        self.rect.y -= self.speed
    
    def down(self):
        self.rect.y += self.speed
    

    def fire(self):
        pass

class Start(sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename), (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x_x, y_y):
        return self.rect.collidepoint(x_x, y_y)

class Pulya(sprite.Sprite):
    def __init__(self, filename, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (40, 50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def up(self):
        self.rect.y -= self.speed

    def dohuya(self):
        self.rect.x += 1000

class Enemy(sprite.Sprite):
    def __init__(self, filename, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (100, 60))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def down(self):
        self.rect.y += self.speed

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def dohuya(self):
        self.rect.x -= 1000

class Meteor(sprite.Sprite):
    def __init__(self, filename, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (60, 60))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def down(self):
        self.rect.y += self.speed

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def dohuya(self):
        self.rect.x -= 1000

class Heart(sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Restart(sprite.Sprite):
    def __init__(self, x , y , width, height, color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.color1 = color

    def set_text(self, text_color, text):
        self.text = text
        self.image = font1.render(text, True, text_color)

    def draw(self):
        draw.rect(window, self.color1, self.rect)
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def outline(self, ccolor, thickness):
        draw.rect(window, ccolor, self.rect, thickness)
        
start = Start("start.png", 150, 50)
start1 = True
background = transform.scale(image.load("galaxy1.jpg"), (700, 500))
while start1:
    window.blit(background, (0, 0))
    start.draw()

    for ee in event.get():
        if ee.type == MOUSEBUTTONDOWN and ee.button == 1:
            x_x_x, y_y_y = ee.pos
            if start.collidepoint(x_x_x, y_y_y):
                start1 = False

        if ee.type == KEYDOWN:

            if ee.key == K_F11:
                if f11 == False:
                    window = display.set_mode((700, 500), FULLSCREEN)
                    f11 = True

                elif f11 == True:
                    window = display.set_mode((700, 500))
                    f11 = False
            
        if ee.type == QUIT:
            run = False
            start1 = False
            pisun = False
            pyk = False


    display.update()
    clock.tick(40)

while pyk:
    pul = []
    enemies = []
    meteories = []
    hearts = []

    with open("score.txt", "r", encoding = "utf-8") as file:
        data = file.read()

    if localization == "r":
        data1 = font1.render("Рекорд: " + str(data), True, (255, 215, 0))

    elif localization == "k":
        data1 = font1.render("Baw Najvyšejšy: " + str(data), True, (255, 215, 0))

    elif localization == "a":
        data1 = font1.render("Rżekord: " + str(data), True, (255, 215, 0))

    elif localization == "p":
        data1 = font1.render("Rekord: " + str(data), True, (255, 215, 0))

    else:
        data1 = font1.render("Record: " + str(data), True, (255, 215, 0))


    gg = 0
    ggg = 0
    wait = 0 
    score = 0
    gggg = 0
    pop = 0
    f11 = False
    pisun = True
    run = True

    mixer.music.load("space.ogg")
    mixer.music.play()

    if localization == "r":
        welcome = font1.render("Счет: " + str(score), True, (255, 215, 0))

    elif localization == "k":
        welcome = font1.render("Lik: " + str(score), True, (255, 215, 0))

    elif localization == "a":
        welcome = font1.render("Śkora: " + str(score), True, (255, 215, 0))

    elif localization == "p":
        welcome = font1.render("Shet: " + str(score), True, (255, 215, 0))

    else:
        welcome = font1.render("Score: " + str(score), True, (255, 215, 0))

    rocket = Player("rocket.png", 310, 420, 7)
    xxx = 400
    for jpg in range(5):
        w = Heart("heart.png", xxx , 0)
        xxx += 60
        hearts.append(w)

    while run:
        if esc == False:
            keys = key.get_pressed()

            if keys[K_a] and rocket.rect.x > 5:
                rocket.left()

            if keys[K_d] and rocket.rect.x < 620:
                rocket.right()

            if keys[K_SPACE] and gg != 1 and ggg == 0:
                ggg = 25 
                d = Pulya("bullet.png", rocket.rect.centerx - 18, rocket.rect.y , randint(2, 6))
                pul.append(d)
                gg = 1
                kick = mixer.Sound('fire.ogg')
                kick.play()

            if ggg > 0:
                ggg -= 1


            if not keys[K_SPACE]:
                gg = 0


            if wait == 0:
                ppp = randint(1, 10)
                if ppp == 1:
                    l = Meteor("asteroid.png", randint(1, 640), 0, randint(1, 2))
                    meteories.append(l)
                elif len(enemies) != 6 and ppp >= 2:
                    a = Enemy("ufo.png", randint(1, 600), 0, randint(1, 2))
                    enemies.append(a)
                wait = randint(50, 70)

                
            wait -= 1

            window.blit(background, (0, 0))
            window.blit(welcome, (0, 0))
            window.blit(data1, (0, 50))

            for i in pul:
                i.up()
                i.draw()

            for meter in meteories:
                meter.down()
                meter.draw()

                if meter.colliderect(rocket):   
                    if pop < 4:
                        pop += 1

                        kkk = 0
                        for png in hearts:
                            if kkk == 0:
                                kkk = 1
                                hearts.remove(png)

                        meteories.remove(meter)
                        meter.dohuya()

                    else:
                        run = False
                        if localization == "r":
                            brawl = font1.render("Вы проиграли!", True, (255, 0, 0))

                        elif localization == "k":
                            brawl = font1.render("Zleŭ!", True, (255, 0, 0))

                        elif localization == "a":
                            brawl = font1.render("Wy ŭ porażnie!", True, (255, 0, 0))

                        elif localization == "p":
                            brawl = font1.render("Vi proigrali!", True, (255, 0, 0))

                        else:
                            brawl = font1.render("You lose!", True, (255, 0, 0))

                        window.blit(brawl, (200, 200))

                        if score > int(data):

                            with open("score.txt", "w", encoding = "utf-8") as file:
                                file.write(str(score))
                    

            for enemy1 in enemies:
                enemy1.draw()
                enemy1.down()

                if enemy1.rect.y > 500 or enemy1.colliderect(rocket):

                    if pop < 4:
                        pop += 1

                        kkk = 0
                        for png in hearts:
                            if kkk == 0:
                                kkk = 1
                                hearts.remove(png)
                        
                        enemies.remove(enemy1)
                        enemy1.dohuya()
                    
                    else:
                        run = False
                        if localization == "r":
                            brawl = font1.render("Вы проиграли!", True, (255, 0, 0))

                        elif localization == "k":
                            brawl = font1.render("Zleŭ!", True, (255, 0, 0))

                        elif localization == "a":
                            brawl = font1.render("Wy ŭ porażnie!", True, (255, 0, 0))

                        elif localization == "p":
                            brawl = font1.render("Vi proigrali!", True, (255, 0, 0))

                        else:
                            brawl = font1.render("You lose!", True, (255, 0, 0))

                        window.blit(brawl, (200, 200))

                        if score > int(data):

                            with open("score.txt", "w", encoding = "utf-8") as file:
                                file.write(str(score))

                for i1 in pul:
                    if enemy1.colliderect(i1):
                        enemy1.dohuya()
                        i1.dohuya()
                        enemies.remove(enemy1)
                        pul.remove(i1)
                        score += 1
                        if localization == "r":
                            welcome = font1.render("Счет: " + str(score), True, (255, 215, 0))

                        elif localization == "k":
                            welcome = font1.render("Lik: " + str(score), True, (255, 215, 0))

                        elif localization == "a":
                            welcome = font1.render("Śkora: " + str(score), True, (255, 215, 0))

                        elif localization == "p":
                            welcome = font1.render("Shet: " + str(score), True, (255, 215, 0))

                        else:
                            welcome = font1.render("Score: " + str(score), True, (255, 215, 0))

            for png in hearts:
                png.draw()


            rocket.draw()

            clock.tick(60)
            display.update()

        if esc == True:
            rocket.draw()
            for i1 in pul:
                i1.draw()

            for enemy11 in enemies:
                enemy11.draw()
            


        for e in event.get():
            if e.type == KEYDOWN:

                if e.key == K_F11:
                    if f11 == False:
                        window = display.set_mode((700, 500), FULLSCREEN)
                        f11 = True

                    elif f11 == True:
                        window = display.set_mode((700, 500))
                        f11 = False

                if e.key == K_ESCAPE:
                    if esc == False:
                        esc = True
                
                    elif esc == True:
                        esc = False

            if e.type == QUIT:
                run = False
                pisun = False
                pyk = False
                if score > int(data):
                        
                    with open("score.txt", "w", encoding = "utf-8") as file:
                        file.write(str(score))

    gg = 0
    pas = True

    restart = Restart(520, 400, 160, 80, (255, 255, 0))
    restart.set_text((0, 0, 0), "restart")

    restart_meh = False

    while gg != 90 and pas and pisun:

        window.blit(background, (0, 0))
        window.blit(welcome, (0, 0))
        window.blit(data1, (0, 50))

        for jpeg in pul:
            jpeg.draw()

        for ico in enemies:
            ico.draw()

        rocket.draw()
        restart.draw()
        restart.outline((0, 0, 255), 5)
        display.update()
        clock.tick(40)
        gg += 1

        if gg == 89 and restart_meh == True:
            restart_meh == False

        elif gg == 89 and restart_meh == False:
            pyk = False

        for u in event.get():
            if u.type == QUIT:
                pas = False
                pyk = False

            elif u.type == MOUSEBUTTONDOWN and u.button == 1:
                x_x_x_x, y_y_y_y = u.pos
                if restart.collidepoint(x_x_x_x, y_y_y_y):
                    restart_meh = True

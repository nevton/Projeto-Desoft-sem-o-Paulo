# -*- coding: utf-8 -*-
"""
Created on Tue may 10 05:39:18 2019

@author: nevton
"""
import pygame
from pygame.locals import *
from random import randint

try:
	hulk = pygame.image.load("img/hulk.png")
	homemaranha = pygame.image.load("img/homem-aranha.png")
	ironman = pygame.image.load("img/ironman.png")
	thanos = pygame.image.load("img/thanos.png")
	capitaoamerica = pygame.image.load("img/capitaoamerica.png")
	handEmpty = pygame.image.load("img/maesemmanopla.png")
	joiaAmarela = pygame.image.load("img/joiaamarela.png")
	joiaAzul = pygame.image.load("img/joiaazul.png")
	joiaLaranja = pygame.image.load("img/joialaranja.png")
	joiaVerde = pygame.image.load("img/joiaVerde.png")
	joiaVermelha = pygame.image.load("img/joiaVermelha.png")
	joiaRoxa = pygame.image.load("img/joiaRoxa.png")	
	avengersss = pygame.image.load("img/avengers.jpg")
	thanosWin = pygame.image.load("img/thanoswin.gif")

except ValueError:
	print ('Cannot load someone image!')

joiaRoxaAtivada = False
joiaVerdeAtivada = False
joiaAmarelaAtivada = False
joiaAzulAtivada = False
joiaLaranjaAtivada = False
joiaVermelhaAtivada = False
winGame = False
vidaGasta = 0

class Maze():

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.GOLD = (246, 253, 49)
        self.GREY = (50, 50, 50)
        self.RED = (255, 0, 0)
        self.BLUE = (20, 27, 229)
        self.BLUEJOIA = (26, 26, 255)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.PURPLE = (128, 0, 128)
        self.ORANGE = (255, 143, 32)
        self.YELLOW = (174, 174, 0)
        self.walls = []
        self.width = 20
        self.height = 20
        self.margin = 1
        self.score = 0
        self.level = 1
        self.grid = []
        self.countfinal = 0
        self.make()
        self.size = [1200, 700]
        self.screen = pygame.display.set_mode(self.size)

    def make(self):	
        for i in range(0, 30):
            self.walls.append([0, i])
        for i in range(0, 27):
            self.walls.append([i, 0])
        for i in range(0, 30):
            self.walls.append([26,i])
        for i in range(0, 27):
            self.walls.append([i, 29])
        
        for i in range(2, 5):
            for j in range(2, 5):
                self.walls.append([j, i])
        for i in range(2, 5):
            for j in range(6, 11):
                self.walls.append([j, i])
        for i in range(1, 5):
            for j in range(12, 14):
                self.walls.append([j, i])
        for i in range(2, 5):
            for j in range(15, 21):
                self.walls.append([j, i])
            for j in range(22, 25):
                self.walls.append([j, i])

        for i in range(6, 8):
            for j in range(2, 5):
                self.walls.append([j, i])
        for i in range(9, 15):
            for j in range(0, 5):
                self.walls.append([j, i])
        for i in range(6, 15):
            for j in range(6, 8):
                self.walls.append([j, i])
        for i in range(9, 11):
            for j in range(8, 11):
                self.walls.append([j, i])
        for i in range(6, 8):
            for j in range(9, 17):
                self.walls.append([j, i])
        
        for i in range(8, 11):
            for j in range(12, 14):
                self.walls.append([j, i])

        for i in range(6, 8):
            for j in range(2+20, 5+20):
                self.walls.append([j, i])
        for i in range(9, 15):
            for j in range(0+21, 5+21):
                self.walls.append([j, i])
        for i in range(6, 15):
            for j in range(6+12, 8+12):
                self.walls.append([j, i])
        for i in range(9, 11):
            for j in range(8+7, 11+7):
                self.walls.append([j, i])
        for i in range(9+7, 15+7):
            for j in range(0, 5):
                self.walls.append([j, i])
        for i in range(23, 28):
            for j in range(2, 5):
                self.walls.append([j, i])
        for i in range(6+10, 6+16):
            for j in range(6, 8):
                self.walls.append([j, i])
        for i in range(6+14, 6+16):
            for j in range(8, 10):
                self.walls.append([j, i])
        for i in range(6+10, 6+16):
            for j in range(6+12, 8+12):
                self.walls.append([j, i])
        for i in range(6+14, 6+16):
            for j in range(8+8, 10+8):
                self.walls.append([j, i])
        for i in range(9+7, 15+7):
            for j in range(0+21, 5+21):
                self.walls.append([j, i])
        for i in range(6+14, 6+16):
            for j in range(8+3, 10+5):
                self.walls.append([j, i])
        for i in range(29-6, 29):
            for j in range(12, 14):
                self.walls.append([j, i])
        
        for i in range(23, 28):
            for j in range(6, 8):
                self.walls.append([j, i])
        
        for i in range(23, 25):
            for j in range(9, 11):
                self.walls.append([j, i])

        for i in range(26, 28):
            for j in range(9, 11):
                self.walls.append([j, i])
        for i in range(23, 25):
            for j in range(9+6, 11+6):
                self.walls.append([j, i])
        for i in range(23, 25):
            for j in range(9+6, 11+6):
                self.walls.append([j, i])
        for i in range(26, 28):
            for j in range(9+6, 11+6):
                self.walls.append([j, i])
        for i in range(23, 28):
            for j in range(18, 20):
                self.walls.append([j, i])
        for i in range(23, 28):
            for j in range(21, 23):
                self.walls.append([j, i])
        for i in range(26, 28):
            for j in range(23, 25):
                self.walls.append([j, i])

        for i in range(22, 25):
            for j in range(24, 26):
                self.walls.append([j, i])
        for i in range(13, 18):
            for j in range(9, 17):
                self.walls.append([j, i])

        for row in range(30):
            self.grid.append([])
            for column in range(40):
                self.grid[row].append(0)
        for wall in self.walls:
            self.grid[wall[1]][wall[0]]=1
        self.grid[15][1]=1
        return self
    
    def reset(self):
        self.grid = []
        self.walls = []
        self.countfinal = 0
        self.make()

        global joiaAmarelaAtivada, joiaAzulAtivada, joiaLaranjaAtivada, joiaRoxaAtivada
        global joiaVerdeAtivada, joiaVermelhaAtivada, vidaGasta

        joiaAmarelaAtivada = False
        joiaAzulAtivada = False
        joiaLaranjaAtivada = False
        joiaRoxaAtivada = False
        joiaVerdeAtivada = False
        joiaVermelhaAtivada = False
        vidaGasta = 0
        return self

    def scoredisp(self):
        scoretext = self.scorefont.render("Score: "+(str)(self.score), 1, self.RED)
        self.screen.blit(scoretext, (640, 220))
        

        global handEmpty
        self.screen.blit(handEmpty, (600, 250))
        self.screen.blit(avengersss, (194, 284))
        if joiaVerdeAtivada:
            self.screen.blit(joiaVerde, (770, 380))
        if joiaVermelhaAtivada:
            self.screen.blit(joiaVermelha, (665, 345))
        if joiaAzulAtivada:
            self.screen.blit(joiaAzul, (700, 345))
        if joiaLaranjaAtivada:
            self.screen.blit(joiaLaranja, (635, 345))
        if joiaAmarelaAtivada:
            self.screen.blit(joiaAmarela, (680, 370))
        if joiaRoxaAtivada:
            self.screen.blit(joiaRoxa, (725, 345))
        global winGame
        if winGame:
            pygame.time.delay(1000)
            self.screen.blit(thanosWin, (30, 30))
            pygame.time.delay(1000)
            winGame = False

    def dispmaze(self):
        for row in range(30):
            for column in range(27):
                color = self.GREY
                pygame.draw.rect(self.screen, color, [(self.margin+self.width)*column+self.margin,(self.margin+self.height)*row+self.margin, self.width, self.height])
                color = self.GOLD
                if self.grid[row][column] == 0:
                    pygame.draw.rect(self.screen, color, [(self.margin+self.width)*column+self.margin+7,(self.margin+self.height)*row+self.margin+7, self.width-14, self.height-14])
                    self.countfinal += 1
    
        if self.grid[1][25] == 0:
            color = self.GREEN
            pygame.draw.circle(self.screen,color,[(self.margin+self.width)*25+self.margin+10,(self.margin+self.height)*1+self.margin+10], 5, 5)
        if self.grid[15][1] == 0:
            color = self.ORANGE
            pygame.draw.circle(self.screen,color,[(self.margin+self.width)*1+self.margin+10,(self.margin+self.height)*15+self.margin+10], 5, 5)
        if self.grid[1][1] == 0:
            color = self.BLUEJOIA
            pygame.draw.circle(self.screen,color,[(self.margin+self.width)*1+self.margin+10,(self.margin+self.height)*1+self.margin+10], 5, 5)
        if self.grid[27][25] == 0:
            color = self.RED
            pygame.draw.circle(self.screen,color,[(self.margin+self.width)*25+self.margin+10,(self.margin+self.height)*27+self.margin+10], 5, 5)
        if self.grid[15][25] == 0:
            color = self.PURPLE
            pygame.draw.circle(self.screen,color,[(self.margin+self.width)*25+self.margin+10,(self.margin+self.height)*15+self.margin+10], 5, 5)
        if self.grid[27][1] == 0:
            color = self.YELLOW
            pygame.draw.circle(self.screen,color,[(self.margin+self.width)*1+self.margin+10,(self.margin+self.height)*27+self.margin+10], 5, 5)


    def drawwalls(self):
        for wall in self.walls:
            pygame.draw.rect(self.screen,self.BLUE,[(self.margin+self.width)*wall[0]+self.margin,(self.margin+self.height)*wall[1]+self.margin,self.width,self.height])


class Person(Maze):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def checkWall(self, x, y, W):
        if [x, y] in W:
            return True
        else:
            return False

    def moveleft(self, W):
        if self.x > 0:
            if self.checkWall(self.x-1, self.y, W):
                self.x = self.x
            else:
                self.x = self.x-1
        return self

    def moveright(self, W):
        if self.x < 39:
            if self.checkWall(self.x+1, self.y, W):
                self.x = self.x
            else:
                self.x = (self.x)+1

        return self

    def moveup(self, W):
        if self.y > 0:
            if self.checkWall(self.x, self.y-1, W):
                self.y = self.y
            else:
                self.y = self.y -1
        return self

    def movedown(self, W):
        if self.y < 29:
            if self.checkWall(self.x, self.y+1, W):
                self.y = self.y
            else:
                self.y = self.y + 1

        return self

class Thanos(Person):
    def __init__(self):
        x = 14
        y = 18
        Person.__init__(self, x, y)

    def resetThanos(self):
        x = 14
        y = 18
        Person.__init__(self, x, y)

    def winGame(self):
        if joiaAmarelaAtivada and joiaAzulAtivada and joiaLaranjaAtivada and joiaRoxaAtivada and joiaVerdeAtivada and joiaVermelhaAtivada:
            global winGame
            winGame = True
            return True

    def avengersWinsss(self):
        global avengersWins
        avengersWins = True
        return True
    
    def collectCoin(self, Wa):
        if(self.y == 1 and self.x == 25):
            global joiaVerdeAtivada
            joiaVerdeAtivada = True
            
        if(self.y == 25 and self.x == 1):
            global joiaAmarelaAtivada
            joiaAmarelaAtivada = True
            
        if(self.y == 1 and self.x == 1):
            global joiaAzulAtivada
            joiaAzulAtivada = True
            
        if self.y == 27 and self.x == 25:
            global joiaVermelhaAtivada
            joiaVermelhaAtivada = True

        if self.y == 15 and self.x == 1:
            global joiaLaranjaAtivada
            joiaLaranjaAtivada = True
        
        if self.y == 15 and self.x == 25:
            global joiaRoxaAtivada
            joiaRoxaAtivada = True

        if joiaAzulAtivada and self.y == 15 and self.x == 25:
            self.x = 2
            self.y = 15
            
        if joiaAzulAtivada and self.y == 15 and self.x == 1:
            self.x = 24
            self.y = 15
            

        if Wa.grid[self.y][self.x] == 0:
            return True
        else:
            return False

    
    def pacright(self, Wa):
        Person.moveright(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self

    def pacleft(self, Wa):
        Person.moveleft(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self

    def pacup(self, Wa):
        Person.moveup(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self
    
    def pacdown(self, Wa):
        Person.movedown(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self

    def pos(self, G):
        global thanos
        G.screen.blit(thanos, ((G.margin+G.width)*self.x+G.margin+3, (G.margin+G.height)*self.y+G.margin))

    def checkGhost(self, V):
        global vidaGasta
        if [self.x, self.y] == [V.x, V.y]:
            if joiaRoxaAtivada:
                V.x = 10000
                V.y = 10000
                
            elif joiaLaranjaAtivada and vidaGasta == 0:
                self.x = 14
                self.y = 18
                vidaGasta = 1
            else:
                return True
        else:
            return False
        
    def checkHulk(self, V):
        global vidaGasta
        if [self.x, self.y] == [V.x, V.y]:
            if joiaRoxaAtivada and joiaVermelhaAtivada:
                V.x = 10000
                V.y = 10000
                
                
            elif joiaLaranjaAtivada and vidaGasta == 0:
                self.x = 14
                self.y = 18
                vidaGasta = 1
            else:
                return True
        else:
            return False    

    def pacPosition(self, G):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pacleft(G)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pacright(G)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.pacup(G)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.pacdown(G)

class Ghost(Person):
    def __init__(self, avengers):
        self.avengers = avengers
        x=1
        y=1
        if (avengers == "homemaranha"):
            x=1
            y=1
        if(avengers == "ironman"):
            x=1
            y=25
        if(avengers == "capitaoamerica"):
            x=25
            y=25
        Person.__init__(self, x, y)

    def ghleft(self, Wa):
        Person.moveleft(self,Wa.walls)
        return self
    def ghright(self, Wa):
        Person.moveright(self,Wa.walls)
        return self
    def ghup(self, Wa):
        Person.moveup(self,Wa.walls)
        return self
    def ghdown(self, Wa):
        Person.movedown(self,Wa.walls)
        return self

    def pos(self, G):
        if self.avengers == "homemaranha":
            G.screen.blit(homemaranha, ((G.margin+G.width)*self.x+G.margin, (G.margin+G.height)*self.y+G.margin))
        if(self.avengers == "ironman"):
            G.screen.blit(ironman, ((G.margin+G.width)*self.x+G.margin, (G.margin+G.height)*self.y+G.margin))
        if(self.avengers == "capitaoamerica"):
            G.screen.blit(capitaoamerica, ((G.margin+G.width)*self.x+G.margin, (G.margin+G.height)*self.y+G.margin))

    def ghostPosition(self, G):
        move = randint(0, 3)
        if move == 0:
            self.ghleft(G)
        if move == 1:
            self.ghright(G)
        if move == 2:
            self.ghup(G)
        if move == 3:
            self.ghdown(G)

class Hulk(Person):
    def __init__(self, avengers):
        self.avengers = avengers
        x=1
        y=1
        
        if(avengers == "hulk"):
            x=25
            y=1

        Person.__init__(self, x, y)

    def hleft(self, Wa):
        Person.moveleft(self,Wa.walls)
        return self
    def hright(self, Wa):
        Person.moveright(self,Wa.walls)
        return self
    def hup(self, Wa):
        Person.moveup(self,Wa.walls)
        return self
    def hdown(self, Wa):
        Person.movedown(self,Wa.walls)
        return self

    def pos(self, G):
        if(self.avengers == "hulk"):
            G.screen.blit(hulk, ((G.margin+G.width)*self.x+G.margin, (G.margin+G.height)*self.y+G.margin))

    def hPosition(self, G):
        move = randint(0, 1)
        if self.x == 25:
            if move == 1 or move == 0:
                self.hdown(G)
        if self.y == 9:
            if move == 1 or move == 0:
                self.hleft(G)
        if self.x == 19:
            if move == 1 or move == 0:
                self.hup(G)
        if self.y == 5:
            if move == 1 or move == 0:
                self.hleft(G)
        if self.x == 14:
            if move == 1 or move == 0:
                self.hup(G)
        if self.y == 1:
            if move == 1 or move == 0:
                self.hright(G)
            
        return self
            
            
if __name__ == "__main__" or __name__ == "Thanos":
    GAME = Maze()
    HERO = Thanos()
    VILAO = Ghost("homemaranha")
    VILAO2 = Hulk("hulk")
    VILAO3 = Ghost("capitaoamerica")
    VILAO4 = Ghost("ironman")
    
    pygame.init()
    GAME.scorefont = pygame.font.Font(None, 30)
    done = False
    clock = pygame.time.Clock()

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_q:
                    done = True

        HERO.pacPosition(GAME)
        GAME.screen.fill(GAME.BLACK)
        VILAO.ghostPosition(GAME)
        VILAO2.hPosition(GAME)
        VILAO3.ghostPosition(GAME)
        VILAO4.ghostPosition(GAME)
        move = randint(0, 3)
        GAME.countfinal = 0
        GAME.dispmaze()
        GAME.drawwalls()
        HERO.pos(GAME)
        VILAO.pos(GAME)
        VILAO2.pos(GAME)
        VILAO3.pos(GAME)
        VILAO4.pos(GAME)

        if HERO.checkGhost(VILAO) or HERO.checkHulk(VILAO2) or HERO.checkGhost(VILAO3) or HERO.checkGhost(VILAO4):
            done = True
            print ("VOCE FOI DERROTADO\nFinal Score = "+(str)(GAME.score))
        elif GAME.countfinal == 287 or HERO.winGame():
            GAME.reset()
            HERO.resetThanos()
            VILAO = Ghost("homemaranha")
            VILAO2 = Hulk("hulk")
            VILAO3 = Ghost("capitaoamerica")
            VILAO4 = Ghost("ironman")
        GAME.level += 1
        GAME.scoredisp()
        clock.tick(10)
        if joiaVerdeAtivada:
            clock.tick(6)
        pygame.display.flip()
    pygame.quit()

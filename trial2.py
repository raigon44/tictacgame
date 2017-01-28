import pygame,sys,random,time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("Trial No : 1")
font = pygame.font.SysFont("arial",30)

#pygame.draw.circle(screen,(255,0,0),(50,50),10)
pygame.display.update()

global player
player = 1 
global cell

cell = [2,2,2,2,2,2,2,2,2]


def winner(win):

    count = 0
    global cell

    if win == 1:

        if cell[0] == 1 and cell[1]== 1 and cell[2] == 1 :
            screen.fill((255,255,255))
            text = font.render("PLAYER 1 WINS",True,(255,0,0),(255,255,255))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            print count
            return 1
        if cell[3] == 1 and cell[4]== 1 and cell[5] == 1:
            text = font.render("PLAYER 1 WINS",True,(255,0,0),(255,255,255))
            screen.blit(text,(37,37+font.get_linesize()))            
            pygame.display.update()
            return 1   
        if cell[6] == 1 and cell[7]== 1 and cell[8] == 1 :
            text = font.render("PLAYER 1 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1   
        if cell[0] == 1 and cell[4]== 1 and cell[8] == 1 :
            text = font.render("PLAYER 1 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1 
        if cell[2] == 1 and cell[4]== 1 and cell[6] == 1 :
            text = font.render("PLAYER 1 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1                                        
        if cell[0] == 1 and cell[3]== 1 and cell[6] == 1 :
            text = font.render("PLAYER 1 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1
        if cell[1] == 1 and cell[4]== 1 and cell[7] == 1 :
            text = font.render("PLAYER 1 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1
        if cell[2] == 1 and cell[5]== 1 and cell[8] == 1 :
            text = font.render("PLAYER 1 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1  
    
    else :

        if cell[0] == 0 and cell[1]== 0 and cell[2] == 0 :
            screen.fill((255,255,255))            
            text = font.render("PLAYER 2 WINS",True,(255,0,0),(255,255,255))
            screen.blit(text,(37,37+font.get_linesize()))            
            pygame.display.update()
            return 1
        if cell[3] == 0 and cell[4]== 0 and cell[5] == 0 :
            text = font.render("PLAYER 2 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1   
        if cell[6] == 0 and cell[7]== 0 and cell[8] == 0 :
            text = font.render("PLAYER 2 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1   
        if cell[0] == 0 and cell[4]== 0 and cell[8] == 0 :
            text = font.render("PLAYER 2 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1 
        if cell[2] == 0 and cell[4]== 0 and cell[6] == 0 :
            text = font.render("PLAYER 2 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1                                        
        if cell[0] == 0 and cell[3]== 0 and cell[6] == 0 :
            text = font.render("PLAYER 2 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1
        if cell[1] == 0 and cell[4]== 0 and cell[7] == 0 :
            text = font.render("PLAYER 2 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1
        if cell[2] == 0 and cell[5]== 0 and cell[8] == 0 :
            text = font.render("PLAYER 2 WINS",True,(255,0,0))
            screen.blit(text,(37,37+font.get_linesize()))
            pygame.display.update()
            return 1  

    for inc in range(0,9):
        if cell[inc] == 1 or cell[inc] == 0 :
            count = count + 1
    if count == 9:
        text = font.render("Game is a Draw ",True,(255,0,0)) 
        screen.blit(text,(37,37+font.get_linesize()))
        pygame.display.update()
        return 1                             


def colorinp(a,b):

    global player
    global cell
    if  player == 1 :

        print player
        if a > 0 and a < 100:
            if b > 0 and b < 100:
                if cell[0] == 2 :
                    cell[0] = 1


                    pygame.draw.circle(screen,(255,0,0),(50,50),10)
                    pygame.display.update()
                    return player
                    #print event.pos[1]
                    #print event.pos[0]
                else :
                    return    
            if b > 100 and b < 200:
                if cell[1] == 2:
                    cell[1] = 1

                    pygame.draw.circle(screen,(255,0,0),(50,150),10)
                    pygame.display.update()
                    return player
                else :
                    return                  
            if b > 200 and b < 300:
                    if cell[2] == 2:
                        cell[2] = 1

                        pygame.draw.circle(screen,(255,0,0),(50,250),10)
                        pygame.display.update() 
                        return player
                    else :
                        return


        if a > 100 and a < 200:
            if b > 0 and b < 100:
                if cell[3] == 2:
                    cell[3] = 1

                    pygame.draw.circle(screen,(255,0,0),(150,50),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 100 and b < 200:
                if cell[4] == 2:
                    cell[4] = 1

                    pygame.draw.circle(screen,(255,0,0),(150,150),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 200 and b < 300:
                if cell[5] == 2:
                    cell[5] = 1                
                    pygame.draw.circle(screen,(255,0,0),(150,250),10) 
                    pygame.display.update()
                    return player
                else :
                    return                    

        if a > 200 and a < 300:
            if b > 0 and b < 100:
                if cell[6] == 2:
                    cell[6] = 1                 
                    pygame.draw.circle(screen,(255,0,0),(250,50),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 100 and b < 200:
                if cell[7] == 2:
                    cell[7] = 1                 
                    pygame.draw.circle(screen,(255,0,0),(250,150),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 200 and b < 300:
                if cell[8] == 2:
                    cell[8] = 1                 
                    pygame.draw.circle(screen,(255,0,0),(250,250),10) 
                    pygame.display.update()
                    return player
                else :
                    return                    
        #player = 0

    else :

        print player
        if a > 0 and a < 100:
            if b > 0 and b < 100:
                if cell[0] == 2 :
                    cell[0] = 0                
                    pygame.draw.circle(screen,(0,255,0),(50,50),10)
                    pygame.display.update()
                    #print event.pos[1]
                    #print event.pos[0]
                    return player
                else :
                    return                    
            if b > 100 and b < 200:
                if cell[1] == 2 :
                    cell[1] = 0                
                    pygame.draw.circle(screen,(0,255,0),(50,150),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 200 and b < 300:
                if cell[2] == 2 :
                    cell[2] = 0                
                    pygame.draw.circle(screen,(0,255,0),(50,250),10)
                    pygame.display.update()
                    return player 
                else :
                    return
        if a > 100 and a < 200:
            if b > 0 and b < 100:
                if cell[3] == 2 :
                    cell[3] = 0                
                    pygame.draw.circle(screen,(0,255,0),(150,50),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 100 and b < 200:
                if cell[4] == 2 :
                    cell[4] = 0                
                    pygame.draw.circle(screen,(0,255,0),(150,150),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 200 and b < 300:
                if cell[5] == 2 :
                    cell[5] = 0                
                    pygame.draw.circle(screen,(0,255,0),(150,250),10) 
                    pygame.display.update()
                    return player
                else :
                    return                    

        if a > 200 and a < 300:
            if b > 0 and b < 100:
                if cell[6] == 2 :
                    cell[6] = 0                
                    pygame.draw.circle(screen,(0,255,0),(250,50),10)
                    pygame.display.update()
                    return player
                else :
                    return                
            if b > 100 and b < 200:
                if cell[7] == 2 :
                    cell[7] = 0                
                    pygame.draw.circle(screen,(0,255,0),(250,150),10)
                    pygame.display.update()
                    return player
                else :
                    return                    
            if b > 200 and b < 300:
                if cell[8] == 2 :
                    cell[8] = 0                
                    pygame.draw.circle(screen,(0,255,0),(250,250),10) 
                    pygame.display.update()
                    return player
                else :
                    return                    

        #player = 1





while 1:
    #screen.fill(0)
    x = y = 0
    for i in range (0,3):
        for j in range (0,3):
            pygame.draw.rect(screen,(255,0,255),Rect((x,y),(100,100)),1)
            #pygame.draw.circle(screen,(255,0,0),(x+50,y+50),10)
            x = x + 100
        x = 0
        y = y + 100

    pygame.display.update()

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        if event.type==MOUSEBUTTONDOWN :
            #IF THE MOUSE IS CLICKED SOMEWHERE IN THE SCREEN THEN 
            if event.button==1 :
                ply = colorinp(event.pos[0],event.pos[1])
                if ply == 1:
                    cond = winner(1)
                    if cond == 1:
                        pygame.time.wait(10000)
                        exit(0)

                    player = 0
                else :
                    cond = winner(0)
                    if cond == 1:
                        pygame.time.wait(10000)
                        exit(0)
                    player = 1
                #pygame.draw.circle(screen,(255,0,0),(event.pos[0],event.pos[1]),10)
                pygame.display.update()




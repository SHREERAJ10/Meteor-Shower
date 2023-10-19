#PROJECT METEOR SHOWER BY SHREERAJ SHRESTHA

import pygame
from pygame import *
import os
import random


def display_score(stop):
        
        if stop == True:
            global final_score
            end_score = font.render(f"Your Score: {final_score}",False,"Green")
            screen.blit(end_score,(675,600))
            return 0

        elif stop == False:
                current_time = int((pygame.time.get_ticks() / 100) - start_time)
                final_score = current_time
                score = score_font.render(f"Score: {current_time}",False,"green")
                score_rect = score.get_rect(topleft = (330,200))
                screen.blit(score,score_rect)

        
        

pygame.init()
mixer.init()
game_active = False
start_time = 0

#game window and ceiling
screen_width= 1920
screen_height= 1080
screen = pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Meteor Shower")

#background image and title screen
abs_path = os.path.dirname(__file__)
bg = pygame.image.load(os.path.join(abs_path,"images/main_bg.jpg"))
title_font = pygame.font.Font(os.path.join(abs_path,"fonts and sound/title font.otf"),150)
title = title_font.render("Meteor Shower",False,(131,238,255))

#game elements
player = pygame.image.load(os.path.join(abs_path,"images/player.png"))
x_pos = 980
player_rect = player.get_rect(midbottom = (x_pos,875))

bullet = pygame.image.load(os.path.join(abs_path,"images/bullet.png"))
bullet_rect = bullet.get_rect(midbottom = (978,600))
bullet_rect2 = bullet.get_rect(midbottom = (100,600))
bullet_rect3 = bullet.get_rect(midbottom = (178,600))
bullet_rect4 = bullet.get_rect(midbottom = (178,600))
bullet_rect5 = bullet.get_rect(midbottom = (178,600))
speed= 0.004

score_font = pygame.font.Font(os.path.join(abs_path,"fonts and sound/gamefont.ttf"),25)
font = pygame.font.Font(os.path.join(abs_path,"fonts and sound/gamefont.ttf"),50)
start_text = font.render('Press "Spacebar" to start',None, "white")
end_text = font.render("Game Over!",None, "white")
played = False
stop = False

jethalal = mixer.Sound(os.path.join(abs_path,"fonts and sound/jethalal.mp3"))
badal_barsa = mixer.Sound(os.path.join(abs_path,"fonts and sound/badal baarsa.mp3"))
song = mixer.Sound(os.path.join(abs_path,"fonts and sound/meme song.mp3"))
mixer.Sound.play(jethalal)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

    def move_player(input):
        if input[pygame.K_a] or input[pygame.K_LEFT]:
            player_rect.x-=8
            if player_rect.x<=325:
                player_rect.x+=8
                #this line cancels out -=5 using +=5 giving illusion of spaceship not moving

        #secret feature
        elif input[pygame.K_LSHIFT]:
            player_rect.x-=16
            if player_rect.x<=325:
                player_rect.x+=16

        elif input[pygame.K_d] or input[pygame.K_RIGHT]:
            player_rect.x+=8
            if player_rect.x>=1500:
                player_rect.x-=8
        
        elif input[pygame.K_RSHIFT]:
            player_rect.x+=16
            if player_rect.x>=1500:
                player_rect.x-=16

        #easter egg
        
        if input[pygame.K_1]:
            name1 = font.render("Shreeraj Shrestha",False,(8,143,143))
            screen.blit(name1,(650,300))

    if game_active:

        screen.blit(bg,(0,0))
        screen.blit(player,player_rect)
        display_score(stop)
        input = pygame.key.get_pressed()
        #.get_pressed used for keys when player holds it down)

        move_player(input)

        screen.blit(bullet,bullet_rect)
        screen.blit(bullet,bullet_rect2)
        screen.blit(bullet,bullet_rect3)
        screen.blit(bullet,bullet_rect4)
        screen.blit(bullet,bullet_rect5)

        bullets = [bullet_rect, bullet_rect2,bullet_rect3,bullet_rect4,bullet_rect5]
        for fire in bullets:
            fire.y+= speed
            increase = random.randint(1,10)
            speed+=(increase/1000)

            if fire.y >= 899:
                fire.y = 180
                if fire == bullet_rect:
                    fire.x =random.randint(325,510)
                elif fire == bullet_rect2:
                    fire.x =random.randint(550,735)
                elif fire == bullet_rect3:
                    fire.x =random.randint(785,970)
                elif fire == bullet_rect4:
                    fire.x =random.randint(1020,1205)
                elif fire == bullet_rect5:
                    fire.x =random.randint(1255,1500)

            if fire.colliderect(player_rect):
                played=True
                mixer.Sound.stop(jethalal)
                mixer.Sound.stop(song)
                mixer.Sound.play(badal_barsa)
                game_active = False

    elif game_active == False and played== True:
        screen.blit(bg,(0,0))
        screen.blit(player,player_rect)
        screen.blit(bullet,bullet_rect)
        screen.blit(bullet,bullet_rect2)
        screen.blit(bullet,bullet_rect3)
        screen.blit(bullet,bullet_rect4)
        screen.blit(bullet,bullet_rect5)
        screen.blit(end_text,(750,500))
        stop = True
        display_score(stop)

        restart = pygame.key.get_pressed()
        if restart[pygame.K_SPACE]:
            bullet_rect = bullet.get_rect(midbottom = (978,200))
            bullet_rect2 = bullet.get_rect(midbottom = (100,200))
            bullet_rect3 = bullet.get_rect(midbottom = (178,300))
            bullet_rect4 = bullet.get_rect(midbottom = (178,250))
            bullet_rect5 = bullet.get_rect(midbottom = (178,340))
            speed= 0.004
            mixer.Sound.stop(badal_barsa)
            mixer.Sound.play(song)
            
            stop = False
            start_time= (pygame.time.get_ticks()/100)
            game_active = True

    elif game_active==False:
        screen.blit(bg,(0,0))
        screen.blit(title,(400,440))
        screen.blit(start_text,(475,700))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            
            mixer.Sound.stop(jethalal)
            mixer.Sound.stop(badal_barsa)
            mixer.Sound.play(song)
            game_active=True
            start_time= (pygame.time.get_ticks()/100)
    

        #print(pygame.mouse.get_pos())
    clock.tick(60)
    pygame.display.update()

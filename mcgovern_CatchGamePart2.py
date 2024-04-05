#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:23:40 2024

@author: thomasmcgovern
"""

import pygame, simpleGE, random

"""

Thomas McGovern
03/29/2024
Slide and Catch game
Objective of this assignment is to successfully create and animate a simple object catching game

"""
class Intro(simpleGE.Scene):
    def __init__(self, score = 0):
        super().__init__()
        self.setImage("WelcomeScreen.jpg")
        
        self.status = "quit"
        self.score = score
        
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.textLines = [
            "How to play: Catch as many footballs as you can ",
            "with D.J. Moore before the time runs out. Good luck!"]
        self.lblInstructions.center = (320, 310)
        self.lblInstructions.size = (550, 100)
        self.lblInstructions.color= ()
        
        self.lblScore = simpleGE.Label()
        self.lblScore.center = (500, 200)
        self.lblScore.size = (250, 30)
        self.lblScore.text = f"Previous Score: {self.score}"
      

        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (150, 400)
        self.btnPlay.text = "Play"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (500, 400)
        self.btnQuit.text = "Quit"
        
        self.sprites = [
            self.lblScore,
            self.lblInstructions,
            self.btnPlay,
            self.btnQuit
            ]

    def process(self):
        if self.btnPlay.clicked:
            self.status = "play"
            self.stop()
        if self.btnQuit.clicked:
            self.status = "quit"
            self.stop()

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ball.png")
        self.setSize(40, 40)
        self.minSpeed = 2
        self.maxSpeed = 6
        self.reset()
        
    def reset(self):
        
        self.y = 20
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class DjMoore(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Djmoore.png")
        self.setSize(100, 100)
        self.position = (320, 400)
        self.moveSpeed = 8
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Your Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)
        
 
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("field.png")
        
  
        self.score = 0
       
        
        self.sndCoin = simpleGE.Sound("success-1.mp3")
        self.numCoins = 10
       
     

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30

        
        self.DjMoore = DjMoore(self)
        
        self.coins = []
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
            
        self.lblScore = LblScore()
        self.lblTime = LblTime()
            
        self.sprites = [self.DjMoore, 
                        self.coins, 
                        self.lblScore, 
                        self.lblTime]            
                    
    def process(self):
        for coin in self.coins:        
            if coin.collidesWith(self.DjMoore):
                   coin.reset()
                   self.score += 1
                   self.lblScore.text = f"Score: {self.score}"
                   
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
              print(f"Final Score: {self.score}")
              self.stop()
                   
   
def main():

    keepGoing = True
    score = 0
    
    while keepGoing:
        intro = Intro(score)
        intro.start()
        
        if intro.status == "quit":
            keepGoing = False
        else:
            game = Game()
            game.start()
            score = game.score

if __name__ == "__main__":
    main()
    
    
    
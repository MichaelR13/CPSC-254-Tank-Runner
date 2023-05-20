#!/usr/bin/env python3
import pygame
import main

def testTank():
    def testTankImages():
        tank = main.Tank()
        assert tank.image in main.RUNNING
    
        tank.duck()
        assert tank.image in main.DUCKING
    
        tank.jump()
        assert tank.image == main.JUMPING

    def testTankJump():
        tank = main.Tank()
        tank.update({pygame.K_UP: True})
        assert tank.tankJump
        assert not tank.tankDuck
        assert not tank.tankRun

    testTankImages()
    testTankJump()

if __name__ == "__main__":
    testTank()

import pygame
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(x=100, y=100)

    def update(self):
        self.player.update()
        self.player.draw(self.screen)

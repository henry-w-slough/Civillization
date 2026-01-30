import include.GameObject as GameObject
import pygame


class Cursor(GameObject.GameObject):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group):
        super().__init__(width, height, "", *groups)
    
    def update(self):
        self.rect.x, self.rect.y = pygame.mouse.get_pos()
import pygame
import include.GameObject as GameObject
import math


class UIElement(GameObject.GameObject):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group):
        super().__init__(width, height, None, *groups)

        self.enabled = True

    def set_pos(self, x:int, y:int) -> None:
        self.rect.x = x
        self.rect.y = y

    def set_color(self, color:tuple) -> None:
        self.texture.color_fill(color)

    def set_enabled(self, enable:bool) -> None:
        self.enabled = enabled

    def add_text(self, text):
        text_image = pygame.Surface((self.rect.width, self.rect.height))

        font_size = math.isqrt((self.rect.width * self.rect.height) // len(text))
        font = pygame.font.Font("ByteBounce.ttf", font_size)

        text = font.render(text)
   
        
        
        








        
    
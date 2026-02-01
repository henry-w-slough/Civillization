import pygame
import include.Engine.GameObject as GameObject
import math

pygame.init()

class UIElement(GameObject.GameObject):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group):
        super().__init__(width, height, "", *groups)

        self.color:tuple = (0, 0, 0)

    def set_pos(self, x:int, y:int) -> None:
        self.rect.x = x
        self.rect.y = y

    def set_color(self, color:tuple) -> None:
        self.texture.color_fill(color)
        self.color = color

    def add_text(self, text: str, text_color: tuple) -> None:
        font_size = min(self.rect.width, self.rect.height) // 2
        font = pygame.font.Font("assets/ByteBounce.ttf", font_size)
        
        # Adjust font size until text fits
        while font_size > 1:
            text_image = font.render(text, False, text_color, self.color)
            if text_image.get_width() <= self.rect.width * 0.9 and text_image.get_height() <= self.rect.height * 0.9:
                break
            font_size -= 1
            font = pygame.font.Font("assets/ByteBounce.ttf", font_size)
    
        # Center the text
        x = (self.rect.width - text_image.get_width()) // 2
        y = (self.rect.height - text_image.get_height()) // 2
        self.image.blit(text_image, (x, y))
   
        
        
        








        
    
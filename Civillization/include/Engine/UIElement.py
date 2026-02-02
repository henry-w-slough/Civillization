import pygame
import include.Engine.GameObject as GameObject

pygame.init()

class UIElement(GameObject.GameObject):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group):
        super().__init__(width, height, "", *groups)

    def set_text(self, text: str, text_color: tuple) -> None:

        #temporary surface to act as image placeholder
        temp = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        temp.blit(self.image, (0, 0))
        temp.fill((255, 255, 255, self.alpha), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Find proper font size
        font_size = min(self.rect.width, self.rect.height) // 2
        font = pygame.font.Font("assets/ByteBounce.ttf", font_size)
        text_image = font.render(text, False, text_color)
        
        while font_size > 1 and (text_image.get_width() > self.rect.width * 0.9 or text_image.get_height() > self.rect.height * 0.9):
            font_size -= 1
            font = pygame.font.Font("assets/ByteBounce.ttf", font_size)
            text_image = font.render(text, False, text_color)
        
        # Center and blit opaque text
        x = (self.rect.width - text_image.get_width()) // 2
        y = (self.rect.height - text_image.get_height()) // 2

        temp.blit(text_image, (x, y))
        self.image = temp
   
        
        
        








        
    
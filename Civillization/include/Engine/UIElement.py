import pygame
import include.Engine.GameObject as GameObject

pygame.init()

class UIElement(GameObject.GameObject):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group):
        super().__init__(width, height, "", *groups)

    def set_text(self, text: str, text_color: tuple) -> None:

        #temp surface to act as self.image placeholder
        temp = self.texture.set_texture(self.texture.img_path)
        
        # Find proper font size
        font_size = min(self.rect.width, self.rect.height) // 2
        font = pygame.font.Font("assets/ByteBounce.ttf", font_size)
        text_image = font.render(text, False, text_color)
        
        #iterates until the text fits the given width/height
        while font_size > 1 and (text_image.get_width() > self.rect.width * 0.9 or text_image.get_height() > self.rect.height * 0.9):
            font_size -= 1
            font = pygame.font.Font("assets/ByteBounce.ttf", font_size)
            text_image = font.render(text, False, text_color)
        
        #centering text
        x = (self.rect.width - text_image.get_width()) // 2
        y = (self.rect.height - text_image.get_height()) // 2

        temp.blit(text_image, (x, y))
        self.image = temp
   
        
        
        








        
    
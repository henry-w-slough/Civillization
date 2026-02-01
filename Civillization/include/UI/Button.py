import include.Engine.UIElement as UIElement
import pygame




class Button(UIElement.UIElement):
    def __init__(self, width:int, height:int, *groups:pygame.sprite.Group):
        super().__init__(width, height, *groups)

    def is_hover(self, cursor) -> bool:
        if cursor.rect.right >= self.rect.left and cursor.rect.right <= self.rect.right:
            if cursor.rect.bottom >= self.rect.top and cursor.rect.top <= self.rect.bottom:
                return True
        return False
    



        

   

import pygame

class Texture():
    def __init__(self, img_path:str, width:int, height:int):

        if img_path != "":
            self.texture = pygame.image.load(img_path)
            self.texture = pygame.transform.scale(self.texture, (width, height))
        else:
            self.texture = pygame.Surface((width, height))
        
        self.width = width
        self.height = height

      
    def get_surface(self) -> pygame.Surface:
        return self.texture
    

    def resize(self, width:int, height:int) -> None:
        self.texture = pygame.transform.scale(self.texture, (width, height))
        width = width
        height = height


    def color_fill(self, color:tuple) -> None:
        self.texture.fill(color)



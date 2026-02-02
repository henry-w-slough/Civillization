import pygame

class Texture():
    def __init__(self, img_path:str, width:int, height:int):

        if img_path != "":
            try:
                self.texture = pygame.image.load(img_path)
            except pygame.error:
                self.texture = pygame.transform.scale(self.texture, (width, height))
        else:
            self.texture = pygame.Surface((width, height), pygame.SRCALPHA)

    def set_texture_background(self, color:tuple, alpha:int=255) -> pygame.Surface:
        self.texture.fill(color)
        self.texture.set_alpha(alpha)
        return self.texture

    def set_texture_size(self, width:int, height:int) -> pygame.Surface:
        self.texture = pygame.transform.scale(self.texture, (width, height))
        return self.texture



import pygame

class Texture():
    def __init__(self, img_path:str, width:int, height:int):

        self.color:tuple = (0, 0, 0)
        self.alpha = 255

        self.img_path = img_path
    
        try:
            self.texture = pygame.image.load(img_path)
        except FileNotFoundError:
            self.texture = pygame.Surface((width, height), pygame.SRCALPHA)
            print(f"ERROR: TEXTURE: Image path not found: '{img_path}'")

    def set_texture_color(self, color:tuple, alpha:int) -> pygame.Surface:
        self.texture.fill((*self.color, alpha))
        self.color = color
        self.alpha = alpha
        return self.texture

    def set_texture(self, img_path:str) -> pygame.Surface:
        try:
            w, h = self.texture.get_width(), self.texture.get_height()
            #setting the texture with old size and new img
            self.texture = pygame.image.load(img_path)
            self.texture = pygame.transform.scale(self.texture, (w, h))
        except FileNotFoundError:
            #error checking for invalid path gives a colored img
            self.texture = pygame.Surface((self.texture.get_width(), self.texture.get_height()), pygame.SRCALPHA)
            self.texture.fill((*self.color, self.alpha))
            print(f"ERROR: TEXTURE: Image path not found: '{img_path}'")
        return self.texture

    def set_texture_size(self, width:int, height:int) -> pygame.Surface:
        #sets the size of the texture then returns for self.image update
        self.texture = pygame.transform.scale(self.texture, (width, height))
        return self.texture



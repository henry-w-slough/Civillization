import pygame
import include.Engine.Texture as Texture



class GameObject(pygame.sprite.Sprite):

    def __init__(self, width:int, height:int, img_path:str, *groups:pygame.sprite.Group):
        super().__init__(*groups)

        self.texture = Texture.Texture(img_path, width, height)
        self.image = self.texture.set_texture_size(width, height)
        self.rect = self.image.get_rect()

        self.color:tuple = (0, 0, 0)
        self.alpha = 255

    def set_size(self, width:int, height:int):
        #resize sets the texture's size and returns the surface
        self.image = self.texture.set_texture_size(width, height)
        self.rect = self.image.get_rect()

    def set_pos(self, x:int, y:int):
        self.rect.x = x
        self.rect.y = y

    def set_background(self, color:tuple, alpha:int=255):
        self.image = self.texture.set_texture_background(color, alpha)
        self.alpha = alpha
        self.color = color

        








import pygame
import include.Engine.Texture as Texture



class GameObject(pygame.sprite.Sprite):

    def __init__(self, width:int, height:int, img_path:str, *groups:pygame.sprite.Group):
        super().__init__(*groups)

        self.texture = Texture.Texture(img_path, width, height)
        self.image = self.texture.set_texture_size(width, height)
        self.rect = self.image.get_rect()

    def set_size(self, width:int, height:int) -> None:
        self.image = self.texture.set_texture_size(width, height)
        self.rect = self.image.get_rect()

    def set_pos(self, x:int, y:int) -> None:
        self.rect.x = x
        self.rect.y = y

    def set_image(self, img_path:str) -> None:
        self.image = self.texture.set_texture(img_path)

    def set_color(self, color:tuple, alpha:int):
        self.image = self.texture.set_texture_color(color, alpha)
        

        








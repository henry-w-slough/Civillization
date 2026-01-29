import pygame
import include.Texture as Texture



class GameObject(pygame.sprite.Sprite):

    def __init__(self, width:int, height:int, img_path:str, *groups:pygame.sprite.Group):
        super().__init__(*groups)

        self.texture = Texture.Texture(img_path, width, height)
        self.image = self.texture.get_surface()
        self.rect = self.image.get_rect()

    def update(self):
        self.image.blit(self.texture.texture, (0, 0))

    
    def scale(self, width, height) -> None:
        self.texture.resize(width, height) 
        self.image = self.texture.get_surface()
        self.rect = self.image.get_rect()


    def translate(self, x:int, y:int) -> None:
        self.rect.x += x
        self.rect.y += y








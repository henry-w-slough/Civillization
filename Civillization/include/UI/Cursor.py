import include.Engine.GameObject as GameObject
import include.Engine.Screen as Screen
import pygame


class Cursor(GameObject.GameObject):
    def __init__(self, width:int, height:int, screen:Screen.Screen, *groups:pygame.sprite.Group):
        super().__init__(width, height, "", *groups)

        self.image.set_alpha(100)
        self.image.fill((255, 255, 255))

        self.screen_ref = screen
    
    def update(self) -> None:
        mouse_pos = pygame.mouse.get_pos()

        for tile in self.screen_ref.layers["tiles"]:
            if tile.rect.collidepoint(mouse_pos):
                self.rect.topleft = tile.rect.topleft
                break


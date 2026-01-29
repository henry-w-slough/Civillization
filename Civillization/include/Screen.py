import pygame
import include.Texture as Texture
import include.GameObject as GameObject

class Screen():

    def __init__(self, width:int, height:int):
        
        self.screen = pygame.display.set_mode((width, height))

        self.width = width
        self.height = height

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.layers = {
            "tiles": pygame.sprite.Group(),
            "sprites": pygame.sprite.Group(),
            "ui": pygame.sprite.Group(),
            "cursor": pygame.sprite.Group()
        }


    def update(self):

        self.screen.fill((255, 0, 255))

        for l in self.layers.values():
            l.update()
            l.draw(self.screen)
        
        pygame.display.flip()
        self.clock.tick(self.fps)
    

                    


            
            

        
import pygame
import include.Engine.Texture as Texture
import include.Engine.GameObject as GameObject

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
            "ui": pygame.sprite.Group()
        }

        

    def update(self) -> None:

        self.screen.fill((255, 0, 255))

        for l in self.layers.values():
            l.update()
            l.draw(self.screen)
        
        pygame.display.flip()
        self.clock.tick(self.fps)
    

                    


            
            

        
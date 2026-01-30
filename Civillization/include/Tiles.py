import pygame
import include.Texture as Texture
import include.GameObject as GameObject


class Tile(GameObject.GameObject):
    def __init__(self, img_path:str, x:int, y:int, width:int, height:int, *groups):
        super().__init__(width, height, img_path, *groups)

        self.rect.width = width
        self.rect.height = height

        self.rect.x = x
        self.rect.y = y


class Grass(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("", x, y, width, height, *groups)

        self.texture.color_fill((57, 89, 54))


class Stone(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("", x, y, width, height, *groups)

        self.texture.color_fill((52, 54, 56))
        

class Water(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("", x, y, width, height, *groups)
       
        self.texture.color_fill((24, 48, 22))


class Tree(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("", x, y, width, height, *groups)

        self.texture.color_fill((24, 48, 22))




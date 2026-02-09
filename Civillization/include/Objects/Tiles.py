import include.Engine.GameObject as GameObject


class Tile(GameObject.GameObject):
    def __init__(self, img_path:str, x:int, y:int, width:int, height:int, *groups):
        super().__init__(width, height, img_path, *groups)

        self.rect.width = width
        self.rect.height = height

        self.rect.x = x
        self.rect.y = y


class Grass(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("assets/sprites/grass.png", x, y, width, height, *groups)


class Stone(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("assets/sprites/stone.png", x, y, width, height, *groups)
        

class Water(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("assets/sprites/water.png", x, y, width, height, *groups)
    

class Tree(Tile):
    def __init__(self, x, y, width, height, *groups):
        super().__init__("assets/sprites/tree.png", x, y, width, height, *groups)





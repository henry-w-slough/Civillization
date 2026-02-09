import pygame
import include.Objects.Tiles as Tiles
import random


class Generation():

    def __init__(self, width:int, height:int, tiles:int):

        self.width = width
        self.height = height

        self.tiles = tiles

        self.tile_width = self.width / tiles
        self.tile_height = self.height / tiles

    def generate_map(self, chance:int, map_group:pygame.sprite.Group, Tile):
        for x in range(self.tiles):
            for y in range(self.tiles):
                tile_chance = random.randrange(1, chance+1)

                if tile_chance == 1:
                    self.change_tile(x, y, map_group, Tile)

    def change_tile(self, x:int, y:int, tile_group:pygame.sprite.Group, Tile):

        for t in tile_group.sprites():
            if [t.rect.x, t.rect.y] == [x*self.tile_width, y*self.tile_height]:  # Changed to use tile_w/tile_h
                t.kill()
                break
        Tile(x*self.tile_width, y*self.tile_height, self.tile_width, self.tile_height, tile_group)
                
        









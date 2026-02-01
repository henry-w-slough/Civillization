import pygame
import include.GameObjects.Tiles as Tiles
import random


class Generation():

    def __init__(self, width:int, height:int, tiles:int):

        self.width = width
        self.height = height

        self.tiles = tiles

        self.tile_width = self.width // tiles
        self.tile_height = self.height // tiles

    def generate_map(self, chance:int, map_group:pygame.sprite.Group, Tile):
        for x in range(self.tiles):
            for y in range(self.tiles):
                tile_chance = random.randrange(1, chance)

                if tile_chance == 1:
                    self.change_tile(x, y, map_group, Tile)

    def change_tile(self, tile_row, tile_column, tile_group: pygame.sprite.Group, Tile):
        #checking to see if there is a tile at the pos and destroying it
        for t in tile_group.sprites():
            if [t.rect.x, t.rect.y] == [tile_row*self.tile_width, tile_column*self.tile_height]:
                t.kill()
                break
        Tile(tile_row*self.tile_width, tile_column*self.tile_height, self.tile_width, self.tile_height, tile_group)









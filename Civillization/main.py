import pygame
import include.Engine.Screen as Screen
import include.Engine.Generation as Generation
import include.GameObjects.Tiles as Tiles
import include.GameHandlers.UIHandler as UIHandler
import include.GameHandlers.Game as Game
import include.UI.Cursor as Cursor
import sys

screen = Screen.Screen(800, 800)

game = Game.Game()

generation = Generation.Generation(screen.width, screen.height, 32)

generation.generate_map(1, screen.layers["tiles"], Tiles.Grass)
generation.generate_map(4, screen.layers["tiles"], Tiles.Tree)
generation.generate_map(20, screen.layers["tiles"], Tiles.Stone)

cursor = Cursor.Cursor(generation.width//generation.tiles, generation.height//generation.tiles, screen, screen.layers["cursor"])

ui_handler = UIHandler.UIHandler(screen, game, cursor)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update()
    screen.update()
    ui_handler.update()


pygame.quit()
sys.exit()
    









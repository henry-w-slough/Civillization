import pygame
import include.Engine.Screen as Screen
import include.Engine.Generation as Generation
import include.Objects.Tiles as Tiles
import include.UI.Cursor as Cursor
import include.Handlers.UIHandler as UIHandler
import sys

screen = Screen.Screen(800, 800)

ui_handler = UIHandler.UIHandler(screen)

generation = Generation.Generation(screen.width, screen.height, 32)

generation.generate_map(1, screen.layers["tiles"], Tiles.Grass)
generation.generate_map(4, screen.layers["tiles"], Tiles.Tree)
generation.generate_map(20, screen.layers["tiles"], Tiles.Stone)

cursor = Cursor.Cursor(generation.width//generation.tiles, generation.height//generation.tiles, screen, screen.layers["cursor"])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ui_handler.update()
    screen.update()
    
    
pygame.quit()
sys.exit()
    









import pygame
import include.Engine.Screen as Screen
import include.Engine.Generation as Generation
import include.GameObjects.Tiles as Tiles
import include.GameHandlers.UIHandler as UIHandler

screen = Screen.Screen(800, 800)

generation = Generation.Generation(screen.width, screen.height, 32)

generation.generate_map(1, screen.layers["tiles"], Tiles.Grass)
generation.generate_map(4, screen.layers["tiles"], Tiles.Tree)
generation.generate_map(20, screen.layers["tiles"], Tiles.Stone)

ui_handler = UIHandler.UIHandler(screen)
ui_handler.start(generation, screen)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ui_handler.update()
    screen.update()
    









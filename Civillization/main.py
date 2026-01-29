import pygame
import include.Screen as Screen
import include.Generation as Generation
import include.Tiles as Tiles
import include.UIElement as UIElement
import include.Button as Button
import include.Cursor as Cursor


screen = Screen.Screen(800, 800)


generation = Generation.Generation(screen.width, screen.height, 16)


generation.generate_map(2, screen.layers["tiles"], Tiles.Grass)
generation.generate_map(5, screen.layers["tiles"], Tiles.Tree)
generation.generate_map(10, screen.layers["tiles"], Tiles.Stone)


button = Button.Button(128, 128, screen.layers["ui"])
button.set_color((255, 255, 255))


cursor = Cursor.Cursor(generation.tile_width, generation.tile_height, screen.layers["cursor"])


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.update()









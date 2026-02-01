import pygame
import include.Engine.Generation as Generation
import include.Engine.Screen as Screen
import include.UI.Button as Button
import include.UI.Cursor as Cursor



class UIHandler():
    def __init__(self, screen:Screen.Screen):
        
        self.layers = {
            "resources": pygame.sprite.Group(),
            "cursor": pygame.sprite.Group()
        }

        self.screen_ref = screen
        self.ui_enabled = False

        self.prev_keys = ""
    

    def start(self, generation:Generation.Generation, screen:Screen.Screen):
        Cursor.Cursor(generation.tile_width, generation.tile_height, screen, self.layers["cursor"])
        self.enable_layer("cursor")

        button = Button.Button(screen.width, generation.tile_height * 5, self.layers["resources"])
        button.set_pos(0, screen.height - button.rect.height)
        button.set_opacity(100)
        button.add_text("This is transparent text", (255, 255, 255))
        


    def update(self):
        keys = pygame.key.get_pressed()

        if keys != self.prev_keys:
            if keys[pygame.K_e]:
                self.ui_enabled = not self.ui_enabled

        self.prev_keys = keys

        if self.ui_enabled:
            for layer in self.layers:
                self.enable_layer(layer)
        else:
            for layer in self.layers:
                if layer == "cursor":
                    continue
                self.disable_layer(layer)


    def enable_layer(self, layer:str) -> None:
        for sprite in self.layers[layer].sprites():
            self.screen_ref.layers["ui"].add(sprite)


    def disable_layer(self, layer:str) -> None:
        for sprite in self.layers[layer].sprites():
            self.screen_ref.layers["ui"].remove(sprite)
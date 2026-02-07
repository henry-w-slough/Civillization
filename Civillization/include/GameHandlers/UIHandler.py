import pygame
import include.Engine.Generation as Generation
import include.Engine.Screen as Screen
import include.UI.Button as Button
import include.UI.Cursor as Cursor
import include.Engine.UIElement as UIElement
import include.GameHandlers.Game as Game
import random

clock = pygame.time.Clock()

class UIHandler():
    def __init__(self, screen:Screen.Screen, game:Game.Game, cursor:Cursor.Cursor):
        
        self.layers = {
            "background": pygame.sprite.Group(),
            "enabled": pygame.sprite.Group(),
            "assets": pygame.sprite.Group(),
            "stats": pygame.sprite.Group()
        }

        self.screen = screen
        self.cursor = cursor
        self.game = game

        self.ui_enabled = True

        self.prev_keys = ""

        self.ui_label = UIElement.UIElement(64, 64, self.layers["enabled"])
        self.ui_label.set_size(self.screen.width, self.screen.height//5)
        self.ui_label.set_pos(0, self.screen.height-self.ui_label.rect.height)
        self.ui_label.set_text("Hello")
        
        self.asset_tab = Button.Button(0, 0, self.layers["enabled"])
        self.asset_tab.set_size(self.screen.width//8, self.screen.height // 10)
        self.asset_tab.set_pos(0, self.ui_label.rect.y-self.asset_tab.rect.height)
        self.asset_tab.set_text("Assets")
        
        self.stats_tab = Button.Button(0, 0, self.layers["enabled"])
        self.stats_tab.set_size(self.asset_tab.rect.width, self.asset_tab.rect.height)
        self.stats_tab.set_pos(self.asset_tab.rect.x+self.stats_tab.rect.width, self.asset_tab.rect.y)
        self.stats_tab.set_text("Stats")

        self.fps_label = UIElement.UIElement(32, 32, self.layers["enabled"])
        self.fps_label.set_text(str(round(clock.get_fps(), 2)))

    def update(self):
        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed()
    
        self.prev_keys = keys


    def enable_layer(self, layer:pygame.sprite.Group):
        for sprite in layer:
            self.screen.layers["ui"].add(sprite)

    def disable_layer(self, layer:pygame.sprite.Group):
        for sprite in layer:
            if self.screen.layers["ui"].has(sprite):
                self.screen.layers["ui"].remove(sprite)

import include.Engine.Screen as Screen
import include.Engine.UIElement as UIElement
import include.UI.Button as Button
import pygame

class UIHandler():
    def __init__(self, screen:Screen.Screen) -> None:
        
        self.screen = screen

        self.layers = {
            "background": pygame.sprite.Group(),
            "assets": pygame.sprite.Group(),
        }

        self.enabled = pygame.sprite.Group()

        self.ui_visible = False

        self.prev_keys = ""
  
        self.assets_tab = Button.Button(128, 128, self.layers["assets"])      
        self.assets_tab.set_pos(screen.width // 2, screen.height // 2)
        self.assets_tab.set_size(screen.width, screen.height // 8)
   
    def update(self):
        keys = pygame.key.get_pressed()

        if self.prev_keys != keys and keys[pygame.K_e]:
            self.ui_visible = not self.ui_visible

        if self.ui_visible:
            self.enabled.add(*self.layers["assets"].sprites())
            self.screen.layers["ui"].add(*self.enabled.sprites())
            print(self.enabled.sprites())
        else:
            self.screen.layers["ui"].remove(*self.enabled.sprites())

        self.prev_keys = keys 






    

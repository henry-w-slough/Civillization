import pygame
import include.Engine.Generation as Generation
import include.Engine.Screen as Screen
import include.UI.Button as Button
import include.UI.Cursor as Cursor
import include.Engine.UIElement as UIElement



class UIHandler():
    def __init__(self, screen:Screen.Screen):
        
        self.layers = {
            "menus": pygame.sprite.Group(),
            "cursor": pygame.sprite.Group()
        }

        self.screen_ref = screen
        self.ui_enabled = False

        self.prev_keys = ""
        self.prev_buttons = ""

        self.cursor:Cursor.Cursor

        self.ui_label:UIElement.UIElement
        self.asset_tab:Button.Button
        self.stats_tab:Button.Button
    

    def start(self, generation:Generation.Generation, screen:Screen.Screen):
        self.cursor = Cursor.Cursor(generation.width//generation.tiles, generation.height//generation.tiles, screen, self.layers["cursor"])
        self.enable_layer("cursor")

        self.ui_label = UIElement.UIElement(screen.width, screen.height//4, self.layers["menus"])
        self.ui_label.set_color((100, 100, 100), 230)
        self.ui_label.set_text("This is the assets tab.", (255, 255, 255))
        self.ui_label.set_pos(0, screen.height-self.ui_label.rect.height)

        self.asset_tab = Button.Button(screen.width//7, screen.height//10, self.layers["menus"])
        self.asset_tab.set_color((100, 255, 255), 230)
        self.asset_tab.set_text("Assets", (255, 255, 255))
        self.asset_tab.set_pos(64, self.ui_label.rect.y-self.asset_tab.rect.height)

        self.stats_tab = Button.Button(screen.width//7, screen.height//10, self.layers["menus"])
        self.stats_tab.set_color((100, 255, 100), 230)
        self.stats_tab.set_text("Stats", (255, 255, 255))
        self.stats_tab.set_pos(self.asset_tab.rect.x+self.stats_tab.rect.width+64, self.ui_label.rect.y-self.asset_tab.rect.height)

    def update(self):
        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed()

        if keys != self.prev_keys:
            if keys[pygame.K_e]:
                self.ui_enabled = not self.ui_enabled

        if buttons != self.prev_buttons:
            if buttons[0]:
                if self.asset_tab.is_hover(self.cursor):
                    self.ui_label.set_text("This is the assets tab.", (255, 255, 255))
                if self.stats_tab.is_hover(self.cursor):
                    self.ui_label.set_text("This is the stats tab.", (255, 255, 255))


        self.prev_buttons = buttons
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
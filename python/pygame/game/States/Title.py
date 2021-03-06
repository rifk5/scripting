import pygame, os
from States.State import State
from States.Game import Game
from Button import Button

class Title(State):

    def __init__(self, app):
        State.__init__(self, app)
        self.loadAssets()
        self.start_button = Button(app.canvas, self.start_image, 0.6, self.app.screen_center[0]-180, self.app.screen_center[1]+50)
        self.exit_button = Button(app.canvas, self.exit_image, 0.6, self.app.screen_center[0]+40, self.app.screen_center[1]+50)
        self.keys = pygame.key.get_pressed()
    
    def loadAssets(self):
        self.start_image = pygame.image.load(os.path.join(self.app.button_dir, "start_btn.png")).convert_alpha()
        self.exit_image = pygame.image.load(os.path.join(self.app.button_dir, "exit_btn.png")).convert_alpha()
    
    def initGameState(self):
        game_state = Game(self.app)
        game_state.enterState()

    def update(self, dt):
        if (self.start_button.update()):
            self.initGameState()

        if (self.exit_button.update()):
            self.app.running = False
        
        if self.keys[pygame.K_RETURN]:
            self.initGameState()
            
    def render(self, display):
        display.fill((255, 255, 255))
        self.app.drawText(display, "Python Game 2022", self.app.color["ORANGE"], 
                          (self.app.screen_center[0], self.app.screen_center[1]),
                          False)
        self.start_button.render(display)
        self.exit_button.render(display)
        
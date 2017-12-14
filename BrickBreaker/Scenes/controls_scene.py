import pygame

from BrickBreaker.Scenes.scene import Scene
from BrickBreaker.Shared import *


class ControlsScene(Scene):

    def __init__(self, game):
        super().__init__(game)

    def render(self):

        self.clear_text()
        self.add_text("F1 - Use mouse for movement", x=500, y=200, size=60)
        self.add_text("F2 - Use keyboard for movement", x=500, y=280, size=60)
        self.add_text("F3 - Back to Main Menu", x=500, y=360, size=60)

        super().render()

    def handle_events(self, events):
        super().handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_game().change_scene(GameConstants.MAIN_MENU_SCENE)

                if event.key == pygame.K_F1:
                    self.get_game().get_pad().activate_mouse()

                if event.key == pygame.K_F2:
                    self.get_game().get_pad().activate_keyboard()

                if event.key == pygame.K_F3:
                    self.get_game().change_scene(GameConstants.MAIN_MENU_SCENE)

import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SQUARE_SIZE
from color import Color

class Screen(object):
    def __init__(self):

        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.square_size = SQUARE_SIZE

        self.font = pygame.font.Font('freesansbold.ttf', 64)

        self.clock = pygame.time.Clock()
        self.set_title()

    def fill_background(self, color=Color.BLACK):
        self.screen.fill(color)

    @staticmethod
    def set_title(title="Chess"):
        pygame.display.set_caption(title)

    @staticmethod
    def update():
        pygame.display.flip()

    def draw_win_screen(self, text):
        text = self.font.render(text, True, Color.GREEN, Color.BLUE)
        text_rect = text.get_rect()
        text_rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.screen.blit(text, text_rect)
import pygame

class Robot:
    """A rectangular robot that follows the user's mouse."""

    def __init__(self, width, height, color, line_width):
        self.rect = pygame.Rect((0, 0), (width, height))
        self.color = color
        self.line_width = line_width

    def update_position(self, mouse_coords):
        self.rect.center = mouse_coords
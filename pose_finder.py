import pygame

from constants import Constants


class PoseFinder:
    """The PoseFinder program."""

    def __init__(self):
        """Initialize necessary elements."""
        # Initialize pygame.
        pygame.init()

        # Create screen.
        self.screen = pygame.display.set_mode([Constants.SCREEN_WIDTH_PIXELS, Constants.SCREEN_HEIGHT_PIXELS])

        # Load image.
        self.field_drawing = pygame.image.load(Constants.FIELD_DRAWING_FILE_PATH)
        self.field_drawing.convert()

        # Center the field drawing on the screen.
        self.field_drawing_rect = self.field_drawing.get_rect()
        self.field_drawing_rect.center = self.screen.get_rect().center

    def run_game(self):
        """Run the game."""
        self.running = True
        while (self.running):
            self.check_events()
            self.draw_elements()

        # End the game.
        pygame.quit()

    def check_events(self):
        """Check user events."""
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_coords = event.pos
                field_pose = self.get_field_pose(mouse_coords)
                print(field_pose)

    def get_field_pose(self, mouse_coords):
        """Convert mouse coords to field pose."""
        pixel_x, pixel_y = mouse_coords
        pixel_y = Constants.SCREEN_HEIGHT_PIXELS - pixel_y

        field_x = pixel_x * Constants.WIDTH_METERS_PER_PIXEL
        field_y = pixel_y * Constants.HEIGHT_METERS_PER_PIXEL

        return (field_x, field_y)
    
    def draw_elements(self):
        # Fill background with white.
        self.screen.fill(Constants.BACKGROUND_COLOR)

        # Draw the field drawing.
        self.screen.blit(self.field_drawing, self.field_drawing_rect)

        # Flip to newly drawn screen.
        pygame.display.flip()


if (__name__ == '__main__'):
    pf = PoseFinder()
    pf.run_game()
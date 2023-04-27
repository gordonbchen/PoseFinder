import math
import pygame

from constants import Constants
from robot import Robot


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

        # Create robot instance.
        self.robot = Robot(
            width=Constants.ROBOT_WIDTH_PIXELS, height=Constants.ROBOT_HEIGHT_PIXELS,
            color=Constants.ROBOT_COLOR, line_width=Constants.ROBOT_LINE_WIDTH
        )

        # Distance mode.
        self.distance_mode = False
        self.start_pose = None

    def run_game(self):
        """Run the game."""
        self.running = True
        while (self.running):
            self.check_events()
            self.robot.update_position(pygame.mouse.get_pos())
            self.draw_elements()

        # End the game.
        pygame.quit()

    def check_events(self):
        """Check user events."""
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False
            elif (event.type == pygame.KEYDOWN):
                self.handle_keydown_events(event.key)
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                field_pose = self.get_field_pose(event.pos)
                print(f"\nPose: {field_pose}")

                if (self.distance_mode):
                    if (self.start_pose):
                        distance = self.calc_distance(self.start_pose, field_pose)
                        print(f"Distance: {distance}")
                        self.start_pose = None
                    else:
                        self.start_pose = field_pose

    def handle_keydown_events(self, key):
        """Handle keydown events."""
        if (key == pygame.K_ESCAPE):
            self.running = False
        elif (key == pygame.K_d):
            self.distance_mode = True
            print("\nDistance mode activated")
        elif (key == pygame.K_p):
            self.distance_mode = False
            print("\nPose mode activated")

    def get_field_pose(self, mouse_coords):
        """Convert mouse coords to field pose."""
        pixel_x, pixel_y = mouse_coords
        pixel_y = Constants.SCREEN_HEIGHT_PIXELS - pixel_y

        field_x = pixel_x * Constants.WIDTH_METERS_PER_PIXEL
        field_y = pixel_y * Constants.HEIGHT_METERS_PER_PIXEL

        return (field_x, field_y)
    
    def calc_distance(self, start_pose, end_pose):
        """Find the euclidean distance between 2 poses."""
        dx = start_pose[0] - end_pose[0]
        dy = start_pose[1] - end_pose[1]
        return math.sqrt(dx ** 2 + dy ** 2)

    def draw_elements(self):
        # Fill background with white.
        self.screen.fill(Constants.BACKGROUND_COLOR)

        # Draw the field drawing.
        self.screen.blit(self.field_drawing, self.field_drawing_rect)

        # Draw the robot.
        pygame.draw.rect(
            self.screen, color=self.robot.color,
            rect=self.robot.rect, width=self.robot.line_width
        )

        # Flip to newly drawn screen.
        pygame.display.flip()


if (__name__ == '__main__'):
    pf = PoseFinder()
    pf.run_game()
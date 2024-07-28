import pygame
import sys

def main():
    """
    Initialize Pygame and create a window with a bouncing ball.

    This script initializes Pygame, sets up a window of size 640x480, and creates a game loop that updates and renders a bouncing ball at 60 frames per second.

    Example:
        To run this script, simply execute it with Python. The window will appear and the ball will start bouncing. Close the window to exit the script.

    Returns:
        None
    """

    # Initialize Pygame
    pygame.init()

    # Set up some constants
    WIDTH, HEIGHT = 640, 480
    FPS = 60

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Set up some variables
    ball_radius = 30
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel = [3, 3]

    # Game loop
    running = True
    while running:
        # Keep the loop running at the right speed
        pygame.time.Clock().tick(FPS)

        # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > WIDTH:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > HEIGHT:
            ball_vel[1] = -ball_vel[1]

        # Draw / Render
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 255, 255), ball_pos, ball_radius)

        # After drawing everything, flip the display
        pygame.display.flip()

    # Done! Close the window when done
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
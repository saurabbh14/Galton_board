import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ROWS = 10
PEG_RADIUS = 5
PEG_SPACING = 50
BALL_RADIUS = 5
BIN_WIDTH = PEG_SPACING
MARGIN = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galton Board")
clock = pygame.time.Clock()

# Calculate peg positions
def generate_pegs(rows):
    pegs = []
    for row in range(rows):
        y = MARGIN + row * PEG_SPACING
        #offset = PEG_SPACING / 2 if row % 2 == 1 else 0
        for col in range(row + 1):
            x = WIDTH // 2 + (col - row / 2) * PEG_SPACING #+ offset*0
            pegs.append((x, y))
    return pegs

pegs = generate_pegs(ROWS)
print(pegs)

def draw_board():
    screen.fill((0, 0, 0))  # black background

    # Draw pegs
    for peg in pegs:
        pygame.draw.circle(screen, (255, 255, 255), peg, PEG_RADIUS)

    # Draw bins
    bin_y = MARGIN + ROWS * PEG_SPACING
    for i in range(ROWS + 1):
        x = WIDTH // 2 + (i - ROWS / 2) * PEG_SPACING
        pygame.draw.rect(screen, (0, 100, 200), (x - BIN_WIDTH // 2, bin_y, BIN_WIDTH, HEIGHT - bin_y))

    pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_board()
    clock.tick(60)
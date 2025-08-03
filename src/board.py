import pygame
from config import WIDTH, PEG_SPACING,MARGIN

# Pegs
def generate_pegs(rows):
    pegs = []
    for row in range(rows):
        y = MARGIN + row * PEG_SPACING
        for col in range(row + 1):
            x = WIDTH // 2 + (col - row / 2) * PEG_SPACING
            pegs.append((x, y))
    return pegs

def draw_pegs(screen, pegs, radius=5):
    for peg in pegs:
        pygame.draw.circle(screen, (255, 255, 255), peg, radius)

def draw_bins(screen, bin_centers, bin_y, bin_width, hist_height):
    for center_x in bin_centers:
        pygame.draw.rect(screen, (0, 100, 200),
            (center_x - bin_width // 2, bin_y, bin_width, (screen.get_height() - bin_y - hist_height)))


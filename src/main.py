import pygame
import sys
from config import *
from setup import *
from count import *
from board import generate_pegs, draw_pegs, draw_bins
from hist import draw_histogram
from ball import Ball
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galton Board")
clock = pygame.time.Clock()

pegs = generate_pegs(ROWS)

balls = []
frame_counter = 0
counts = 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    frame_counter += 1
    if frame_counter % BALL_DELAY == 0:
        balls.append(Ball())

    for ball in balls:
        prev_landed = ball.landed
        ball.update()
        if not prev_landed and ball.landed:
            counts += 1

    # Draw
    screen.fill((0, 0, 0))
    draw_pegs(screen, pegs, PEG_RADIUS)
    draw_bins(screen, bin_centers, bin_y, BIN_WIDTH, HIST_HEIGHT)
    for ball in balls:
        ball.draw(screen)
    show_count(screen,counts, x_c, y_c)
    draw_histogram(screen, bin_centers, bin_counts, BIN_WIDTH, HIST_HEIGHT)

    pygame.display.flip()
    clock.tick(50)
import pygame
import sys
#Total count
x_c = 10
y_c = 10

def show_count(screen, counts, x, y):
    font = pygame.font.Font("freesansbold.ttf", 30)
    count = font.render("Count: " + str(counts), True, (255, 255, 255))
    screen.blit(count, (x, y))
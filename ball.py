import pygame
import random
import math
from config import WIDTH, ROWS, PEG_SPACING, MARGIN, BIN_WIDTH, BALL_SPEED, BALL_RADIUS
from setup import *



# Ball class
class Ball:
    def __init__(self):
        self.path = self.generate_path()
        self.current_step = 0
        self.pos = [WIDTH // 2, MARGIN - 20]
        self.landed = False

    def generate_path(self):
        x = WIDTH // 2
        path = []
        for row in range(ROWS):
            direction = random.choice([-1, 1])
            x += direction * PEG_SPACING / 2
            y = MARGIN + row * PEG_SPACING
            path.append((x, y))
        path.append((x, bin_y))
        return path

    def update(self):
        if self.landed:
            return

        if self.current_step < len(self.path):
            target = self.path[self.current_step]
            dx = target[0] - self.pos[0]
            dy = target[1] - self.pos[1]
            dist = math.hypot(dx, dy)
            if dist < BALL_SPEED:
                self.pos = list(target)
                self.current_step += 1
            else:
                self.pos[0] += BALL_SPEED * dx / dist
                self.pos[1] += BALL_SPEED * dy / dist

        if self.current_step == len(self.path):
            # Determine closest bin
            closest_bin = min(
                range(len(bin_centers)),
                key=lambda i: abs(self.pos[0] - bin_centers[i])
            )
            bin_counts[closest_bin] += 1
            self.landed = True

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.pos[0]), int(self.pos[1])), BALL_RADIUS)
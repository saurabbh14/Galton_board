import pygame
import sys
import asyncio
from config import *
from setup import *
from count import *
from board import generate_pegs, draw_pegs, draw_bins
from hist import draw_histogram
from ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Galton Board")
        self.clock = pygame.time.Clock()

        self.pegs = generate_pegs(ROWS)

        self.balls = []
        self.frame_counter = 0
        self.counts = 0

    async def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.frame_counter += 1
            if self.frame_counter % BALL_DELAY == 0:
                self.balls.append(Ball())

            for ball in self.balls:
                prev_landed = ball.landed
                ball.update()
                if not prev_landed and ball.landed:
                    self.counts += 1

            self.draw()
            self.clock.tick(50)
            # Required for Pygbag
            await asyncio.sleep(0)

    def draw(self):# Draw
        self.screen.fill((0, 0, 0))
        draw_pegs(self.screen, self.pegs, PEG_RADIUS)
        draw_bins(self.screen, bin_centers, bin_y, BIN_WIDTH, HIST_HEIGHT)
        for ball in self.balls:
            ball.draw(self.screen)
        show_count(self.screen, self.counts, x_c, y_c)
        draw_histogram(self.screen, bin_centers, bin_counts, BIN_WIDTH, HIST_HEIGHT)
        pygame.display.flip()


# Main loop
async def main():
    game = Game()
    await game.game_loop()
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())

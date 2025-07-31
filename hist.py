import pygame

def draw_histogram(screen, bin_centers, bin_counts, bin_width, hist_height):
    max_count = max(bin_counts) if max(bin_counts) > 0 else 1
    screen_height = screen.get_height()

    for i, count in enumerate(bin_counts):
        x = bin_centers[i]
        bar_height = int((count / max_count) * hist_height)
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (x - bin_width // 2, screen_height - bar_height, bin_width, bar_height)
        )
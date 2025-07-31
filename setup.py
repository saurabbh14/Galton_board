from config import MARGIN, ROWS, PEG_SPACING, WIDTH

# Bin centers
bin_y = MARGIN + ROWS * PEG_SPACING
bin_centers = [
    WIDTH // 2 + (i - ROWS / 2) * PEG_SPACING
    for i in range(ROWS + 1)
]
bin_counts = [0] * (ROWS + 1)
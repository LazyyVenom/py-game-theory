import pygame
import sys

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FONT_SIZE = 24
LINE_SPACING = 5
SCROLL_SPEED = 20

class ScrollableText:
    def __init__(self, text, x, y, width, height, font_size):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.lines = self.render_text()
        self.scroll_pos = 0

    def render_text(self):
        lines = []
        words = self.text.split()
        line = ''
        for word in words:
            test_line = line + word + ' '
            if self.font.size(test_line)[0] < self.width:
                line = test_line
            else:
                lines.append(line)
                line = word + ' '
        lines.append(line)
        return lines

    def draw(self, surface):
        y_offset = self.y
        for line in self.lines[self.scroll_pos:]:
            text_surface = self.font.render(line, True, TEXT_COLOR)
            surface.blit(text_surface, (self.x, y_offset))
            y_offset += self.font_size + LINE_SPACING

    def scroll_up(self):
        if self.scroll_pos > 0:
            self.scroll_pos -= 1

    def scroll_down(self):
        if self.scroll_pos < len(self.lines) - self.height // (self.font_size + LINE_SPACING):
            self.scroll_pos += 1

# Create a Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Scrollable Text')

# Sample text
theory_text = """
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
This is a sample theory text. You can replace it with your own content.
It should be long enough to require scrolling. You can use paragraphs,
bullet points, or any other formatting you want.
"""

# Create scrollable text object
scrollable_text = ScrollableText(theory_text, 50, 50, WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100, FONT_SIZE)

# Main loop
while True:
    window.fill(BACKGROUND_COLOR)
    scrollable_text.draw(window)
    pygame.display.update()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scrollable_text.scroll_up()
            elif event.key == pygame.K_DOWN:
                scrollable_text.scroll_down()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                scrollable_text.scroll_up()
            elif event.button == 5:  # Scroll down
                scrollable_text.scroll_down()

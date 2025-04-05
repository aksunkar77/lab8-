#in this file i will do paint in pygame 
#and there will be rect, circle erase (balluur)etc
#and have  4 colors
import pygame
import sys

pygame.init()

# Screen 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK

#  background
screen.fill(WHITE)

#  options
DRAW_RECT = 'rect'
DRAW_CIRCLE = 'circle'
DRAW_FREE = 'free'
ERASER = 'eraser'
current_tool = DRAW_FREE

# Drawing state
start_pos = None
radius = 20

# Font
font = pygame.font.SysFont(None, 24)

def draw_ui():
    pygame.draw.rect(screen, RED, (10, 10, 40, 40))
    pygame.draw.rect(screen, GREEN, (60, 10, 40, 40))
    pygame.draw.rect(screen, BLUE, (110, 10, 40, 40))
    pygame.draw.rect(screen, BLACK, (160, 10, 40, 40))
    pygame.draw.rect(screen, WHITE, (210, 10, 40, 40))
    pygame.draw.rect(screen, (200, 200, 200), (260, 10, 80, 40))  # Rect
    pygame.draw.rect(screen, (200, 200, 200), (350, 10, 80, 40))  # Circle
    pygame.draw.rect(screen, (200, 200, 200), (440, 10, 80, 40))  # Free
    pygame.draw.rect(screen, (200, 200, 200), (530, 10, 80, 40))  # Eraser

    screen.blit(font.render("Rect", True, BLACK), (270, 20))
    screen.blit(font.render("Circle", True, BLACK), (360, 20))
    screen.blit(font.render("Free", True, BLACK), (450, 20))
    screen.blit(font.render("Eraser", True, BLACK), (540, 20))

def get_color(pos):
    x, y = pos
    if 10 <= x <= 50 and 10 <= y <= 50:
        return RED
    elif 60 <= x <= 100 and 10 <= y <= 50:
        return GREEN
    elif 110 <= x <= 150 and 10 <= y <= 50:
        return BLUE
    elif 160 <= x <= 200 and 10 <= y <= 50:
        return BLACK
    elif 210 <= x <= 250 and 10 <= y <= 50:
        return WHITE
    return None

def get_tool(pos):
    x, y = pos
    if 260 <= x <= 340 and 10 <= y <= 50:
        return DRAW_RECT
    elif 350 <= x <= 430 and 10 <= y <= 50:
        return DRAW_CIRCLE
    elif 440 <= x <= 520 and 10 <= y <= 50:
        return DRAW_FREE
    elif 530 <= x <= 610 and 10 <= y <= 50:
        return ERASER
    return None

running = True
mouse_down = False

draw_ui()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            start_pos = pygame.mouse.get_pos()
            pos = pygame.mouse.get_pos()
            color = get_color(pos)
            tool = get_tool(pos)
            if color:
                current_color = color
            if tool:
                current_tool = tool

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            end_pos = pygame.mouse.get_pos()
            if current_tool == DRAW_RECT and start_pos:
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
            elif current_tool == DRAW_CIRCLE and start_pos:
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                radius = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                pygame.draw.circle(screen, current_color, center, radius, 2)

        elif event.type == pygame.MOUSEMOTION and mouse_down:
            if current_tool == DRAW_FREE:
                pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), 3)
            elif current_tool == ERASER:
                pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 10)

    draw_ui()
    pygame.display.flip()

pygame.quit()
sys.exit()
#code worked succesfully

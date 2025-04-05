import pygame
import random
import sys


pygame.init()

# Screen 
BLOCK_SIZE = 20
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (BLOCK_SIZE, 0)

# Wall blocks (customize this to make more complex levels)
wall_blocks = [(300, 200), (320, 200), (340, 200)]

# Score and level
score = 0
level = 1
speed = 10

# Generate valid food

def generate_food(snake_body, wall_blocks):
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_pos = (x, y)
        if food_pos not in snake_body and food_pos not in wall_blocks:
            return food_pos

food = generate_food(snake, wall_blocks)


def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def game_loop():
    global snake, snake_dir, food, score, level, speed

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Arrow key input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                    snake_dir = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                    snake_dir = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                    snake_dir = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                    snake_dir = (BLOCK_SIZE, 0)

        # Move 
        head_x, head_y = snake[0]
        new_head = (head_x + snake_dir[0], head_y + snake_dir[1])

        
        if new_head in wall_blocks or new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            running = False

        snake.insert(0, new_head)

        # Food 
        if new_head == food:
            score += 1
            food = generate_food(snake, wall_blocks)

            # Level up every 4 points
            if score % 4 == 0:
                level += 1
                speed += 2  # increase speed
        else:
            snake.pop()  # keep snake size if not eating

        # Draw snake
        for block in snake:
            pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

        # Draw food
        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

        # Draw wall
        for wall in wall_blocks:
            pygame.draw.rect(screen, BLUE, (*wall, BLOCK_SIZE, BLOCK_SIZE))

        # Draw score and level
        draw_text(f"Score: {score}", WHITE, 10, 10)
        draw_text(f"Level: {level}", WHITE, 10, 40)

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    sys.exit()



game_loop()

#finally this code worked succesfully 

import pygame
import random


# Initialize PyGame
pygame.init()


# --- Constants (use tuples for colors) ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 180, 50)
BLUE = (50, 100, 220)
YELLOW = (240, 200, 50)
COLORS = [RED, GREEN, BLUE, YELLOW]


# --- Game State (use a dictionary) ---
game_state = {
 "score": 0,
 "lives": 3,
 "level": 1,
 "game_over": False,
 "fall_speed": 3
}


# --- Player (basket) settings ---
basket_width = 120
basket_height = 20
basket_x = SCREEN_WIDTH // 2 - basket_width // 2
basket_y = SCREEN_HEIGHT - 50
basket_speed = 8


# --- Falling objects (use a list of dictionaries) ---
falling_objects = []


# --- Screen setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)


def create_object():
    return {
        "x": random.randint(0, SCREEN_WIDTH - 20),
        "y": 0,
        "color": random.choice(COLORS),
        "size": 20
    }


def reset_game():
    global basket_x, falling_objects
    game_state["score"] = 0
    game_state["lives"] = 3
    game_state["level"] = 1
    game_state["game_over"] = False
    game_state["fall_speed"] = 3
    basket_x = SCREEN_WIDTH // 2 - basket_width // 2
    falling_objects = []

frame_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state["game_over"]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                elif event.key == pygame.K_q:
                    running = False


    if not game_state["game_over"]:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
            basket_x += basket_speed


        frame_count += 1
        if frame_count % 30 == 0:
            falling_objects.append(create_object())


        new_objects = []
        for obj in falling_objects:
            obj["y"] += game_state["fall_speed"] # Move down

            if (obj["y"] + obj["size"] >= basket_y and 
                basket_x <= obj["x"] <= basket_x + basket_width):
                game_state["score"] += 1
                

                if game_state["score"] % 5 == 0:
                    game_state["fall_speed"] += 1
                    game_state["level"] += 1
            

            elif obj["y"] > SCREEN_HEIGHT:
                game_state["lives"] -= 1
                if game_state["lives"] <= 0:
                    game_state["game_over"] = True
            

            else:
                new_objects.append(obj)
        
        falling_objects = new_objects

    screen.fill(BLACK)
    

    pygame.draw.rect(screen, WHITE, (basket_x, basket_y, basket_width, basket_height))
    

    for obj in falling_objects:
        pygame.draw.circle(screen, obj["color"], (obj["x"], obj["y"]), obj["size"] // 2)

  
    score_surf = font.render(f"Score: {game_state['score']}  Lives: {game_state['lives']}  Level: {game_state['level']}", True, WHITE)
    screen.blit(score_surf, (10, 10))


    if game_state["game_over"]:
        over_surf = font.render(f"GAME OVER! Final Score: {game_state['score']}", True, RED)
        retry_surf = font.render("Press R to Restart or Q to Quit", True, WHITE)
        screen.blit(over_surf, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20))
        screen.blit(retry_surf, (SCREEN_WIDTH // 2 - 170, SCREEN_HEIGHT // 2 + 20))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
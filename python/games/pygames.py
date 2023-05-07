import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the colors used in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the font used for displaying text
FONT = pygame.font.Font(None, 50)

# Set the title of the game window
pygame.display.set_caption("Pygame Game")

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up the game clock
clock = pygame.time.Clock()

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed = 5
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Define the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed = random.randrange(1, 4)
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT + 10:
            self.rect.x = random.randrange(WINDOW_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed = random.randrange(1, 4)

# Define the game function
def game():
    # Create the player sprite
    player = Player()
    
    # Create the enemy sprite group
    enemies = pygame.sprite.Group()
    for i in range(10):
        enemy = Enemy()
        enemies.add(enemy)
        
    # Set up the score
    score = 0
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.topright = (WINDOW_WIDTH - 10, 10)
    
    # Set up the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update the sprites
        player.update()
        enemies.update()
        
        # Check for collisions between the player and enemies
        if pygame.sprite.spritecollide(player, enemies, True):
            score += 1
            enemy = Enemy()
            enemies.add(enemy)
            
        # Draw the sprites
        window.fill(BLACK)
        window.blit(score_text, score_rect)
        #player.draw(window) working 
        enemies.draw(window)
        pygame.display.flip()
        
        # Update the score

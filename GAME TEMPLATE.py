import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("GAME NAME")

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. assign character position/location
    # 4. collision
    # 5. draw on screen
    pygame. display.update()
pygame.quit()
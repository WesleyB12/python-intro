import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Create a surface with per-pixel alpha
circle_surface = pygame.Surface((100, 100), pygame.SRCALPHA)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # Background color

    # Blit the transparent circle onto the screen
    screen.blit(circle_surface, (250, 150))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
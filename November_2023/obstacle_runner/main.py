import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

screen_width = screen.get_width()
screen_height = screen.get_height()

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('light blue')

    pygame.draw.circle(screen, 'purple', player_pos, 40)

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    # resources used for boundary code below (appendix 1)
    if player_pos.x >= screen_width-40:
        player_pos.x -= 300 * dt
    if player_pos.x <= 0+40:
        player_pos.x += 300 * dt
    if player_pos.y >= screen_height-40:
        player_pos.y -= 300 * dt
    if player_pos.y <= 0+40:
        player_pos.y += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60)/1000

pygame.quit()


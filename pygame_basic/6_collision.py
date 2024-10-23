import pygame

pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Woowoo Game")

#FPS
clock = pygame.time.Clock()

background = pygame.image.load("/Users/js/Desktop/python workspace/pygame_basic/background.png")

#캐릭터 불러오기
character = pygame.image.load("/Users/js/Desktop/python workspace/pygame_basic/isabelle.png")
character_size = character.get_rect().size #rect is rectangle
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래

to_x = 0
to_y = 0

#moving speed
character_speed = 0.6 

enemy = pygame.image.load("/Users/js/Desktop/python workspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #rect is rectangle
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2) #화면 세로 크기 가장 아래

running = True
while running:
    dt = clock.tick(60) # number of frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈출
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("COLLISION!")
        running = False

    screen.blit(background, (0,0)) #배경 그리기 
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()
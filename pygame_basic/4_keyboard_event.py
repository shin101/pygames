import pygame

pygame.init()
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Woowoo Game")

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: 
                to_x -=5
            elif event.key == pygame.K_RIGHT:
                to_x +=5 
            elif event.key == pygame.K_UP:
                to_y -=5
            elif event.key == pygame.K_DOWN:
                to_y +=5 

        if event.type == pygame.KEYUP: #방향키를 떼면 멈출
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x
    character_y_pos += to_y
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


    screen.blit(background, (0,0)) #배경 그리기 
    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()
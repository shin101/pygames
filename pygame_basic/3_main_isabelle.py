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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0)) #배경 그리기 
    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()
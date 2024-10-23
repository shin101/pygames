import os
import pygame

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position

        self.direction = LEFT
        self.angle_speed = 2.5
        self.angle = 10 


    def update(self, to_x):
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
        
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)

        self.offset.x += to_x
        self.rotate()

        # rect_center = self.position + self.offset
        # self.rect = self.image.get_rect(center=rect_center)

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1) 
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.position+offset_rotated)

        #rotozoom is similar to rotate
        #putting - in front of self.angle makes it clockwise
        #goes counter clockwise by default
        #1 means image size will stay unchanged as is.
        
    def set_direction(self, direction):
        self.direction = direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center)

    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)

def setup_gemstone():
    # 작은 금
    small_gold = Gemstone(gemstone_images[0], (200, 380)) 
    gemstone_group.add(small_gold)

    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))
    

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()

# 속도 변수
move_speed = 12 
return_speed = 20


# 게임 관련 변수
default_offset_x_claw = 40
to_x = 0
LEFT = -1
STOP = 0
RIGHT = 1

# 색깔 변수
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))


# 4개 보석 이미지 불러오기
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")),
    pygame.image.load(os.path.join(current_path, "big_gold.png")),
    pygame.image.load(os.path.join(current_path, "stone.png")),
    pygame.image.load(os.path.join(current_path, "diamond.png"))]

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone()

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = Claw(claw_image, (screen_width // 2, 110))


running = True
while running:
    clock.tick(30) # standardize FPS so same game speed no matter what pc you use 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            claw.set_direction(STOP)
            to_x = move_speed
    
    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed

    if claw.offset.x < default_offset_x_claw:
        to_x = 0
        claw.set_init_state()

    screen.blit(background, (0, 0))
    gemstone_group.draw(screen)
    claw.update(to_x)
    claw.draw(screen)
    pygame.display.update()


pygame.quit()

 
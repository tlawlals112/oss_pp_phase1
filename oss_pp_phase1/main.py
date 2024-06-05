import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("톰을 피해라!!")
clock = pygame.time.Clock()
FPS = 60

# 이미지 로드 및 최적화
background = pygame.image.load(r"C:\Users\김서현\Desktop\pygame_basic\background.png").convert()
character = pygame.image.load(r"C:\Users\김서현\Desktop\pygame_basic\character.png").convert_alpha()
angry_jerry = pygame.image.load(r"C:\Users\김서현\Desktop\pygame_basic\angry_jerry.png").convert_alpha()
tom_images = [
    pygame.image.load(r"C:\Users\김서현\Desktop\pygame_basic\tom1.png").convert_alpha(),
    pygame.image.load(r"C:\Users\김서현\Desktop\pygame_basic\tom2.png").convert_alpha(),
    pygame.image.load(r"C:\Users\김서현\Desktop\pygame_basic\tom3.png").convert_alpha()
]

# 캐릭터 크기 및 위치 설정
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면에 그리기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.flip()  # 화면 업데이트 (전체 코드에서는 flip() 사용)
    clock.tick(FPS)  # FPS 제한

# Pygame 종료
pygame.quit()

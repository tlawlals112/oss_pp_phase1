import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("톰을 피해라!!!")
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

# 캐릭터 이동 설정
to_x = 0
speed = 5  # 전체 코드에 맞춰 speed 값 설정

# 똥(tom) 설정
tom_x_pos = random.randint(0, screen_width - tom_images[0].get_width())
tom_y_pos = 0
tom_speed = 5  # 전체 코드에 맞춰 tom_speed 값 설정
current_tom_image = random.choice(tom_images)  # 랜덤 톰 이미지 선택

# 폰트 설정
game_font = pygame.font.Font(None, 40)

# 게임 시간 설정
total_time = 50  # 전체 코드에 맞춰 total_time 값 설정
start_ticks = pygame.time.get_ticks()

# 게임 루프
running = True
while running:
    dt = clock.tick(FPS)  # 프레임 시간 계산

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 캐릭터 이동 처리 (프레임 시간에 따라 이동량 조절)
    character_x_pos += to_x * dt

    # 캐릭터 화면 밖으로 나가지 않도록 설정
    character_x_pos = max(0, min(character_x_pos, screen_width - character_width))

    # 똥(tom) 이동 처리
    tom_y_pos += tom_speed
    if tom_y_pos > screen_height:
        tom_y_pos = 0
        tom_x_pos = random.randint(0, screen_width - current_tom_image.get_width())
        current_tom_image = random.choice(tom_images)

    # 충돌 처리 (Rect 사용)
    character_rect = character.get_rect(topleft=(character_x_pos, character_y_pos))
    tom_rect = current_tom_image.get_rect(topleft=(tom_x_pos, tom_y_pos))
    if character_rect.colliderect(tom_rect):
        character = angry_jerry
        character_y_pos -= 90  # 전체 코드에 맞춰 y 좌표 조정
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    # 화면에 그리기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(current_tom_image, (tom_x_pos, tom_y_pos))  # 똥(tom) 그리기

    # 타이머 표시
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(f"Time: {int(total_time - elapsed_time)}", True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        running = False

    pygame.display.flip()

# 잠시 대기
pygame.time.delay(2000)  # 2초 대기

# Pygame 종료
pygame.quit()

import pygame
import random
import sys
import time
import login  # 필요한 경우 로그인 관련 모듈 임포트
import rank  # 랭킹 모듈 임포트

def main():
    pygame.init()

    # 게임 관련 설정 초기화
    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("톰을 피해라!!!")

    clock = pygame.time.Clock()
    FPS = 60

    background = pygame.image.load(r"./images/background.png").convert()
    character = pygame.image.load(r"./images/character.png").convert_alpha()
    angry_jerry = pygame.image.load(r"./images/angry_jerry.png").convert_alpha()

    tom_images = [
        pygame.transform.scale(pygame.image.load(r"./images/tom1.png").convert_alpha(), (50, 50)),
        pygame.transform.scale(pygame.image.load(r"./images/tom2.png").convert_alpha(), (50, 50)),
        pygame.transform.scale(pygame.image.load(r"./images/tom3.png").convert_alpha(), (50, 50))
    ]

    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width - character_width) / 2
    character_y_pos = screen_height - character_height

    to_x = 0
    speed = 5

    tom_list = []
    tom_speed = 5

    game_font = pygame.font.Font(None, 40)

    start_ticks = pygame.time.get_ticks()  # 시작 시간

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= speed
                elif event.key == pygame.K_RIGHT:
                    to_x += speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0

        character_x_pos += to_x
        character_x_pos = max(0, min(character_x_pos, screen_width - character_width))

        if random.randint(0, 130) == 0:
            tom_x_pos = random.randint(0, screen_width - tom_images[0].get_width())
            tom_y_pos = 0
            current_tom_image = random.choice(tom_images)
            tom_list.append([tom_x_pos, tom_y_pos, current_tom_image])

        for tom in tom_list:
            tom[1] += tom_speed

            if tom[1] > screen_height:
                tom_list.remove(tom)

            character_rect = character.get_rect(topleft=(character_x_pos, character_y_pos))
            tom_rect = tom[2].get_rect(topleft=(tom[0], tom[1]))
            if character_rect.colliderect(tom_rect):
                character = angry_jerry
                character_y_pos -= 90
                pygame.display.update()
                pygame.time.delay(2000)
                running = False

        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        for tom in tom_list:
            screen.blit(tom[2], (tom[0], tom[1]))

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과 시간 계산 (초 단위)
        timer = game_font.render(f"Time: {int(elapsed_time)} sec", True, (255, 255, 255))  # 경과 시간을 화면에 표시
        screen.blit(timer, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # 게임 종료 후 실행되어야 할 코드 추가
    rank.add_ranking(login.logged_in_user, elapsed_time)  # 랭킹에 추가

if __name__ == "__main__":
    main()


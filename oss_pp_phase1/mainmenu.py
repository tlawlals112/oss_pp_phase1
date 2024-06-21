import pygame
import sys
import register
import login
import rank  # 랭킹 모듈을 임포트합니다.
import game  # 게임 모듈을 임포트합니다.

def main_menu():
    pygame.init()

    screen_width = 480
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")

    clock = pygame.time.Clock()
    FPS = 60

    font = pygame.font.Font(None, 40)

    while True:
        screen.fill((0, 0, 0))  # 화면을 검은색으로 채웁니다.

        title = font.render("TOM&JERRY", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen_width // 2, 100))
        screen.blit(title, title_rect)

        start_button = font.render("Start", True, (255, 255, 255))
        start_rect = start_button.get_rect(center=(screen_width // 2, 250))
        screen.blit(start_button, start_rect)

        login_button = font.render("Login", True, (255, 255, 255))
        login_rect = login_button.get_rect(center=(screen_width // 2, 350))
        screen.blit(login_button, login_rect)

        register_button = font.render("Register", True, (255, 255, 255))
        register_rect = register_button.get_rect(center=(screen_width // 2, 450))
        screen.blit(register_button, register_rect)

        rank_button = font.render("Rankings", True, (255, 255, 255))
        rank_rect = rank_button.get_rect(center=(screen_width // 2, 550))
        screen.blit(rank_button, rank_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if start_rect.collidepoint(mouse_pos):
                    if not login.is_logged_in():
                        print("로그인이 필요합니다.")
                    else:
                        game.main()  # 게임 시작

                elif login_rect.collidepoint(mouse_pos):
                    username = input("사용자 이름: ")
                    password = input("비밀번호: ")
                    if login.login_user(username, password):
                        print("로그인 성공!")

                elif register_rect.collidepoint(mouse_pos):
                    username = input("사용자 이름: ")
                    password = input("비밀번호: ")
                    if register.register_user(username, password):
                        print("회원가입 성공!")

                elif rank_rect.collidepoint(mouse_pos):
                    show_ranking(screen, font, screen_width)  # 랭킹 표시

        clock.tick(FPS)

def show_ranking(screen, font, screen_width):
    rankings = rank.get_rankings()

    screen.fill((0, 0, 0))  # 화면을 검은색으로 채웁니다.

    title_text = font.render("Rankings", True, (255, 255, 255))
    screen.blit(title_text, ((screen_width - title_text.get_width()) // 2, 50))

    y_offset = 150
    for idx, ranking in enumerate(rankings[:5]):  # 상위 5개 랭킹 표시
        rank_text = font.render(f"{idx + 1}. {ranking['username']}: {ranking['game_time']} sec", True, (255, 255, 255))
        screen.blit(rank_text, ((screen_width - rank_text.get_width()) // 2, y_offset))
        y_offset += 50

    return_to_menu_text = font.render("Press any key to return to menu.", True, (255, 255, 255))
    screen.blit(return_to_menu_text, ((screen_width - return_to_menu_text.get_width()) // 2, 500))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False

if __name__ == "__main__":
    main_menu()


import pygame
import random  # 전체 코드에 random 모듈이 사용되므로 포함

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기")  # 전체 코드의 게임 제목 사용
clock = pygame.time.Clock()  # 전체 코드에서 사용되는 clock 객체 추가
FPS = 60  # 전체 코드에서 사용되는 FPS 값 추가
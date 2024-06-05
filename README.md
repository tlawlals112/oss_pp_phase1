# 톰을 피해라!!!

## 게임 설명

"톰을 피해라!!!"는 파이썬 Pygame 라이브러리를 사용하여 제작된 간단한 아케이드 게임입니다. 플레이어는 제리를 조종하여 화면 위에서 떨어지는 톰들을 피해야 합니다. 톰과 충돌하면 제리가 화를 내며 게임이 종료됩니다. 제한 시간 동안 최대한 오래 버티는 것이 목표입니다.

## 실행 방법

### Docker 사용

1.  **Docker 설치:** Docker가 설치되어 있지 않다면, [공식 Docker 웹사이트](https://www.docker.com/)에서 설치합니다.
2.  **Docker 이미지 빌드:** 프로젝트 디렉토리에서 다음 명령어를 실행하여 Docker 이미지를 빌드합니다.

```bash
docker build -t tom-avoid-game .
3. **Docker 컨테이너 실행:** 다음 명령어를 실행하여 컨테이너를 실행하고 게임을 시작합니다.

docker run -it --rm \
    -e DISPLAY=<span class="math-inline">DISPLAY \\
\-\-mount type\=bind,source\="</span>(pwd)"/images,target=/app/images \
    tom-avoid-game 


## 직접 실행 (Windows 환경)
1.  **Pygame 설치: Pygame 라이브러리가 설치되어 있지 않다면, 다음 명령어를 사용하여 설치합니다.
 
pip install pygame

2. ** 게임 실행: 프로젝트 디렉토리에서 다음 명령어를 실행하여 게임을 시작합니다.

python main.py


## 조작 방법
왼쪽 화살표 키: 제리를 왼쪽으로 이동
오른쪽 화살표 키: 제리를 오른쪽으로 이동
##게임 종료 조건
제리가 톰과 충돌하면 게임 종료
제한 시간이 초과되면 게임 종료


# rank.py

ranking_file = "rankings.txt"

def add_ranking(username, game_time):
    rankings = get_rankings()
    rankings.append({'username': username, 'game_time': game_time})
    rankings.sort(key=lambda x: x['game_time'], reverse=True)  # Sort rankings by game_time (descending)

    with open(ranking_file, 'w') as file:
        for ranking in rankings:
            file.write(f"{ranking['username']}:{ranking['game_time']}\n")

def get_rankings():
    rankings = []
    try:
        with open(ranking_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    username, game_time = line.strip().split(':')
                    rankings.append({'username': username, 'game_time': float(game_time)})
    except FileNotFoundError:
        print("랭킹 파일이 존재하지 않습니다.")

    rankings.sort(key=lambda x: x['game_time'], reverse=True)  # Sort rankings by game_time (descending)
    return rankings


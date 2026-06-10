# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번:20523 임서준
# 프로젝트 주제: 

import random

# 선수 이름 입력
player = input("선수 이름을 입력하세요: ")

# 2차원 리스트: 토너먼트 단계 정보
# [단계명, 설명, 정규전 횟수, 통과 목표]
stages = [
    ["8강", "첫 번째 경기", 5, "준결승 진출"],
    ["4강", "두 번째 경기", 5, "결승 진출"],
    ["결승", "최종 경기", 5, "우승"]
]

def direction(n):
    if n == 1:
        return "왼쪽"
    elif n == 2:
        return "가운데"
    else:
        return "오른쪽"

def get_choice(prompt):
    while True:
        ans = input(prompt)

        if ans == "1" or ans == "2" or ans == "3":
            return int(ans)
        else:
            print("1, 2, 3 중에서 올바르게 입력하세요.")

def user_attack():
    shot = get_choice(f"{player}의 슛 방향 (1.왼쪽 2.가운데 3.오른쪽): ")
    save = random.randint(1, 3)

    print(player + "의 슛:", direction(shot))
    print("컴퓨터 수비:", direction(save))

    if shot == save:
        print("막혔습니다!")
        return 0
    else:
        print("골!")
        return 1

def computer_attack():
    shot = random.randint(1, 3)
    save = get_choice(f"{player}가 막을 방향 (1.왼쪽 2.가운데 3.오른쪽): ")

    print("컴퓨터 슛:", direction(shot))
    print(player + "의 수비:", direction(save))

    if shot == save:
        print("막았습니다!")
        return 0
    else:
        print("실점!")
        return 1

def match(stage_info):
    stage_name = stage_info[0]
    round_count = stage_info[2]

    print("\n====", stage_name, "====")
    print(stage_info[1], "- 정규", round_count, "차전 진행")

    # 점수판 (2차원 리스트)
    score_board = [
        [player, 0],
        ["컴퓨터", 0]
    ]

    # 정규 승부차기
    for i in range(round_count):
        print("\n", i + 1, "차전")

        print("[내 공격]")
        score_board[0][1] += user_attack()

        print("[컴퓨터 공격]")
        score_board[1][1] += computer_attack()

    # 동점이면 연장전
    if score_board[0][1] == score_board[1][1]:

        while True:
            print("\n연장전!")

            u = user_attack()
            c = computer_attack()

            score_board[0][1] += u
            score_board[1][1] += c

            # 승부가 나면 종료
            if u > c:
                break
            elif c > u:
                break

    print("\n결과")
    print(player + ":", score_board[0][1], "점")
    print("컴퓨터:", score_board[1][1], "점")

    if score_board[0][1] > score_board[1][1]:
        print("이겼습니다!")
        return True
    else:
        print("졌습니다!")
        return False

def show_trophy():
    print("""
         ___________
        '._==_==_=_.'
        .-\\:      /-.
       | (|:.     |) |
        '-|:.     |-'
          \\::.    /
           '::. .'
             ) (
           _.' '._
          `\"\"\"\"\"\"\"`
    """)
    print("축하합니다!")
    print(player, "선수가 토너먼트 챔피언이 되었습니다!")

def tournament():
    for stage_info in stages:

        win = match(stage_info)

        if not win:
            print("\n토너먼트 탈락!")
            return

    print("\n우승!")
    print("토너먼트 챔피언!")
    show_trophy()

# 게임 시작
tournament()
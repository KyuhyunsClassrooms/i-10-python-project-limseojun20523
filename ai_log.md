# Gemini 활용 기록

> 이번 수행평가에서는 학교 계정 Gemini 사용을 허용합니다.  
> 단, Gemini가 만든 코드를 이해하지 못한 채 그대로 제출하면 안 됩니다.  
> 실제 개인정보, 친구 이름, 성적, 전화번호, 주소 등은 절대 입력하지 않습니다.

---

## 1차 Gemini 활용

- 사용 날짜: 6월 10일
- 사용 목적: 코드 수정
- 내가 입력한 프롬프트: 작성한 축구 승부차기 토너먼트 코드의 필수 조건 충족 여부 및 금지 사항 검토 요청

```text
내가 축구 승부차기 게임 코드를 짜봤어. 이 게임은 단순한 축구 승부차기 게임이 아니라 컴퓨터와 대결하고 토너먼트 시스템도 추가되어있어. 여기에 너가 말한 필수 구현 조건 8가지가 충족되었는지, 금지 사항 중에 충족되는 것이 있는지 확인해줘.


import random

# 2차원 리스트: 토너먼트 단계 정보
# [단계명, 설명, 정규전 횟수, 통과 목표]
stages = [
    ["8강", "첫 번째 경기", 3, "준결승 진출"],
    ["4강", "두 번째 경기", 3, "결승 진출"],
    ["결승", "최종 경기", 3, "우승"]
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
        try:
            n = int(input(prompt))
            if n in [1, 2, 3]:
                return n
            print("1, 2, 3 중에서 입력하세요.")
        except ValueError:
            print("숫자로 입력하세요.")

def user_attack():
    shot = get_choice("내 슛 방향 (1.왼쪽 2.가운데 3.오른쪽): ")
    save = random.randint(1, 3)

    print("내 슛:", direction(shot))
    print("컴퓨터 수비:", direction(save))

    if shot == save:
        print("막혔습니다!")
        return 0
    else:
        print("골!")
        return 1

def computer_attack():
    shot = random.randint(1, 3)
    save = get_choice("막을 방향 (1.왼쪽 2.가운데 3.오른쪽): ")

    print("컴퓨터 슛:", direction(shot))
    print("내 수비:", direction(save))

    if shot == save:
        print("막았습니다!")
        return 0
    else:
        print("실점!")
        return 1

def match(stage_info):
    stage_name = stage_info[0]
    round_count = stage_info[2]

    print(f"\n==== {stage_name} ====")
    print(f"{stage_info[1]} - 정규 {round_count}차전 진행")

    # 2차원 리스트로 점수 관리
    score_board = [["나", 0], ["컴퓨터", 0]]

    for i in range(round_count):
        print(f"\n{i + 1}차전")

        print("[내 공격]")
        score_board[0][1] += user_attack()

        print("[컴퓨터 공격]")
        score_board[1][1] += computer_attack()

    while score_board[0][1] == score_board[1][1]:
        print("\n서든데스!")

        u = user_attack()
        c = computer_attack()

        score_board[0][1] += u
        score_board[1][1] += c

    print("\n결과")
    print("나:", score_board[0][1], "점")
    print("컴퓨터:", score_board[1][1], "점")

    if score_board[0][1] > score_board[1][1]:
        print("이겼습니다!")
        return True
    else:
        print("졌습니다!")
        return False

def tournament():
    for stage_info in stages:
        win = match(stage_info)
        if not win:
            print("\n토너먼트 탈락!")
            return

    print("\n우승!")
    print("토너먼트 챔피언!")

tournament()

이 코드에 수정할만한 요소이 있거나 어려운 문법이 들어가있으면 우리가 배운 문법을 토대로 다시 코드를 수정해주고 너가 바꾼 부분을 나에게 보고해줘.
```

- Gemini가 제안한 내용 요약:필수 조건은 모두 만족하나, 수업 범위를 벗어날 수 있는 try-except 문법 대신 문자열 비교 방식을 제안함.
- 내가 반영한 부분:get_choice 함수를 문자열 비교 방식으로 수정하여 코드인터뷰 설명을 더 쉽게 대비함.
- 내가 수정하거나 사용하지 않은 부분:어렵고 아직 배우지 않은 문법인 try-except를 걷어내고 안전한 문자열 비교로 바꾸었다.
- 반영 위치: main.py 27번, 41번 줄

---

## 2차 Gemini 활용

- 사용 날짜:6월 11일
- 사용 목적:승부차기 게임에 '실축 시스템'을 추가하는 방법과 필요한 문법 문의
- 내가 입력한 프롬프트:이전에 보냈던 코드의 내용을 토대로 실축 시스템 구현을 위한 도움 요청

```text
지금 코드에 실축 시스템을 추가하고 싶은데 어떤 문법을 사용해야해?
```

- Gemini가 제안한 내용 요약:
1.random.randint() 문법을 사용하여 1~20까지 사이의 난수를 뽑고 만약 뽑은 숫자가 1 혹은 2이면 10퍼센트의 확률로 실축하게 되는 시스템을 만들 수 있다.
2.조건문을 사용하여 슛이 성공적으로 날아갔는지에 대한 조건을 하나 더 추가하면 실축하는 시스템을 만들 수 있다.

- 내가 반영한 부분:random.randint(1, 20)으로 설정한 후 3가지의 변수 상황을 만들어 20개 중에 3개, 즉 15퍼센트의 확률로 실축되는 시스템을 추가하였다.

- 내가 수정하거나 사용하지 않은 부분:
1.random.randint()문법에서 gemini는 1~10 사이의 1개의 변수 상황을 만들어 10퍼센트의 확률로 실축되는 시스템을 만들고자 하였지만, 확률을 좀 더 올리고 싶어 15퍼센트로 수정함
2.조건문을 사용하면 복잡해져서 random 시스템을 사용함

- 반영 위치:
main.py 43번 줄, 70번 줄

---

## 3차 Gemini 활용

- 사용 날짜:6월 16일
- 사용 목적:import random 문구의 필수 여부와 생략 시 발생하는 오류 원인을 명확히 이해하기 위함.
- 내가 입력한 프롬프트: 이전에 작성하였던 코드를 이해하기 위해 코드의 첫줄부터 있는 import함수를 설명해달라고 함 

```text
내가 보낸 코드의 첫줄에 있는 import라는 함수는 내가 배운 것이 아닌데, 선생님이 import가 무엇인지에 대한 질문을 한다면 어떻게 대답해야 할까?
```

- Gemini가 제안한 내용 요약:import는 함수가 아니라 라이브러리를 불러오는 '명령어'임을 바로잡아 주고, 컴퓨터의 무작위 행동을 위해 random 도구 상자를 가져온 이유를 설명하는 면접 답변 틀을 제공함.
- 내가 반영한 부분:report.md 작성 및 최종 코드인터뷰 준비 과정에 반영.
- 내가 수정하거나 사용하지 않은 부분:없음
- 반영 위치:main.py 5번줄

---

## AI 활용 성찰

Gemini가 도움이 된 점:AI는 승부차기 게임의 코드 구조를 개선하는 데 도움을 주었다. 특히 2차원 리스트를 활용하여 토너먼트 단계를 관리하는 방법, 함수 분리 방법, 입력 오류 처리 방법 등을 제안해 주었다. 또한 연장전 기능, 선수 이름 입력 기능, 실축 시스템, 우승 트로피 출력 기능 등의 아이디어를 제공하여 프로그램의 완성도를 높이는 데 도움이 되었다.


Gemini의 제안을 그대로 쓰지 않고 내가 판단하거나 수정한 점:AI가 처음 제안한 코드와 기능을 그대로 사용하지는 않았다. 수행평가 조건에 맞도록 try-except를 제거하고 문자열 비교 방식으로 입력 검사를 수정하였다. 또한 승부차기 횟수를 3회에서 5회로 변경하였고, 연장전 반복문도 수행평가에서 요구한 while True와 break 구조로 수정하였다. 실축 시스템의 적용 여부와 게임 기능들도 직접 판단하여 선택하였다.


다음에 AI를 사용할 때 주의해야 할 점:AI가 제안한 내용이 항상 과제 조건에 맞는 것은 아니므로 그대로 사용하기 전에 반드시 확인해야 한다. 또한 AI가 작성한 코드의 동작 원리를 이해하고 직접 실행하여 오류가 없는지 검토해야 한다. 앞으로는 AI의 도움을 참고 자료로 활용하되, 최종 결과물은 직접 판단하고 수정하는 과정을 거쳐 사용해야겠다.


import random

while True:
    def match(c, p):
        if c == p:
            return ('비겼습니다!')
        elif match_dic[c] == p:
            return ('졌습니다!')
        else:
            return ('이겼습니다!')

    rsp_dic = {0: '가위', 1: '바위', 2: '보'}
    match_dic = {'가위': '보', '바위': '가위', '보': '바위'}

    computer = rsp_dic[random.randint(0, 2)]

    player = input('가위 바위 보 중 하나를 내세요:')

    result = match(computer, player)
    print(result)

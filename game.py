import random
numbers = random.randint(1, 100)

game_count = 0

while True:
    usernum = int(input('1부터 100까지 중 숫자 하나를 입력하세요 :'))
    game_count += 1

    if (usernum < numbers):
        print('UP!')
    elif (usernum > numbers):
        print('DOWN!')
    else:
        print(f'정답입니다!, {game_count}회 만에 맞췄습니다^^!')

        more = input('게임을 더 하시겠습니까?[Y/N]:')

        if (more == 'Y'):
            print('게임을 다시 시작합니다')
        elif (more == 'N'):
            print('게임을 종료합니다.')
            break
        else:
            print('대문자로 답변해주세요.')
            one_more = input('게임을 더 하시겠습니까?[Y/N]:')
            if (one_more == 'Y'):
                print('게임을 다시 시작합니다.')
            else:
                print('게임을 종료합니다')
                break

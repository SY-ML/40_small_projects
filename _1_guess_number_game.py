"""
# Summary #
Users should guess the answer which is a number between 1 and 100 (both included)
If users give a valid input, then a hint will be given if it is bigger or smaller than the answer

숫자를 하나 입력하면 임의로 생성된 수 보다 높은지 낮은지 정답인지를 알려줍니다.
정답을 맞힌 경우 정답을 몇 번 만에 맞추었는지 그 결과로 게임의 승부를 알 수 있습니다.
"""

import random

answer = random.randint(1, 100)

# Number of total tirals
count_try = 0

# User input log >> to be used to provide a user with the valid range of numbers
log = {'UP':[0], 'DOWN':[101]}

while (1):
    # user input
    user_input = input(f"Insert a number between ({max(log['UP'])+1} ~ {min(log['DOWN'])-1}): ")

    # CHECK 1 : DOES THE INPUT CONTAIN NON-NUMBER VALUE?
    if user_input.isnumeric(): # in the case that only numbers are contained
        user_input = int(user_input) # convert from string to integer
        max_up, min_down = max(log['UP']), min(log['DOWN']) # valid number milestones
        # CHECK 2: IS THE INPUT IN THE VALID RANGE?
        if user_input > 100 or user_input == 0:
            print('ERROR) Invalid Number! Insert a number between 1 and 100.')
            continue
        # CHECK 2: IS THE INPUT IN THE VALID RANGE?
        elif user_input < max_up+1:
            print(f'ERROR) Invalid Number! Insert a number greater than {max_up}.')
            continue
        # CHECK 2: IS THE INPUT IN THE VALID RANGE?
        elif user_input > min_down-1:
            print(f'ERROR) Invalid Number! Insert a number less than {min_down}.')
            continue
    # CHECK 1 : DOES THE INPUT CONTAIN NON-NUMBER VALUE?
    else: # in the case that only numbers are not contained
        print('ERROR) Invalid Number! Insert a number without any character')
        continue

    count_try+=1
    if answer == user_input: # 정답인 경우
        unit = 'trial' if count_try == 1 else 'trials'
        print(f'Congratulations!. The answer is {answer}! You have completed with {count_try} {unit}.')
        break

    else:
        msg = 'UP' if answer > user_input else 'DOWN'
        log[msg].append(user_input)
        print(msg)


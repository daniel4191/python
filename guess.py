import random

randint = random.randint(1,100)

n = 1
while True:
    if n >20:
        print("시도 횟수를 모두 소진 했습니다.")
        break
    else:
        x = int(input(f"숫자를 맞혀보세요{n}번째 시도: "))
    
    if x == randint:
        print(f"정답입니다. {x}를 맞췄습니다. {n}번째 시도")
        break
    elif x > randint:
        print(f"{x}보다 작습니다. 다시 시도해보세요. {n}번째 시도")
        n += 1
    elif x < randint:
        print(f"{x}보다 큽니다. 다시 시도해보세요. {n}번째 시도")
        n += 1        

while True:
    n = 1
    print(f"{n}회차 시도 합니다. 현재 틱택토 상태")
    
    basic = [0,0,0,0,0,0,0,0,0]
    a = 3
    
    # 현재
    
    for i in range(0,len(basic),a):
        print(basic[i:i+a])
        
    player1 = int(input("몇번째 리스트에 넣으시겠어요? 0~8: "))
    player2 = int(input("몇번째 리스트에 넣으시겠어요? 0~8: "))
    
    basic[player1] = 1
    basic[player2] = 2
    
    if basic[1,2,3] == 1:
        
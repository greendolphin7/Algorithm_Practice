# 에라토스테네스의 체

N, K = list((input().split()))

N = int(N)  # 정수 N
K = int(K)  # K번째로 지워지는 수 찾기

num_list = [n for n in range(2, N+1)]

count = 0  # K 번째에 프린트해주기 위한 카운트 변수
for number in num_list:  # 전체 리스트 반복
    if number != 0:  # 만약 해당 요소가 0이 아니라면 (0 이면 이미 지웠다는 뜻!)
        for num in range(number, len(num_list)+2, number):  # number의 배수들을 없애기
            
            if num in num_list:  # 만약에 배수가 번호 리스트에 존재하면
                index = num_list.index(num)  # 인덱스 가져와서
                temp = num_list[index] 
                num_list[index] = 0  # 해당 인덱스의 요소 0으로 변경
                count += 1  # 삭제후에는 카운트 추가
                
                if count == K:  # K 번 삭제 했다면 
                    print(temp)  # 출력하고 끝
                    break

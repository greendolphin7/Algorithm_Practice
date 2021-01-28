import collections
import sys

def input():
    return int(sys.stdin.readline())  # 인풋이 시간을 엄청 잡아먹을 줄 몰랐다. 앞으로는 이렇게 쓰자
    
n = int(input())

num_list = []   # 데이터 받아주고
for num in range(n):
    num = int(input())
    num_list.append(num)

# 산술 평균
def cal_avg(num_list):
    avg = round(sum(num_list) / n)  # sum 나누기 갯수 
    return avg

# 중앙값
def median(num_list):  # 정렬하고 가장 가운데 인덱스 숫자 
    num_list.sort()
    med_num = num_list[n // 2]  # (이 문제는 특이하게도 결과가 정수를 고집해서 몫 인덱스로 충분하다)
    return med_num

# 최빈값
def mode_num(num_list): 
    count = collections.Counter(num_list).most_common()  # 라이브러리를 사용하지 않으면 시간초과 발생
    if len(count) > 1 and count[0][1] == count[1][1]:  # 최빈값이 여러개인 경우를 위한 조건
        return count[1][0]  # 리스트 안에 튜플 형식이다.
    else:                   # [(해당 숫자, 숫자 갯수)]
        return count[0][0]  # 최빈값 한개면 바로 리턴

# 범위 
def cal_range(num_list):  # 범위는 최대값 - 최소값
    min_num = min(num_list)
    max_num = max(num_list)
    return (max_num - min_num)

print(cal_avg(num_list))
print(median(num_list))
print(mode_num(num_list))
print(cal_range(num_list))
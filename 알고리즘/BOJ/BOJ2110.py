# 공유기 설치

N, C = map(int, input().split(' '))
# buildings = list(int(input()) for _ in range(N))
buildings = []
for _ in range(N):
    buildings.append(int(input()))

# 건물 위치 정렬
buildings = sorted(buildings)

# 시작점과 끝 값 저장
start = buildings[1] - buildings[0]  # 가장 가까이 있는 gap
end = buildings[-1] - buildings[0]  # 가장 먼 곳에 있는 gap

# 최적의 gap을 구하는 것이 목적
result = 0

# 시작점이 끝점을 넘지 않는 선에서 
while (start <= end):
    # 중간값을 시작점과 끝점 사이에 저장
    mid = (start + end) // 2  # mid는 결국 gap
    # 현재 설치할 수 있는 후보 값을 초기화
    value = buildings[0]
    count = 1

    # 전체 건물들을 순회하면서
    for i in range(1, len(buildings)):
        # 만약 어떤 건물이 현재 건물에서 gap만큼 더한 것보다 더 크다면
        if buildings[i] >= value + mid:
            # 거기서 후보 건물 초기화해주고
            value = buildings[i]
            # 공유기 설치
            count += 1
    # 설치할 수 있는 공유기가 설치한 공유기와 같다면
    if count >= C:
        # 더 설치할 수 있는지 확인
        start = mid + 1
        # 해당 결과 저장
        result = mid
    else:
        end = mid - 1
print(result)

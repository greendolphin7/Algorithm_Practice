# 구구단

def gugudan(s, e):
    if s > e:
        for i in range(1, 10):
            answer = ''
            for k in range(s, e - 1, -1):
                if k * i // 10 == 0:
                    ki = ' ' + str(k * i)
                else:
                    ki = str(k * i)
                answer += '%s * %s = %s   ' %(str(k), str(i), ki)
            print(answer)
    else:
        for i in range(1, 10):
            answer = ''
            for k in range(s, e + 1):
                if k * i // 10 == 0:
                    ki = ' ' + str(k * i)
                else:
                    ki = str(k * i)
                answer += '%s * %s = %s   ' %(str(k), str(i), ki)
            print(answer)


s, e = map(int, input().split())
while True:
    if 2 <= s <= 9 and 2 <= e <= 9:
        break
    else:
        print("INPUT ERROR!")
        s, e = map(int, input().split())
gugudan(s, e)

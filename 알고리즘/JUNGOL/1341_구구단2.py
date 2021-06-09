# 구구단2

# 구구단

def gugudan(s, e):
    if s > e:
        for k in range(s, e - 1, -1):
            answer = ''
            for i in range(1, 10):
                if k * i // 10 == 0:
                    ki = ' ' + str(k * i)
                else:
                    ki = str(k * i)
                answer += '%s * %s = %s   ' %(str(k), str(i), ki)
                if i % 3 == 0:
                    print(answer)
                    answer = ''
            print()
    else:
        for k in range(s, e + 1):
            answer = ''
            for i in range(1, 10):    
                if k * i // 10 == 0:
                    ki = ' ' + str(k * i)
                else:
                    ki = str(k * i)
                answer += '%s * %s = %s   ' %(str(k), str(i), ki)
                if i % 3 == 0:
                    print(answer)
                    answer = ''
            print()


s, e = map(int, input().split())

gugudan(s, e)

# 영준이의 카드 카운팅

def find_card(card_list):
    space_list = []
    heart_list = []
    diamond_list = []
    clova_list = []

    for i in range(len(card_list)):
        if card_list[i] == 'S':
            if int(card_list[i+1:i+3]) in space_list:
                return 'ERROR'
            space_list.append(int(card_list[i+1:i+3]))

        elif card_list[i] == 'D':
            if int(card_list[i+1:i+3]) in diamond_list:
                return 'ERROR'
            diamond_list.append(int(card_list[i+1:i+3]))

        elif card_list[i] == 'H':
            if int(card_list[i+1:i+3]) in heart_list:
                return 'ERROR'
            heart_list.append(int(card_list[i+1:i+3]))

        elif card_list[i] == 'C':
            if int(card_list[i+1:i+3]) in clova_list:
                return 'ERROR'
            clova_list.append(int(card_list[i+1:i+3]))
    
    need_space = 13 - len(space_list)
    need_heart = 13 - len(heart_list)
    need_diamond = 13 - len(diamond_list)
    need_clova = 13 - len(clova_list)

    return str(need_space) + ' ' + str(need_diamond) + ' ' + str(need_heart) + ' ' + str(need_clova)

T = int(input())
for tc in range(1, T + 1):
    card_list = input()

    print('#%s ' %(tc) + find_card(card_list))

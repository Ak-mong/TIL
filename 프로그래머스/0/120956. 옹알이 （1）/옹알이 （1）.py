def solution(babbling):
    answer = 0
    babbles =  [ "aya", "ye", "woo", "ma"]
    for bab in babbling:
        cor = ''
        for i in range(4):
            if bab.find(babbles[i]) != -1:
                cor += babbles[i]
        if len(bab) == len(cor):
            answer += 1
    return answer
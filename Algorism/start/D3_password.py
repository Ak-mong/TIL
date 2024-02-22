# 단순 2진 암호코드
'''
암호코드 8개의 숫자
올바른 암호 : 홀수자리 합 *3 + 짝수자리합 = 10의 배수

스캐너를 만들자
스캐너는 직사각형 배열을 읽는다
암호 가로 길이 = 8*7
숫자 하나 = 7개의 비트로 암호화
'''
import sys;sys.stdin = open('txt/password.txt')
password = {
     '0001101': 0,
     '0011001': 1,
     '0010011': 2,
     '0111101': 3,
     '0100011': 4,
     '0110001': 5,
     '0101111': 6,
     '0111011': 7,
     '0110111': 8,
     '0001011': 9,
}
def scan_password(arr):
    for i in range(n):
        for j in range(m-1,-1,-1):
            if arr[i][j] == 1:
            # 어떻게 0을 찾았을 때 암호문의 시작일까? 뒤는 전부 1이니 뒤에서 부터 찾자
                return i,j

t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    passowrd_arr = [list(map(int,input())) for _ in range(n)]
    # for i in arr: print(i)
    # 스캐너 돌리기 = 암호코드 1개 포함된 직사각형 배열 찾기
    #7개의 비트가 한글자 => 8글자
    #리스트 슬라이싱
    r,c = scan_password(passowrd_arr) # 스캐너로 암호 시작점
    passowrd_arr2 = ''.join(map(str,passowrd_arr[r][c-55:c+1]))
    new_arr = []
    a, b = 0,7
    while b <= len(passowrd_arr2)+1:
        # print(passowrd_arr2[a:b])
        new_arr.append(password[passowrd_arr2[a:b]])
        a = b
        b = b+7

    test_sum = 0
    for i in range(len(new_arr)):
        # 올바른 암호 : 홀수자리 합 *3 + 짝수자리합 = 10의 배수
        # 자리가 1부터 시작됨 => 홀짝 반대로
        if not i % 2:
            test_sum += new_arr[i]*3
        else:
            test_sum += new_arr[i]
    # print(test_sum)
    if test_sum % 10 == 0:
        print(f'#{tc} {sum(new_arr)}')
    else:
        print(f'#{tc}',0)
    # print(r,c)
    # if
    # print(new_str)
    # 검증코드 확인
    #검증됐으면 숫자 더하기
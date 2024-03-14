import sys;
# 너의 평점은 실버 5 25206
arr = [list(sys.stdin.readline().split()) for _ in range(20)]
grade = {'A+': 4.5, 'A0': 4.0,'B+': 3.5,'B0': 3.0,'C+': 2.5,'C0': 2.0,'D+': 1.5,'D0': 1.0,'F': 0.0}
sum_v = 0
score_v = 0
for i in arr:
    score = float(i[1]) #
    if i[2] == 'P': continue
    grade_v = grade[i[2]]
    sum_v += score * grade_v
    score_v += score
print(sum_v/score_v)
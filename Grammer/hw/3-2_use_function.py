pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject,day,title = None):
    global pro_num
    data = {}
    data['과목'] = subject
    data['일자'] = day
    data['제목'] = title
    data['문제 번호'] = pro_num + 1
    pro_num += 1
    return data

result1 = create_data('python',3)
result2 = create_data(day = 1,subject= 'web',title='web 연습하기''python')
# input1, input2, input3 = global_data.values()
# result3 = create_data(input1,input2,input3)
result3 = create_data(**global_data)

print(result1)
print(result2)
print(result3)

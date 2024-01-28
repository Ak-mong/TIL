data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for d in data:
    for key, value in d.items():
        print(f'{key}은/는 {value}입니다.')
    print()

for phone in data:
    for key in key_list:
        if not phone.get(key):
            phone.setdefault(key, 'unknowns')
        print(f'{key}은/는 {phone[key]}입니다.')
    print()
print('-'*50)
for dt in data:
    for key in key_list:
        if dt.get(key) == None:
            dt.setdefault(key,'unknown')
        print(f'{key} 은/는 {dt[key]}입니다.')
    print()
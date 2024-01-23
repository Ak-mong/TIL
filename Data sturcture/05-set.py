# my_set = {'a','b','c',1,2,3}

# my_set.add(4)
# print(my_set) #출력할때 요소는 같지만 배치는 달라짐

# my_set.add(4)
# print(f"add " + my_set)

# my_set.remove('a')
# # my_set.remove('z') # key error 나옴
# print("remove "+my_set) 

# element = my_set.pop()
# print("pop() : "+ element)

# # my_set2 = {'a','b','c','d'}
# # element2 = my_set2.pop()
# # print(element2)
# # print(my_set2)

# my_set.update([1,4,5])
# print("update() : " + my_set)

# my_set.discard(1)
# print("discard() : "+ my_set)

# result = my_set.discard('z')
# print('discard() result' + result)
# print('discard(): ' + my_set)

# my_set.clear()
# print('clear: ' + my_set)

set1 = {0,1,2,3,4}
set2 = {1,3,5,7,9}
set3 = {0,1}

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.issuperset(set3))
print(set1.union(set2))


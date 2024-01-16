a_string = 'hello?'

#list comprehension
list_range = list(range(0,10,2))
print(list_range) #[0, 2, 4, 6, 8]

list_com = [i for i in range(0,10,2)]
print(list_com) #[0, 2, 4, 6, 8]

list_com2 = [i for i in range(0,10) if i % 2 != 0] #홀수로만 리스트만듦
print(list_com2) #[1,3,5,7,9]

list_op = [i**2 for i in range(0,10,2)]
print(list_op) #[0, 4, 8, 16, 36, 64]

list_up = [i.upper() for i in a_string]
print(list_up) #['H', 'E', 'L', 'L', 'O', '?']

list_gen = (i**2 for i in range(10) if i % 2 == 0) #제너레이터 expression, 리스트를 만드는게 아니라 제너레이터 오브젝트만 생성
print(list_gen) #<generator object <genexpr> at 0x102ba4740>
print(list(list_gen)) #[0, 4, 16, 36, 64]



#filter
list3 = list(range(0,25))
print(list3)

def is_multiple(x):
    return x % 3 == 0 #3의 배수이면 True를 리턴함

#filter function : generator이다. 실제 객체를 만드는것이아님. 함수를 argument로 받아서 객체에 어떤 작업을 할 수 있다.
print(list(filter(is_multiple, list3))) #3의 배수로만 구성된 리스트 출력됨

#lambda function : anonymous function 이름없는 무명 함수
#무명함수로 함수로서의 다양한 기능을 손쉽게 수행, 필터랑 같이쓰면 함수가 들어갈 매개변수자리에 람다식 사용
list4 = list(filter(lambda x: x % 3 == 0, list3))#list3에서 하나씩 x로 받아서 3의 배수이면 filter를 거쳐 3의배수로 이루어진 리스트를 만듦
print(list4) #3의 배수로만 구성된 리스트 출력


#map
print(list(map(lambda x: x**2, list4))) #제곱한 값을 list4와 대칭적으로 순서 똑같이 집어넣어 리스트를 만들어라
list(map(lambda x: x**2, filter(lambda x: x%3 ==0, list3)))
print([i**2 for i in list4])
print(x**2 for x in list3 if x%3 == 0)

"""
[0, 9, 36, 81, 144, 225, 324, 441, 576]
[0, 9, 36, 81, 144, 225, 324, 441, 576]
[0, 9, 36, 81, 144, 225, 324, 441, 576]
[0, 9, 36, 81, 144, 225, 324, 441, 576]
출력값은 같으므로, 람다와 map을 남발하지말고 리스트컴프리헨션을 이용
"""

#zip: 두개의 리스트 object에서 쌍으로 뽑아낼때 사용
players = ['Ryu', 'de', 'jikey' ,'eru']; goals = [7,20,15,7]
for last_name, goal in zip(players, goals):
    print(f'{last_name} : {goal}')


"""
Ryu : 7
de : 20
jikey : 15
eru : 7
"""

#matirx expression of list
a= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a) # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for row in a:
    for col in row:
        print(col, end=" ")
    print()

"""
1 2 3 4 
5 6 7 8 
9 10 11 12 
"""

list_a = list(range(0,8,2))
list_c = [i>3 for i in list_a]
print(list_c)





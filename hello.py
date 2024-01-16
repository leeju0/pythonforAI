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

#filter function : generator이다. 실제 객체를 만드는것이아님. 펑션을 argument로 받아서 객체에 어떤 작업을 할 수 있다.
print(list(filter(is_multiple, list3))) #3의 배수로만 구성된 리스트 출력됨

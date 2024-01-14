A,B,C = map(int,input().split()) #여러 값을 한번에 입력받는 방법. m
"""
    map(매칭할자료형,입력받을값) 
    split() : 입력값을 받아서 하나씩 쪼개서 iteration형태로 만듦
    sep = '\n' 줄바꿈으로 구분하겠음.
"""


print(((A+B)%C),((A%C) + (B%C))%C,(A*B)%C,((A%C) * (B%C))%C, sep='\n')
# math 모듈 포함
import math

# 넓이를 구하는 프로그램
                                 
#get_area() 함수 정의
# def 함수명 ( 매개변수 ):
def get_area( r ):
    # (원의 넓이) = (원주율) * (반지름)^2
    area = math.pi * math.pow(r, 2)
    return area 

# 파이썬에서는 코드블록(영역)을 들여쓰기로 구분한다.

#반지름
r = 4
# 함수 호출 : 함수명( 전달인자 )
area = get_area(r)
print('area : ', area)  
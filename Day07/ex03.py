'''
시퀀스 내장 함수

1. enumerate()함수
   : 리스트와 함께 사용하여,
     (index, 튜플)의 형태로 반환하는 함수
    ex) for item in enumerate( ['a','b','c'] )
          print(item)
        (결과)
        (0, 'a')
        (1, 'b')
        (2, 'c')
        
2. range() 함수
    : 전달받은 값에 따라서 특정 범위에 데이터를 반환하는 함수
    
    i) range(끝)
    : 0부터 끝에 지정한 번화까지 정수를 생성
    ii) range(시작, 끝)
    : 시작부터 끝 사이의 모든 정수를 생성
    iii) range(시작, 끝, 단계)
    : 시작부터 끝 사이 수들을 단계의 크기만큼 생성
'''
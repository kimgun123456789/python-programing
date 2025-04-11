def read_single_digit(a):
    if a==1:
        return '일'
    elif a==2:
        return "이"
    elif a==3:
        return '삼'
    elif a==4:
        return '사'
    elif a==5:
        return '오'
    elif a==6:
        return '육'
    elif a==7:
        return '칠'
    elif a==8:
        return '팔'
    elif a==9:
        return '구'
    else:
        return '영'
def read_number(integer):
    a=integer//100#첫번쨰 자리 수
    b=integer-a*100
    b=b//10
    c=integer-a*100-b*10
    print(read_single_digit(a),read_single_digit(b),read_single_digit(c))

integer=int(input('세자리 정수 입력'))
read_single_digit(integer)

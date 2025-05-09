def buy(a):
    item=input('상품명?')
    if item == '':
        return False
    num=int(input('개수?'))
    a[item] = num
    print(f'장바구니에 {item}이 {num}개 담겼습니다.')

def shoW(a):
    print(f'>>> 장바구니 보기 :{a}')

def find(a):
    b=input('장바구니에서 확인하고자 하는 상품은?')
    if b in a:
        print(f'{b}은(는) {a.get(b)}개 있습니다.')
    else:
        print(f'장바구니에 {b}은(는) 없습니다.')


shoppint_bag= {}
while True:
    if buy(shoppint_bag) == False:
        break
shoW(shoppint_bag)
find(shoppint_bag)

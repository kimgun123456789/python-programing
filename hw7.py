shopping_bag={}
while True:
    item=input('상품명?')
    if item == '':
        break
    num=input('개수?')
    shopping_bag[item] = num

    print('장바구니에 {0}가(이){1}개 담겼습니다.'.format(item,num))


print('>>>장바구니 보기:',shopping_bag)

print('[검색]')
a=input('장바구니에서 확인하고자 하는 상품은?')
print(f'{a}은(는) {shopping_bag.get(a)}개 담겨 있습니다.')

def get_fixed_price(discount,price):
    price=price/(1-(discount/100))
    return price

    
disco=int(input("할인율은?"))
awon=int(input("A상품의 할인된 가격은?"))
bwon=int(input("B상품의 할인된 가격은?"))
print('A상품의 정가는',get_fixed_price(disco,awon),'원')
print('B상품의 정가는',get_fixed_price(disco,bwon),'원')

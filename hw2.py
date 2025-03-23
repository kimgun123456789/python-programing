def exchange(n):
  bigwon = n//500
  n=n%500
  middlewon=n//100
  n=n%100
  smallwon=n//50
  n=n%50
  msmallwon=n//10
  print('500원 동전의 개수:',bigwon)
  print('100원 동전의 개수:',middlewon)
  print('50원 동전의 개수:',smallwon)
  print('10원 동전의 개수:',msmallwon)


def get_integer(prompt):
  res=int(input(prompt))
  return res

result=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(result)

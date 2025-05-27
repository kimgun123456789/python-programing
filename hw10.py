
lst=[]
def input_score():
    num=1
    while True:
        a=int(input(f'#{num}?'))
        if a>=0:
            lst.append(a)
            num+=1
        else:
            break

    return lst

def get_average(a):
    average=0
    for i in range(len(a)):
        average+=a[i]
    average=average/len(a)
    return average

import pickle
import os
if os.path.exists('data/score.bin')==False:
    print('[점수 입력]')
    print('개인점수:',end='')
    scores=input_score()
    with open('data/score.bin','wb') as file:
        pickle.dump(lst,file)

if os.path.exists('data/score.bin') == True:
    with open('data/score.bin','rb') as file:
        print('\n[점수 출력]')
        print('개인점수 :',end='')
        a=pickle.load(file)
        print(a)
        print(f'평균 : {get_average(a):.2f}')

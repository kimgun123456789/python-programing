def draw_line_string(msg1):
    msg2='Welcome to Seoul'
    msg1='hello' + msg1
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2) 
    nstr+=2
    print(nstr*'-')
    print('',msg1)
    print('',msg2)
    print(nstr*'-')



msg1=input('input his/her name :')
draw_line_string(msg1)

sir = 40

def riadok(n,ret):
    ph = (n - len(ret))//2
    if ph%2==1:
        pph = ph + 1
    else:
        pph = ph
    print('*'*pph,end='')
    print(ret, end='')
    print('*'* ph,end='\n')

riadok(sir, 'Ján Botto')

pri_valor = int(input('Primeiro valor: '))
seg_valor = int(input('segundo valor: '))
ter_valor = int(input('terceiro valor: '))

if pri_valor < seg_valor and pri_valor <  ter_valor:
    print(f'o menor número digitado foi {pri_valor}')
if pri_valor > seg_valor and pri_valor > ter_valor:
    print(f'o maior número digitado foi {pri_valor}')

if seg_valor < pri_valor and seg_valor < ter_valor:
    print(f'o menor número digitado foi {seg_valor}')
if seg_valor > pri_valor and seg_valor > ter_valor:
    print(f'o maior número digitado foi {seg_valor}')

if ter_valor < pri_valor and ter_valor < seg_valor:
    print(f'o menor número digitado foi {ter_valor}')
if ter_valor > pri_valor and pri_valor > seg_valor:
    print(f'o m número digitado foi {ter_valor}')

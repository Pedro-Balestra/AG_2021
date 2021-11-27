from sympy import Symbol, solve

matricula = 1715
c = matricula % 10

V1 = 3*(c+1)
V2 = 6*(c+1)
V3 = 2*(c+1)

I1 = Symbol('I1')
I2 = Symbol('I2')
I3 = Symbol('I3')


def malha1(I1, I2):
    return(-V1+15*I1+V2+5*I2)


def malha2(I2, I3):
    return(-5*I2+V2+10*I3-V3)


def lei_kirchoff(I1, I2, I3):
    return I1-I2-I3


m1 = malha1(I1, I2)
m2 = malha2(I2, I3)
lk = lei_kirchoff(I1, I2, I3)

resultado = solve((m1, m2, lk))

print('\n')
print('As correntes encontras no circuito foram: ')
for chave, valor in resultado.items():
    print(f'{chave} = {valor/10**3} A')

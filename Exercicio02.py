from sympy import Derivative, Integral, cos, Symbol
from math import pi

matricula = 1715
c = matricula % 10
frequencia = 5
amplitude = 0.05

# omega
w = ((2*pi)*frequencia)

t = Symbol('t')

# função auxiliar


def função(amplitude, t, c, w):
    return(amplitude*w*cos((w*t)-c))


deslocamento = Derivative(função(amplitude, t, c, w), t).doit()
aceleração = Integral(função(amplitude, t, c, w), t).doit()
aceleração_t = Derivative(função(amplitude, t, c, w), t).doit().subs({t: 4})

print('\n')
print(f'Equação do delocamento: {deslocamento}')
print('\n')
print(f'Equação da aceleração: {aceleração}')
print('\n')
print(f'Equação da aceleração no instante t = 4: {aceleração_t}')
print('\n')

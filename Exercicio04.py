from sympy import Symbol, solve

matricula = 1551
c = matricula % 10

V1 = 3*(c+1)
V2 = 6*(c+1)
V3 = 2*(c+1)

I1 = Symbol('I1')
I2 = Symbol('I2')
I3 = Symbol('I3')


def malha1(I3, I2):
    return(5*I2)


def malha2(I2, I3):
    return

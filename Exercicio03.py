from sympy import Integral, Symbol

matricula = 1715
c = matricula % 10

x = Symbol('x')

trabalho = Integral(((x**(2/3)) + (3 * (x**2)) + (2*x) - c), (x, 0, 6)).doit()

print('\n')
print(f'Trabalho realizado pra x ente a 0 e 6 é de: {trabalho} Joules')
print('\n')

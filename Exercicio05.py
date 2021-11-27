from sympy import Symbol, solve, tan

matricula = 1715
c = matricula % 10

x = Symbol('x')


def funcao1(x):
    return 2**x + 2**(4*x) - c - 1


resultuado1 = solve(funcao1(x))


def funcao2(x):
    return 5*(x**0.5) + 4*(x**2) + (x/2) - c


resultuado2 = solve(funcao2(x))


def funcao3(x):
    return (3 * tan((c-3)*x) + 2)**2


resultuado3 = solve(funcao3(x))

print('\n')
print(f'Valor de x na equação 1 é: {resultuado1}')
print(f'Valor de x na equação 2 é: {resultuado2}')
print(f'Valor de x na equação 3 é: {resultuado3}')
print('\n')

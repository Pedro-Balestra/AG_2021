from sympy import Limit, Symbol, S

matricula = 1715
c = matricula % 10

x = Symbol('x')

print('\n')
print(f'========= Resultado dos valores de x =========')
print('\n')

função1 = (((c+1) - x**0.5)/((c+1)**2 - x))
print(
    f'O resultado de x tendendo a {c+1} para a primeira função é: {Limit(função1,x,(c+1)).doit()}')

função2 = (((c+1) - x**0.5)/((c+1)**2 - x))
print(
    f'O resultado de x tendendo a {S.Infinity} para a segunda função é: {Limit(função2,x,S.Infinity).doit()}')

função3 = (((c+1) - x**0.5)/((c+1)**2 - x))
print(
    f'O resultado de x para tendendo a {-S.Infinity} a terceira função é: {Limit(função3,x,-S.Infinity).doit()}')

print('\n')

from scipy.optimize import linprog
from numpy import multiply

# Função objetiva
c = [2, 4, 1.5, 1]
# Restrições técnicas
A = [[2, 2, 10, 20], [50, 20, 10, 30], [80, 70, 10, 80]]
# Restrições técnicas maior, igual, menor num depois
B = [11, 70, 250]

c = multiply(c, -1)
# A[1] = multiply(A[1], -1)
# B[1] = multiply(B[1], -1)

x = (0, None)

resultado = linprog(c, A, B, bounds=(x))

if resultado.status == 0:
    print("\nX1 = " + str(resultado.x[0]))
    print("\nX2 = " + str(resultado.x[1]))
    print("\nX3 = " + str(resultado.x[2]))
    print("\nX4 = " + str(resultado.x[3]))
    print("\nX5 = " + str(resultado.slack[0]))
    print("\nX6 = " + str(resultado.slack[1]))
    print("\nX7 = " + str(resultado.slack[2]))
    print("\nZ = " + str(resultado.fun).replace("-", ""))
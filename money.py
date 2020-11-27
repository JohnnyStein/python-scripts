n = float(input("Money: "))
notas = [200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 1.00, 0.50, 0.25, 0.10, 0.01]
for nota in notas:
    print("{:.0f} notas de {} R$".format(n // float(nota), nota))
    n %= nota
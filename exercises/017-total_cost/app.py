# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    centavos = (d * 100 + c) * n
    total_dolares = centavos // 100
    total_centavos = centavos % 100
    return (total_dolares, total_centavos)


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))

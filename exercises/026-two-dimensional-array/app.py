# Your code here
def two_dimensional_list(x, y):
    result = [[ i * j for j in range(y)] for i in range (x)]
    print(result)
two_dimensional_list(3, 5)
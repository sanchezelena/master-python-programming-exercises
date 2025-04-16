# Your code here
def all_digits_even(digit):
    return all(int(d) % 2 == 0 for d in str(digit))

print(",".join(str(num) for num in range(1000, 3001) if all_digits_even(num)))
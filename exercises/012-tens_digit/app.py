# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  tens = (num // 10) % 10
  return tens


# Invoke the function with any integer
print(tens_digit(1234))

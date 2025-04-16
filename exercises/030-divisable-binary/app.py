# Your code here
def divisible_binary(binary_sequence):
    binaries = binary_sequence.split(",")
    decimal = [binary for binary in binaries if int(binary, 2)% 5 == 0]
    return ','.join(decimal)

print(divisible_binary("0100,0011,1010,1001"))



    

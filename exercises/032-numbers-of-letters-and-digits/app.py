# Your code here
def letters_and_digits(oracion):
    count = {"LETTERS": 0, "DIGITS": 0}
    for char in oracion: 
        if char.isalpha():
            count["LETTERS"] += 1
        elif char.isdigit():
            count["DIGITS"] += 1
    
    return f"LETTERS {count['LETTERS']}\nDIGITS {count['DIGITS']}"
print(letters_and_digits("hello world! 123"))
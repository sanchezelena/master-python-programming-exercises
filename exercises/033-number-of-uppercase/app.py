# Your code here
def number_of_uppercase(sentence):
    calcul = {"UPPERCASE": 0, "LOWERCASE": 0}
    for letter in sentence:
        if letter.isupper():
            calcul["UPPERCASE"] += 1
        elif letter.islower():
            calcul["LOWERCASE"] += 1
        
    return f"UPPERCASE {calcul['UPPERCASE']}\nLOWERCASE {calcul['LOWERCASE']}"
print(number_of_uppercase("Hello world!"))


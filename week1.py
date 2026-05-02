has_upper = False
has_digit = False
has_symbol = False
conditions = 0

password = input("Please enter your password: ")

length = len(password)
    
for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit =True
    if not char.isalnum():
        has_symbol = True
        
if has_upper:
    conditions += 1

if has_digit:
    conditions += 1
    
if has_symbol:
    conditions += 1

if length > 10 and conditions == 3:
    print("Strong Password")
elif length >= 6 and conditions >= 2:
    print("Medium Password")
else:
    print("Weak Password")

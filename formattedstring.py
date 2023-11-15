# the f string enables {} to be used to place placeholders of variable in between strings

def bill(name, amount, duedate):                    
    print(f"Hello{name}")                   #f is placed before the quotation marks
    print(f"yout bill is {amount}")
    print(f"you should pay the amount before {duedate}")

bill("caleb","2000","december")


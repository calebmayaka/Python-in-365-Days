def fun(name1):
    print("happy birthday: " +name1)
    
fun("caleb")                        #calling them separately
fun("mayaka")
fun("ombogo")

def bill(name, amount, duedate):                    # the f string enables {} to be used to place placeholders of variable in between strings
    print(f"Hello{name}")
    print(f"yout bill is {amount}")
    print(f"you should pay the amount before {duedate}")

bill("caleb","2000","december")
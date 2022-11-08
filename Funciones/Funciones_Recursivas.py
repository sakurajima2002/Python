

def cuenta_regresiva(num):
    if num>0:
        print(num)
        cuenta_regresiva(num -1)
    else:
        print("Boooom")

cuenta_regresiva(10)

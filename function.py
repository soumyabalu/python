x = "awsome"   # declaring variable x as global variable
def getValue():  # defining function using def keyword followed by function name
    global X  # declaring a variable as global
    X = "nice"   # declaring local variable whose scope is within the function only or where it is created

    print("soumya is", X)
    print("Ardra is", x)

getValue()   # calling the function name to excecute the process






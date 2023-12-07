Var = int(input("Add the Variable number "))

def add(num1):
    
    return(num1 + Var,Var)
    
def main():
    n1 = int(input("Add number 1 "))
    n2 = int(input("Add number 2 " ))
    num1 = add(n1+n2)

    print("Sum:",num1)
    print("Global",Var)

if __name__ == "__main__":
    main()
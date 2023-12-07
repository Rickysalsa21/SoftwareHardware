Var = 42

def ask_me():
    num = int(input("Enter number:"))
    return (num)
def add(num):
    return(num + Var)
def main():
    num1 = ask_me()
    num2 = ask_me()

    sum = add(num1+num2)
    Var = sum
    

    print("Sum;",sum)
    print("Global",Var)
if __name__ == "__main__":
    main()
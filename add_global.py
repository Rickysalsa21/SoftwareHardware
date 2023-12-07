Var = 42
def add(num):
    return(num+ Var)
def main():
    print("Please insert a number")
    number = add(int(input()))
    print("Sum",number,"is  a whole number")
if __name__ == "__main__":
    main()
def main():


    print("This program adds two nums")

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number"))
    total = num1 + num2
    
    myDict = {"name": "John", "country": "Norway"}
    mySeparator = "TEST"

    x = mySeparator.join(myDict)

    print(x)
if __name__ == "__main__":
    main()
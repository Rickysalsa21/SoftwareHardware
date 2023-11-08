def meal_test(answer):
    if answer == 1:
        print("Fried Chicken Yummy!")
    elif answer == 2:
        print("BUrgeer")
    elif answer == 3:
        print("Pizza Pizza")
    else:
        print("That is not an option")
def main():
    print("Which is your favorite meal? \nInput a number")
    print("1. Chicken")
    print("2. Burger")
    print("3. Pizza")
    answer = input()
    meal_test(int(answer))
if __name__ == "__main__":
    main()
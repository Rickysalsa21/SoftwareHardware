def while_counter(num):
    while num>=0:
        print (num)
        num -=1
def for_counter(num):
    
    for num in range(num,-1,-1):
        print(num)
        


def main():
    print("Please insert number")
    counter = int(input())
    print()
    while_counter(counter)
    print()
    for_counter(counter)

if __name__ == "__main__":
    main()
    
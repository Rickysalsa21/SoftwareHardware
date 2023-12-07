def display_menu():
    fruit = {
        "A":"Apple",
        "B": "Bannana",
        "C" : "Cherry",
        "D" : "Refresh choices"
        
    }

    
    for key in fruit.keys():
        print(key ,":" ,fruit[key])

    
    
    usrchoice = input("Choose the letter corresponding with the fruit ")
    getfruit = fruit.get(usrchoice.upper())
    parser = usrchoice.upper()
   
    if(parser == "D"):
        print("Refreshing options")
        fruit["A"] = "Orange"
        fruit["B"] = "Pear"
        fruit["C"] = "Grapes"
        fruit["D"] = "No more options"
        for key in fruit.keys():
            print(key ,":" ,fruit[key])
        usrchoice = input("Choose the letter corresponding with the fruit ")
        getfruit = fruit.get(usrchoice.upper())
        parser= usrchoice.upper()
        if(parser!= "D" and getfruit != "None"):
            print("You choose " ,getfruit, " Enjoy")
        else:
            print("Sorry there is no more fruits")
    elif(parser!= "D"):
        print("You choose " , getfruit, " Enjoy")

    elif(parser == "None"):
        return main()
        
            





    else:
        print("Wrong option try again")
        main()


def main():
    display_menu()

if __name__ == "__main__":
    main()

def display_menu():
    global fruit     
    fruit = {
        "1":"Apple",
        "2": "Bannana",
        "3" : "Cherry",
        "X" : "Choose your own fruit"
        
    }


    for items,values in fruit.items():
        print(items + "." + values.capitalize())
    return fruit


def main():
    
    menu_dict = 
    display_menu()
    sel = input("Enter:").upper()
    next_last_key = list(fruit)[-2]
    last_key = list(fruit)[-1]
    if sel == 'X':
        new_sel = input("What do you like?")
        new_key = int(next_last_key)+1
        del fruit[last_key]
        print(new_sel + "added to menu")
        runMe =True
        while runMe:
            keepRun = int(input("Insert -1 to stop 1 to keep running"))
            if keepRun == 1:
                return menu_dict()
                
            elif keepRun == -1:
                print("Stopping")
                runMe = False
            else:
                print("Invalid answer Stopping")
                runMe = False
    else:
        print("Great choice I love", fruit[sel],"its so good")
        


if __name__ == "__main__":
    main()
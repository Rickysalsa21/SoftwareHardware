def display_menu():
    fruit = {
        "1":"Apple",
        "2": "Bannana",
        "3" : "Cherry",
        "X" : "Choose your own fruit"
        
    }

    
    for key in fruit.keys():
        print(key ,":" ,fruit[key])

        
            
    
    
    usrchoice = input("Choose the letter corresponding with the fruit ")
    getfruit = fruit.get(usrchoice.upper())
    parser = usrchoice.upper()
   
    if(parser == "X"):
        fruit_adder()
        



    elif(parser!= "X"):
        print("You choose " , getfruit, " Enjoy")

    elif(parser == "None"):
        return main()
        
            





    else:
        print("Wrong option try again")
        main()


def main():
    display_menu()\
    
def fruit_adder():
    
    looper = "Hello"
    fruit = {
        "1":"Apple",
        "2": "Bannana",
        "3" : "Cherry",
        "X" : "Choose your own fruit"
        
    }
    

    for i in looper:
        newfruit1 =input("Choose your own fruit ")
        items = list(fruit.items())
        
        
        adder =1 
        

        order = 3 + adder
        
        typecon = str(order)
        for i in looper:
            if typecon in fruit:
                order +=1 
                typecon = str(order)
                break
            else:
                break
        
        items.insert(-1,(typecon,newfruit1))
        fruit = dict(items)
        print(fruit)
        choice = int(input("Insert -1 if you want to stop 1 if you want to add another fruit"))
        if(choice == -1):
            break
        elif(choice == 1):
            adder+=1
            return fruit_adder()
        else:
            print("This is an invalid option stopping")
            break
    

if __name__ == "__main__":
    main()

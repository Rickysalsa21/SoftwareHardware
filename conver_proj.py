

def converter():
    print("Choose which type of conversion you would like to use")
    #Prints a question to the user
    print("(1) binary to decimal\n(2) decimal to binary")
    #Presents the option
    choice = int(input(""))
    #User chooses what type of conversion
    if(choice) == 1:
        #This is binary to decimal
        print("Please input the binary number")
        bi = (input())
        #bi == the users input
        y = 0
        # going to be used to navigate through bi
        x = 0
        #going to be used for final output
        for i in bi:
            #I use the for loop to run the loop for how long the user input is
            
            if(i == "1"):
                # the if statement checks each int to see when  
                x += pow(2,int(len(bi)) - y -1)
                y += 1
                
            elif(i == "0"):
                y +=1
                continue
            else:
                print("this number isn't binary")
                break
        print(str(x) + " is the decimal version" )   
                
                   


    elif(choice) == 2:
        print("Please insert decimal number")
        
        dec = int(input())
        ls = []
        if dec > 0:
            while dec > 0:
            

                rem =dec % 2
                ls.insert(0,str(rem))
        
            
                dec = dec // 2 
            ant = ""
            for l in ls:
                ant = ant +""+l
            print(ant + " this is the binary version")
            
        elif dec == 0:
            print ("0 is the binary version")
        else:
            print("This is not a decimal number")
                
            

            
        


    else:
        print("this is an  invalid choice")

        

if __name__ == "__main__":
    converter()
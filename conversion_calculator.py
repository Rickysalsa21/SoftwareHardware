#Ricardo Arias program to convert decimal to binary and binary to decimal
#Created 


def binary():
    print("Please input the binary number")
    bi = ((input()))
        #bi == the users input
    y = 0
        # going to be used to navigate through bi
    x = 0
        #going to be used for final output
    for i in bi:
        if(i == "1" or i == "0"):
         #I use the for loop to run the loop for how long the user input is
            if(i=="1"):
        
                # the if statement checks when iterating through the number to see if it is equal to one
                x += pow(2,int(len(bi)) - y -1)
            #When the part of the binary num is 1 it then sees the length and creates a number based on the power of 2 and adds it to the base number
                y += 1
            #This makes sure that the length is becoming less everytime as the number parses from the left
                
            elif(i == "0"):
                y +=1

                continue
        #Will continue code if the number iterated through is 0 and add 1 to y so the length is lower by one
            else:
                print("this number isn't binary")

                break
        #Will stop loop if number inserted isn't binary.
    
    
            
        else: 
            print("invalid selection")
            return binary()
    print(str(x) + " is the decimal version" )
    usrchoice =int(input("Type in -1 to quit or type 1 to go back to menu "))
    if(usrchoice == 1):
        return converter()  
    elif(usrchoice == -1):
        print("Thank you for using the converter")
    else:
        print("No choice was taken")
        print("Thank you for using the converter")
        
      
            
def decimal():
    print("Please insert decimal number")
    
    
    
    dec = input()
    if int(dec.isdigit()):
        dec = int(dec)
        ls = []
    #I create a list to seperate eac number given by the binary
        if dec > 0:
            while dec > 0:
            

                rem =dec % 2
            # gets the remainder of the number divided by 2 
                ls.insert(0,str(rem))
            #Inserts this number to a list which will be converted into a number of binary
        
        
                dec = dec // 2 
            #makes sure the number get divided by 2 and turns into the next number for the loop
            ant = ""
            for l in ls:
            #just adds all the numbers into one string with no spaces
                ant = ant +""+l
            print(ant + " this is the binary version")
            
        elif dec == 0:
            print ("0 is the binary version")
        else:
            print("This is not a decimal number")
        usrchoice =int(input("Type in -1 to quit or type 1 to go back to menu "))
        if(usrchoice == 1):
            return converter()  
        elif(usrchoice == -1):
            print("Thank you for using the converter")
        else:
            print("Invalid choice was taken")
            print("Thank you for using the converter")
    else:
        print("invalid selection try again")
        return decimal()
    
        
    
                
def converter():
    print("Choose which type of conversion you would like to use")
    #Prints a question to the user
    print("(1) binary to decimal\n(2) decimal to binary")
    #Presents the option
    choice = int(input(""))
    #User chooses what type of conversion
    if(choice) == 1:
        #This is binary to decimal
        binary()
          
                 
        


    elif(choice) == 2:
        #Decimal to binary
        decimal()
        
            

            
        


    else:
        print("This is an  invalid choice\nTry again")
        
        converter()
        

if __name__ == "__main__":
    converter()
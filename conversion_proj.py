print("Choose the following conversion with the type of conversion following with the number")
print("(1) binary to decimal \n (2) decimal to binary")
choice = int(input())
def converter():
    if(choice) == 1:
        print("Please input the binary number")
        bi = (input())
        y = 0
        
        if (str(bi[y])== "1"):
            
            x = pow(2,int(len(bi))- 1)
            print(x)
            y += 1
            if(str(bi[y]) == "1"):
                x += pow(2,(int(len(bi))) - y - 1)
                print(x)
                y += 1
            
                if(str(bi[y]) == "1"):
                    x += pow(2,(int(len(bi))) - y - 1)
                    print(x)
    elif(choice) == 2:
        print("Please insert decimal number")


        

if __name__ == "__main__":
    converter()
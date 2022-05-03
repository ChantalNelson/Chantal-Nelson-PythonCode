#Auhtor: Chantal Nelson
#Date Created: 28/4/2022
#Course: ITT103
#Purpose:<To calualte the commission earned by salesperson based on sales received and which class they belong to.Display a error message if user submits invalid class>

salesprsn_idnumber = int(input("Enter salesperson ID number: "))
sales_amnt = int(input("Enter sales amount: "))
Class = int(input("Enter your class: "))


if Class == 1: #If class is 1

        if sales_amnt <= 1000: #If sale amount less than or equal to 1000
                comission = (6 * sales_amnt)/100 #6% comission 

        elif sales_amnt > 1000 and sales_amnt < 2000: #If sale amount is greater than 1000 but less than #2000
                                                                                         
            comission = (7 * sales_amnt)/100 #7% comission

        else:
                comission = (10 * sales_amnt)/100 #10% comission

elif Class == 2: #If class is 2
        #Same conditions as above, only the comission percentage is different
        if sales_amnt < 1000:
                comission = (4 * sales_amnt)/100

        else:
                comission = (6 * sales_amnt)/100

elif Class == 3: #If class is 3
        comission = (4.5 * sales_amnt)/100

else:#If any invalid class is entered
        print("Invalid Class entered")

print(comission)

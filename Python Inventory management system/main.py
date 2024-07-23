import read 
import Write
import Operation
import datetime
import random

def main():
    """This function ask user to sell, buy or purches ."""
    read.my_header()
    main_loop = True
    while main_loop :

        print("Select your Options to continue")
        print("press 1 to Purchase ")
        print("print 2 for Sell ")
        print("Press 3 for Exit ")
        print("------------------------------------------------------------------------------------------------------------------")
        number1= True
        while number1:
            try:#Applying Exception Handeling to handel error.
                input_= int(input("Enter the option to Continue: "))
            #Except Value Error and suitable message .
            except ValueError as e:
                print("Enter a numeric value")
            else:
                number1=False
        print("\n")
        #This loop is for purchase.
        if input_ == 1:
            read.display()
            print("------------------------------------------------------------------------------------------------------------------")
            stringloop=True
            while stringloop:
                user_name = str(input("Enter your Name : "))
                try:
                    if user_name.isalpha():
                        break
                    else:
                        raise ValueError("please give string value to continue")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop = False
            dict = read.myfun1()
            list=[]# A list is decleared to store values .
            loop = True
            while loop == True:
                test= True
                while test:
                    try:
                        laptop_id=int(input("Which Id laptop do you want to buy :  "))
                    except ValueError:
                        print("Enter a numeric value")
                    else:
                        if 0<laptop_id<len(dict):
                            test=False
                
                quantity_of_laptop=Operation.quantity_validation(dict,laptop_id,input_)
                dict=Operation.dictonary_update_purchase(quantity_of_laptop,list,laptop_id)                             
                Write.update_text(dict)
                loop_1 = True
                while loop_1:
                    ask_again= str(input("Do you want to buy again : "))
                    print("-----------------------------------------------------------------------")
                    if ask_again =='y':
                        loop_1=False
                        loop = True
                    elif ask_again == 'n':
                        loop_1= False
                        loop= False
                    else:
                        print("Inappropriate value")
            ("---------------------------------------------------------------------------------------------------------------------------------------")
            bill_no= random.randint(1000,9999999)
            date=datetime.datetime.now().strftime(" %Y-%m-%d")
            time=datetime.datetime.now().strftime(" %I:%M:%S %p")
            Write.biil_for_purches(time,list,date,bill_no,user_name)
            Write.bill_text_purches(date,time,user_name,bill_no,list)
            print("\n")
            print("Thankyou for you colobration.")
            ("---------------------------------------------------------------------------------------------------------------------------------------")

        #This loop is for sell.    
        elif input_==2:
            read.display()
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            loop = True
            stringloop=True
            while stringloop:
                user_name = str(input("Enter your Name : "))
                try:
                    if user_name.isalpha():
                        break
                    else:
                        raise ValueError("please give string value to continue")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop = False
            stringloop1=True
            while stringloop1:
                address = str(input("Enter your address: "))
                try:        
                    if address.isalpha():
                        break
                    else:
                        raise ValueError("The string contains non-alphabetical characters.")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop1 = False
            numloop= True
            while numloop:
                    try:
                        contact_num=int(input("enter your contact number: "))
                    except ValueError:
                        print("Enter a numeric value")
                    else:
                        numloop=False
            #Create list to store value 
            list = []
            while loop:
                check = True
                validate= True
                dict=read.myfun1()
                while validate:
                    laptop_id=Operation.validation_lp_num(dict)
                    print(f"Available stocks {dict[laptop_id][3]} only")
                    if int(dict[laptop_id][3]) == 0 :
                        print("No stocks")
                        loop_1= True
                        while loop_1:
                            ask_again= str(input("Do you want to buy again : "))
                            if ask_again =='y':
                                loop_1=False
                                validate = True
                            elif ask_again == 'n':
                                loop_1= False
                                validate= False
                                a= False
                            else:
                                print("Inappropriate value")
                    else:
                        validate=False
                if check == False:
                    break
                else:  
                    quantity_of_laptop =Operation.quantity_validation(dict,laptop_id,input_)
                    dict=Operation.dictonary_update_sell(laptop_id,list,quantity_of_laptop)
                    Write.update_text(dict)
                    loop_1= True
                    while loop_1:
                        again= str(input("Do you want to buy again : "))
                        if again =='y':
                            loop_1=False
                            loop = True
                        elif again == 'n':
                            loop_1= False
                            loop= False
                        else:
                            print("Inappropriate value")
            if len(dict)!=0:
                ("---------------------------------------------------------------------------------------------------------------------------------------")
                bill_no= random.randint(0,500)
                date=datetime.datetime.now().strftime("%Y-%m-%d")
                time=datetime.datetime.now().strftime("%H:%M:%S")
                Write.bill_for_sell(list,address,contact_num,bill_no,date,time,user_name)
                Write.bill_text_for_sell(list,bill_no,date,address,contact_num,time,user_name)
                print("\n")
                print("Thankyou for you colobration.") 
                ("---------------------------------------------------------------------------------------------------------------------------------------")

        elif input_== 3:
            loop = False
            print("Thankyou for you valuable Time ")
            print("\n")
        else:
            print("The option you entered",input_,"is invalid")
            print("\n")
    return input
main() 
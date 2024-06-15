#ATM PROJECT (MY FIRST PROJECT)


def operations():
    bln=20000
    while True:

        print("press 1 for cash deposit ")
        print("press 2 for cash withdraw")
        print(" press 3 to check balance")
        choice=int(input("enter your choice : " ))

        if choice==1:
            deposit=int(input(" enter amount = "))
            bln=deposit+bln
            break
        if choice==2:
            withdraw=int(input(" enter amount = " ))
            if withdraw>bln:
                print("Insufficient balance ", bln)
            else:
                bln=bln-withdraw
                print("now balance = ", bln)
                break

        else:
            print("balance = ", bln)
            break
    return bln        
        
def check_pin(pin,max_chance):
    for i in range(max_chance):
        user_pin=int(input("enter your pin = "))
        if user_pin==pin:
            return True 
    return False
def main():
   
    pin = 1234
    max_chances = 3

    print('********************************************** WELCOME TO Shivani Banks *******************************************************')
    if check_pin(pin, max_chances):
        balance = operations()
if __name__ == "__main__":
    main()


            


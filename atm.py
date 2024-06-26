import time

print("please enter your card ")

time.sleep(5)

password = 12345

pin = int(input("enter your atm pin"))

balance = 10000
if pin == password:
    print("""
          1 == balance
          2 == withdraw balance
          3 == deposit balance
          4 == exit
          """
          )
    try:
        option = int(input("please enter your choise"))
    except:
        print("please enter valid option")
        
    if option == 1:
        print(f"your current balance is {balance}")
        
    if option == 2:
        
        withdraw_amount = int(input("please enter withdraw_amount"))
        
        balance = balance = withdraw_amount
        
        print(f"{withdraw_amount} is debited from your ccount")
        
        print(f"your current balance is {balance}")
        
    if option == 3:
        deposit_amount =int(input("please enter deposit_amount"))
        
        balancee = balance + deposit_amount
        
        print(f"{deposit_amount} is credited to your account")
       
        print(f"your updated balance is {balance}")
      
        
        
                
  
    
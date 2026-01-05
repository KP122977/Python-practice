# W.A.P. that replicates a calculator / Convert this to function/class based script when you learn about them 
 
# #=============> create naive script here

try:
  while True:
    print('caculator Functionalities')
    print('1.Addition')
    print('2.substration')
    print('3.multiplication')
    print('4.division')
    print('5. Exit')
  
  
   
  
    choice=input('enter your choice from functionalities(from 1-5) : ')
    if choice=='5':
        print("Exiting program.")
        break
    
    a=int(input('enter first number : '))
    b=int(input('enter a second number : '))
  
    if choice== '1':
      
        print(f'Addition of {a} + {b} : ',a+b )
      
    elif choice== '2':
      
         print(f'subsstraction of {a} - {b} : ',a-b)
      
    elif choice=='3':
      
        print(f'multiplication of {a}*{b} : ',a*b)
      
    elif choice=='4':
      
        if b<0:
            raise ZeroDivisionError
        print(f'division of {a}/{b} :',a/b)
    
    
    else:
      
        print('please enter valid choice')
      

except ValueError:
    print("enter a valid number")
  
except ZeroDivisionError as e:
    print(e)
    
    




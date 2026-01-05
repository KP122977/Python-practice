 # create naive script here 
 
   
max_size =5
stack =[0]  * max_size
top = -1 
try:
  while True:
    print('Stack Implementations')
    print('1.push')
    print('2.pop')
    print('3.peek')
    print('4.display')
    print('5.Exit')
  
    choice=input('enter your choice from functionalities(from 1-5) : ')
    if choice=='5':
        print("Exiting program.")
        break
    
    if choice == '1':
            if top == max_size - 1:
                raise OverflowError("stack Overflow")
            else:
                try:
                    element=int(input("Enter an element :"))
                    top =top + 1
                    stack[top]=element
                    print("Element pushed successfully")
                except ValueError:
                    print("Please enter only integer value")

            
        
    elif choice == '2':
            if top == -1:
                raise IndexError("Stack Underflow - Empty Stack")
            else:
                popped_element = stack[top]
                top = top - 1
                print("Popped element:", popped_element)
      
    elif choice=='3':
        if len(stack)==0:
            raise IndexError("---Empty stack---")
        else:
            print("Top element of stack : ",stack[-1])
      
    elif choice=='4':
        print(stack)
      
    else:
      
        print('please enter valid choice')
      
except (ValueError, OverflowError, IndexError) as error:
        print("Error:", error)

    
    
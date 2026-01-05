# create function based script here

stack = []
max_size = 5
top=-1
def push(stack, element):
    global top
    if top == max_size - 1:
        raise OverflowError("stack Overflow")
    else:
        top =top + 1
        stack[top]=element
        print("Element pushed successfully")
       

def pop(stack):
    global top
    if top == -1:
        raise IndexError("Stack Underflow - Empty Stack")
    else:
        popped_element = stack[top]
        top = top - 1
        print("Popped element:", popped_element)
        

def peek(stack):
    if len(stack) == 0:
        raise IndexError("Stack is empty")
    return stack[-1]

def display(stack):
    return stack


while True:
    try:
        print('stack Implementations')
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice=input('enter your choice from functionalities(from 1-5) : ')
        
        if choice=='5':
            print("Exiting program.")
            break

        if choice == '1':
            try:
                value = int(input("Enter element to push : "))
                push(stack, value)
                print("Pushed successfully")
            except ValueError:
                print('enter only integer value')
            

        elif choice == '2':
            print("Popped:", pop(stack))

        elif choice == '3':
            print("Top element:", peek(stack))

        elif choice == '4':
            print("Stack:", display(stack))

        else:
            print("Invalid choice")

    except (ValueError, OverflowError, IndexError) as error:
        print("Error:", error)

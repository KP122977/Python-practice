

class Stack:
    def __init__(self, max_size,top):
        self.stack = []
        self.max_size = max_size
        self.top=top

    def push(self, element):
        if self.top == self.max_size - 1:
            raise OverflowError("stack Overflow")
        else:
            try:
                element=input("enter an element : ")
                self.top=self.top + 1
                self.stack[self.top]=element
                print("element pushed successfully")
            except ValueError:
                print("Please enter only integer value")

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack Underflow - Empty Stack")
        else:
            popped_element = self.stack[self.top]
            self.top = self.top - 1
            print("Popped element:", popped_element)
            
    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def display(self):
        return self.stack


stack_obj = Stack(5,-1)

while True:
    try:
        print('Stack Implementations')
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice=input('enter your choice from functionalities(from 1-5) : ')

        if choice == '1':
            try:
                stack_obj.push()
                print("Pushed successfully")
            except ValueError:
                print('enter only integer value')
            

        elif choice == '2':
            print("Popped:", stack_obj.pop())

        elif choice == '3':
            print("Top element:", stack_obj.peek())

        elif choice == '4':
            print("Stack:", stack_obj.display())
        elif choice=='5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice")

    except (ValueError, OverflowError, IndexError) as error:
        print("Error:", error)


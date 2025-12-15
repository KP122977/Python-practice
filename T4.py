# Given a list of numbers, find the maximum and minimum values.

# by inbuilt max,min method
try: 
    elements=int(input("enter number of element you want to add : "))
    list=[]
    for i in range(elements):
        value=int(input("enter a element :"))
        list.append(value)

    maximum=max(list)
    minimum=min(list)

    print('maximum :' ,maximum)
    print('minimum : ',minimum)
except ValueError:
    print("invalid input ,please enter proper input only")


# by loop 
try:
    elements=int(input("enter number of element you want to add : "))
    list=[]
    for i in range(elements):
        value=int(input("enter a element :"))
        list.append(value)
 
    
    else:
        max_val=list[0]
        min_val=list[0]

        for i in list:
            if i>max_val:
                max_val=i
            if i<min_val:
                min_val=i
        
        print('maximum :' ,max_val)
        print('minimum : ',min_val)
except ValueError:
    print("invalid input ,please enter proper input only")
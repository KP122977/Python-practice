# Write a program to check if a number is even or odd
while True:
     num=int(input("enter a number : "))
     if num<0:
         print("enter positive number ")
         continue
     else:
         if num%2==0:
            print(num,"given number is Even")
            break
         else:
            print(num,"given number is Odd")
            break
        
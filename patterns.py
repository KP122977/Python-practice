#===> Question : 1 

"""
*
**
***
****
"""

# num=int(input('enter a number of elements you want :'))
# rows=1
# while rows<=num:
#     columns=1
#     while columns<=rows:
#         print('*',end='')
#         columns+=1
#     print()
#     rows+=1
    
    
# ====> Question : 2

"""
****
***
**
*
"""
# num=int(input('enter a number of elements you want :'))
# rows=num
# while rows>=1:
#     coulmns=1
#     while coulmns<=rows:
#         print('*',end='')
#         coulmns+=1
#     print()
#     rows-=1

# ====> Question : 3

# """
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# """
# num=int(input('enter a number of elements you want :'))
# rows=1
# number=1
# while rows<=n:
#     columns=1
#     while coulumns<=rows:
#         print(number,end=' ')
#         number+=1
#         columns+=1
#     print()
#     rows+=1

# ====> Question : 4

"""
1
1 2
1 2 3
1 2 3 4
"""

# num=int(input('enter a number of elements you want :'))
# rows=1
# number=1
# while rows<=n:
#     columns=1
#     while columns<=rows:
#         print(columns,end=' ')
#         number+=1
#         columns+=1
#     print()
#     rows+=1
    
    
# ====> Question : 5
"""
10 9 8 7
6 5 4
3 2
1
"""
# num=int(input('enter a number of elements you want :'))
# rows=num
# logic=num*(num+1)//2
# while rows>=1:
#     columns=1
#     while columns<=rows:
#         print(logic,end=' ')
#         logic-=1
#         columns+=1
#     print()
#     rows-=1
    

# ====> Question 6 :

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
# num=int(input('enter a number of elements you want :'))
# rows=num

# while rows>=1:
#     columns=rows
#     while columns>=1:
#         print(columns,end=' ')
#         columns-=1
#     print()
#     rows-=1

# ====> Question 7 :

"""
*     *
**   **
*** ***
*******
"""
# try:
#     total_rows = int(input("Enter number of rows: "))

#     current_row = 1

#     while current_row <= total_rows:
        
#         if current_row == total_rows:
#             star_count = 1
#             while star_count <= (2 * total_rows - 1):
#                 print("*", end="")
#                 star_count += 1
#             print()
#             current_row += 1
#             continue

        
#         star_counter = 1
#         while star_counter <= current_row:
#             print("*", end="")
#             star_counter += 1

        
#         space_counter = 1
#         while space_counter <= (2 * (total_rows - current_row) - 1):
#             print(" ", end="")
#             space_counter += 1

       
#         if current_row != total_rows:
#             star_counter = 1
#             while star_counter <= current_row:
#                 print("*", end="")
#                 star_counter += 1

#         print()  
#         current_row += 1

# except ValueError:
#     print("Please enter a valid integer value")
    
    

# =======> Question 8 :
"""
*******
*** ***
**   **
*     *
"""

# try:
#     rows = int(input('Enter number of rows: '))
#     current_row = rows

#     while current_row >= 1:

    
#         if current_row == rows:
#             star_count = 1
#             while star_count <= (2 * rows - 1):
#                 print("*", end="")
#                 star_count += 1
#             print()
#             current_row -= 1
#             continue

    
#         star_count = 1
#         while star_count <= current_row:
#             print("*", end="")
#             star_count += 1


#         space_count = 1
#         while space_count <= (2 * (rows - current_row) - 1):
#             print(" ", end="")
#             space_count += 1

    
#         star_count = 1
#         while star_count <= current_row:
#             print("*", end="")
#             star_count += 1

#         print()
#         current_row -= 1

# except ValueError:
#     print("Please enter a valid integer value")


# ======> Question : 9

"""
*******
*** ***
**   **
*     *
**   **
*** ***
*******
"""

# try:
#     rows = int(input('Enter number of rows: '))
#     current_row = rows

#     while current_row >= 1:

    
#         if current_row == rows:
#             star_count = 1
#             while star_count <= (2 * rows - 1):
#                 print("*", end="")
#                 star_count += 1
#             print()
#             current_row -= 1
#             continue

    
#         star_count = 1
#         while star_count <= current_row:
#             print("*", end="")
#             star_count += 1


#         space_count = 1
#         while space_count <= (2 * (rows - current_row) - 1):
#             print(" ", end="")
#             space_count += 1

    
#         star_count = 1
#         while star_count <= current_row:
#             print("*", end="")
#             star_count += 1

#         print()
#         current_row -= 1
        
#     current_row = 1

#     while current_row <=rows:
        
#         if current_row == rows:
#             star_count = 1
#             while star_count <= (2 *rows - 1):
#                 print("*", end="")
#                 star_count += 1
#             print()
#             current_row += 1
#             continue

        
#         star_counter = 1
#         while star_counter <= current_row:
#             print("*", end="")
#             star_counter += 1

        
#         space_counter = 1
#         while space_counter <= (2 * (rows - current_row) - 1):
#             print(" ", end="")
#             space_counter += 1

       
#         if current_row != rows:
#             star_counter = 1
#             while star_counter <= current_row:
#                 print("*", end="")
#                 star_counter += 1

#         print()  
#         current_row += 1
        
        
        

# except ValueError:
#     print("Please enter a valid integer value")


# =======> Question 10 :

"""
*       *       *
 *     * *     * *
  *   *   *   *   *
   * *     * *     *
    *       *       *
"""

# try :
#     rows=int(input("Enter number of rows : "))
    
#     current_row=1
#     # space_counter=0
    
#     while current_row <=rows:
        
#         if current_row == rows:
#             star_count = 1
#             while star_count <= (2 *rows - 1):
#                 print("*", end="")
#                 star_count += 1
#             print()
#             current_row += 1
#             continue

        
#         star_counter = 1
#         while star_counter <= current_row:
#             print("*", end="")
            

        
#         space_counter = 0
#         while space_counter <= star_counter:
#             print(" ", end="")
#             space_counter += 1

       
#         if current_row != rows:
#             star_counter = 1
#             while star_counter <= current_row:
#                 print("*", end="")
                

#         print()  
#         current_row += 1
    
    
    
# except ValueError:
#     print('Please enter a valid integer value')
    
    
    
rows = 5
current_row = 0

while current_row < rows:

    
    space_count = 0
    while space_count < current_row:
        print(" ", end="")
        space_count += 1

    
    print("*", end="")

    
    space_count = 0
    while space_count < (2 * (rows - current_row) - 3):
        print(" ", end="")
        space_count += 1

    
    print("*", end="")

   
    space_count = 0
    while space_count < (2 * current_row + 1):
        print(" ", end="")
        space_count += 1

  
    print("*")

    current_row += 1

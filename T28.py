# Create a loop that prints all prime numbers between 1 and 50

for i in range(1,51):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        
     
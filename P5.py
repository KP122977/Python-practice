# Given a list of words, find the word with the maximum length and its length

#  by loop

list=['krish','tanish','paraj']
max_list=""
max_len=0
for i in list:
    if len(i)>max_len:
        max_len=len(i)
        max_list=i
        
    else:
        continue
print("maximum len word ",max_list)
print("maximum length ",max_len)



# by inbuilt max method

list=['apple','banana','pineapple']

max_word=max(list)
max_len=len(max_word)

print("maximum len word ",max_word)
print("maximum length ",max_len)
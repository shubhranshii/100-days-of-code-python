
# Write your code above 👆

#print(result)

with open ("file1.txt") as file1:
    list1= file1.readlines()
with open ("file2.txt") as file2:
    list2=file2.readlines()

new_list=[int(num.strip()) for num in list1 if num in list2]
print(new_list)

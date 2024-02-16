#!/usr/bin/env python
# coding: utf-8

# In[21]:


"""
Aiden Thao
2/16/2024
Lab 6 - Dictionaries
"""


# Problem 1
# Create a phone book.

print("When entering a name and number, please enter names with underscores.\n" +
      "For example: Matt_Priem, 507-389-1438. When done, type 'quit'\n")


      
### Your code here ###

phone_book = {}

while True:
    name = input("Enter a name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    if name in phone_book:
        print(f"{name} is already in the phone book.")
        continue
    number = input("Enter a phone number: ")
    phone_book[name] = number

print('Your phone book consists of:')
for name, number in phone_book.items():
    print(f"{name}: {number}")


    
#Problem 2

	#Test1 - Mode = 2
data_set_1 = [3,3,2,2,2,2,4,4,4,14,14]

	# Test2 - Mode = 5
data_set_2 = [
		10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
		4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
		5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
		4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
		6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
		3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
		10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
		7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
	]

	#Test3 - This data set is multimodal.  The modes are 2 and 4.
data_set_3 = [1,2,2,2,3,3,4,4,4,5]

data = data_set_1

### Your code here ###

def mode(data):
    if not data:
        print("The list is empty.")
        return None
    elif len(data) == 1:
        return data[0]

    count_dict = {}
    for num in data:
        if num not in count_dict:
            count_dict[num] = 0
        count_dict[num] += 1

    max_count = max(count_dict.values())
    mode_nums = [num for num, count in count_dict.items() if count == max_count]

    if len(mode_nums) > 1:
        mode_nums = sorted(mode_nums)
    elif len(mode_nums) == 0:
        print("There is no mode.")
    return mode_nums

print("mode to test 1 equals: ", mode(data_set_1))
print("mode to test 2 equals: ", mode(data_set_2))
print("mode to test 3 equals: ", mode(data_set_3))


# In[ ]:





# Chase Stratton
#Assignment List
# 10 Points 
# October 27th 2024
# Creating A list using python code: 

# Starting with Task 1 : Defining a last called my_list with the given item listed for the assignment
my_list = ['apple', 'banana', 'cherry','  date', 'elderberry']
# The list contains specified fruit names

# Starting Task 2 : Printing the third item on my_list using the code below 
third_item = my_list[2] 
print(f"third item in my_list: {third_item}") # Print the third item  

# Starting task 3: Printing the last item on my_list 
last_item = my_list[-1] # Here we are accessing the last item in the my_list nevgating the index system  
print (f"Last item in my_list : {last_item}") #Print last item here.

# Starting Task 4 : We will be using slicing to create a new list with the second, third and forth items.
new_list = my_list[1:4] # Here we'll be slicing the from the second item onto the fourth item (indexing 1 to 3)
print ("New List (2nd, 3rd, 4th items):", new_list) # Printing the new list that was created by slicing.

#  Starting task 5 : Defining a function called count_vowels that count in a list of words 
def count_vowels(words):
    vowels = 'aeiou'  # Defining a string that is containing all vowels characters
    # Using a nested loop to count each vowel in every word in the list 
    total_vowels = sum(1 for word in words for char in word if char.lower() in vowels )
    return total_vowels # Returning the word count vowel total 

# Starting Task 6 : Defining a function called reverse_list that reverses a list without modifying the original list 
def reverse_list (lst): 
    return lst[::-1] # Using the list slicing to reverse the list and return the reverse version of it  

#Task 7 : Defining a function called remove_duplicates to remove duplications in the list 
def remove_duplicates(lst):
    seen, unique_list  = set (), []   # Creating an empty set for teh sen items and another list for the unique items in it.
    # Looping through the list, adding only unseen items on the unique items list.
    for item in lst :
        if item not in seen:
            unique_list.append(item) # the use of Append is to append unique items to the unique item list 
            seen.add(item)   # Seem : marks the item as seen by adding them to a set 
            return unique_list # Returning the list with duplicates removed
        
        # Task 8:  Defining the function called "Remove_items" to remove items form one list list that appear in the others.
def remove_items(lst1, lst2):
    # Using the list comprehension to include only items from lst1 not in lst2.


    # Giving example usages to see the functions outputs 
    print ("Total vowels in my_list:", count_vowels(my_list))  # code: calls count_vowels on my_list and print the results out.

    print("Reversed my_list:",reverse_list(my_list)) # code : calling reverse_list on my_list and printing the results

    print("my_list with duplicates removed:". remove_duplicates(my_list)) # code: calling remove_duplicates on my_list and printing the results.
    print("Items in my_list not in ['banana', 'date']: ", remove_items(my_list, ['banana', 'date]']))
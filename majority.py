# replace ___ with your code

# define a function that returns the majority element
def find_majority_element(num_list):

    # iterate through each number in the list
    for i in num_list:
        print(i)
        
        # check the number of occurrence of each element
        count = num_list.count(i)
        print(count)
        
        # if the number of occurrences is greater than
        # n // 2, where n is the length of the list
        # len(num_list) returns the length of the list
        if count > len(num_list) //2:
            return i



# given list with majority element
numbers = [1, 7, 8, 7, 7, 7]

# call the method with list as an argument
result = find_majority_element(numbers)
print(result)

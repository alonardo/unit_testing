# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

def remove_zeros(array):
    temp_list = []
    # begin error handling 

    if type(array) != list:
        return 'Not a list, try again.'
    
    elif len(array) == 0:
        return 'List is empty, try again.'

    for num in array:
        if type(num) != int:
            return 'This list contains non-integers. Please provide a list that only contains integers.'
            # end error handling

        if num != 0:
            temp_list.append(num)
    
    for num in array:
        if num == 0:
            temp_list.append(num)

    return temp_list
        

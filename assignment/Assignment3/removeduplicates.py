"""
File: removeduplicates.py
-------------------------
This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    """
    This function should ask the user for a series of integer values
    (until the user enters 0 to stop) and store all those values in a
    list.  That list should then be returned by this function.
    """
    new_list = []
    while(True):
        temp = input("Enter value (0 to stop): ")
        temp = int(temp)
        if(temp == 0):
            break
        new_list.append(temp)
    return new_list


def remove_duplicates(num_list):
    """
    This function is passed a list of integers and returns a new
    list with all duplicate values from the original list remove.
    >>> remove_duplicates([1, 2, 3, 2, 3, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates([1, 1, 1])
    [1]
    >>> remove_duplicates([])
    []
    """
    # unique_list = list(dict.fromkeys(num_list))
    # return unique_list
    unique_list = []
    #duyệt qua từng elem trong num_list
    for elem in num_list:
        if(unique_list.count(elem) == 0):
            #đếm xem trong unique_list đã có phần tử elem chưa để thêm vào
            unique_list.append(elem)
    return unique_list

def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

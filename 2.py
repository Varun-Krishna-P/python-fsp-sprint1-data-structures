# function data_oper
def data_oper(string1,string2):
    '''
    Split the string string1 with whitespace as delimiter
    Remove the words that contain characters that are not alphabets
    Remove the words whose length is less than 3
    Convert first letter of each word in to Upper case
    Store it in variable list1
    Type of list1 - List
    '''
    split_list = string1.split()
    
    list1 = []

    for st in split_list:
    	if (len(st) >= 3 and not st.isnumeric()):
    		list1.append(st.capitalize())
    
    
    
    '''
    Split the string string2 with whitespace as delimiter
    Remove the words that contain characters that are not alphabets
    Remove the words whose length is less than 3
    Convert first letter of each word in to Upper case
    Store it in variable list2
    Type of list2 - List
    '''
    split_list2 = string2.split()
    list2 = []

    for st in split_list2:
    	if (len(st) >= 3 and not st.isnumeric()):
    		list2.append(st.capitalize())
    

    
    
    
    
    '''
    Concatinate the lists list1,list2 and store it in variable list3
    Type of list3 - List
    '''
    
    list3 = list1 + list2
    
    
    
    '''
    Find the count of each word in the list list3 and store it in variable count_dictionary
    Type of count_dictionary - Dictionary
    Keys have to be words
    Dictionary must be ordered based on Keys
    '''
    
    
    count_dictionary = {}
    
    for item in list3:
        if item in count_dictionary:
                count_dictionary[item] += 1
        else:
                count_dictionary[item] = 1
    
    
    '''
    Find the unique words from words of list3 and store it in variable list3_uni
    Type of list3_uni - list
    list3_uni must be sorted in ascending order
    '''
    
    
    list3_uni = []

    for item in list3:
        if item not in list3_uni:
            list3_uni.append(item)
    
    
    '''
    Find the common words in list1,list2 and store it in variable common_tuple
    Type of common_tuple - tuple
    Words have to unique and sorted in ascending order
    If there are no common words in list1,list2 store an empty tuple
    '''
    
    common_tuple = ()

    for element in list1:
        if element in list2:
            common_tuple += tuple([element])
    
    
    
    '''
    Find the words of list3 that ends with 's' and store it in variable ends_with
    Type of ends_with - tuple
    Words have to be unique and sorted in ascending order
    If there are no words in list3 that ends with 's', store an empty tuple
    '''
    
    
    ends_with = ()

    for element in list3:
        if (element[-1] == 's'):
            ends_with += tuple([element])
    

    
    print(list3)
    print(count_dictionary)
    print(list3_uni)
    print(common_tuple)
    print(ends_with)


if __name__=='__main__':
    # string1 = input()
    # string2 = input()
    string1 = "A glance at the outline map on page 4 may shows the location of theseancient works."
    string2 = "To begin with the Mounds and Earthworks themselves, it may be said that there are many thousands of them."
    data_oper(string1,string2)


    # string 1: A glance at the outline map on page 4 may shows the location of theseancient works.
    # string 2: To begin with the Mounds and Earthworks themselves, it may be said that there are many thousands of them.

    # string 1: The Effigy Mounds are believed to have represented the totems or clan symbols of their builders.
	# string 2: Most of the Effigy Mounds are found in southern Wisconsin.

	# string 1: No doubt every reader of this booklet would like to take part in the actual digging of a mound.
	# string 2: An exploration party has arrived on the scene and is preparing to examine this ancient earthwork.

	# string 1: We have had a look at the Mound builders
	# string 2: Putting a groove on a Stone Hammer was really a very important among steps

	# string 1: The lower specimen in the picture, known as a Roller Pestle, was used like a modern rolling-pin.
	# string 2: Stone Pestles are rarely found in Mounds

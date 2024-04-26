# program to calculate the sum
# calcualate the sum of floatint point numbers
# finding count of the prime number in the input
# find the minimum integer
# return true if the input number has zero
# basics of python

def return_integer_number(num):
	if (isinstance(num, int)):
		return num

def numbers(num1,num2,num3,num4):
    num_list = []
    float_num_list = []
    
    print(f"num1: {num1}, num2: {num2}, num3: {num3}, num4: {num4}")

    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    num_list.append(num4)
    
    '''
    Find the sum of all the numbers and store it in variable sum_of_numbers
    '''
    
    
    sum_of_numbers = sum(num_list)
    
    
    '''
    Find the sum of float numbers among the numbers and store it in variable sum_of_float_numbers
    '''
    for i in num_list:
    	if (isinstance(i, float)):
    		float_num_list.append(i)
    
    sum_of_float_numbers = sum(float_num_list)
    
    
    '''
    Find the smallest integer number among the numbers and store it in variable min_number
    '''
    int_num_list = []
    for i in num_list:
    	if (isinstance(i, int)):
    		int_num_list.append(i)
    
    int_num_list.sort()    
    min_number = int_num_list[0]
    
    '''
    Find the count of prime numbers among the numbers and store it in variable prime_count
    '''
    prime = []
    for i in num_list:
    	x = 0
    	for j in range(1, int(i)):
    		if i%j == 0:
    			x+=1
    	if x==1:
    		prime.append(i)
    
    prime_count = len(prime)
    
    '''
    Check for zeros. If there are zeros present among the numbers, store True else store False in the variable zero_check
    '''
    
    zero_check =  False
    if (num1 == 0 or num2 == 0 or num3 == 0 or num4 == 0):
    	zero_check = True
 

    print(sum_of_numbers)
    print(sum_of_float_numbers)
    print(min_number)
    print(prime_count)
    print(zero_check)

if __name__ == '__main__':
 	# num1 = 2
 	# num2 = 3.5
 	# num3 = 0
 	# num4 = 1

 	# num1 = 3
 	# num2 = 2.5
 	# num3 = 11
 	# num4 = 5.2

 	# num1 = 5
 	# num2 = 3.4
 	# num3 = 7
 	# num4 = 5

 	# num1 = 8
 	# num2 = 0
 	# num3 = 7.4
 	# num4 = 5.4

 	num1 = 1
 	num2 = 2
 	num3 = 3
 	num4 = 4

 	numbers(num1,num2,num3,num4)
    


    # num1: 2, num2: 3.5, num3: 0, num4: 1
    # num1: 3, num2: 2.5, num3: 11, num4: 5.2
    # num1: 5, num2: 3.4, num3: 7, num4: 5
    # num1: 8, num2: 0, num3: 7.4, num4: 5.4
    # num1: 1, num2: 2, num3: 3, num4: 4


# integers and Floats
# integers or (int) are basically numbers while floating point numbers (floats) are positive and negative real numbers with a fractional part denoted by the decimal symbol

#Declaring of integers and floats

integer_number = 500
float_number = 100.05

#You can carry out various arithmetic operators on floats and integers as shown below

add_operation = integer_number + float_number
print(add_operation)

subtraction_operation = integer_number - float_number
print(subtraction_operation)

multiplication_operation = integer_number * float_number
print(multiplication_operation)

division_operation = integer_number / float_number
print(division_operation)

#You can format your result to a specific data type as shown

print("Integer Output ",int(add_operation))
print("Float Output ",float(add_operation))
print("String Output ",str(add_operation)) 



#We can also carry out mathematical operators like <,>,<=,>= e.t.c

equal_to = integer_number == float_number #prints true if the values are equal
print(equal_to)

greater_than = integer_number > float_number #print true if integer_number is greater than float_number
print(greater_than)

greater_than_or_equal_to = integer_number >= float_number #print true if integer_number is greater than or equals to float_number
print(greater_than_or_equal_to)

less_than = integer_number < float_number #print true if integer_number is less than float_number
print(less_than)

less_than_or_equal_to = integer_number <= float_number #print true if integer_number is less than or equals to float_number
print(less_than_or_equal_to)

not_equal_to = integer_number != float_number #print true if integer_number is not equal to float_number
print(not_equal_to)
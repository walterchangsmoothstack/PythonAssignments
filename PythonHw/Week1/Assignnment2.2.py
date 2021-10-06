
# 1.


items = [1, "word", 3.4]
print(items)

# 2.

nested_items = [1, 1, [1,2]]
print(nested_items[2][1])

# 3.

lst=['a','b','c'] 

#list[1:] will return all the elements of lst starting at index 1 (0 indexed)
print(lst[1:])

# 4.

weekdays = {"Monday" : 1, "Tuesday":2, "Wednesday":4, "Friday":5}

# 5.

D={'k1':[1,2,3]}

#D[k1][1] will find key k1 and return index 1 of that object (list). The value returned will be 2
print(D['k1'][1])

# 6. Yes you can

tuple_object = (1, [2, 3])
print(tuple_object)

# 7.

distinct = set("Mississippi")
print(distinct)

# 8.

distinct.add('X')
print(distinct)

# 9. {1, 2, 3}

print(set([1, 1, 2, 3]))

# 10.

multiples = [x for x in range(2000, 3201) if x%7 == 0 and x%5 != 0]
#print(multiples)

print(",".join([str(x) for x in multiples]))



##########################################
################QUESTION 2################
##########################################

def factorial(number):
    if(number == 0):
        return 1
    return number*factorial(number-1)
print("Input number to factorialize: ")

x = int(input())
print(factorial(x))

##########################################
################QUESTION 3################
##########################################

def squares(number):
    square_dictionary = dict()
    for i in range(1, number+1):
        square_dictionary[i] = [i*i]
    return square_dictionary

print(squares(8))


##########################################
################QUESTION 4################
##########################################

tuple_input = str(input())

tuple_input = tuple(tuple_input.split(','))
print(tuple_input)

##########################################
################QUESTION 5################
##########################################

class printString:
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s =  str(input())

    def toString(self):
        print(self.s.upper())

obj = printString()
obj.getString()
obj.toString()


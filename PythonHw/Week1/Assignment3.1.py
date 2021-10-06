# 1.

multiples = [x for x in range(1500, 2700) if x%7 == 0 and x%5 == 0]
print(multiples)

# 2.

def celsiusToFahrenHeit(degrees):
    return degrees*9/5 + 32
print(celsiusToFahrenHeit(100))

# 3.

def guessNumber(answer):
    while(answer != int(input())):
        print("Guess again")
    print("Correct")

guessNumber(100)

# 4.
pyramid =""
line = ""
for i in range(5):
    line+="*"
    for j in range(i):
        pyramid+="*"
    pyramid+="\n"

pyramid+= line + pyramid[::-1]

print(pyramid)

# 5.
def reverse(word):
    return word[::-1]
print(reverse("dlrow olleh"))

# 6.
def countEvenOdd(numbers):
    count_odd = len([x for x in numbers if x%2 == 1])
    print("Odd numbers = %d" %count_odd)
    print("Even numbers = %d" %(len(numbers)-count_odd))

countEvenOdd([1, 1, 12, 1, 1, 41, 112312, 221, 2, 44444, 32])

# 7.
def printType(items):
    for i in items:
        print(type(i), i)

printType([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])

# 8.
for i in range(6):
    if(i == 3):
        continue
    print(i, end=" ")

    
        

# 1.
hello = "Hello World"
print(hello[8])

# 2.
slice = "thinker"
print(slice[2:5])

#The output of S=’hello’ S[1] is 'e'

# 3. The output of s[2:] is 'mmy'
s = 'Sammy'
print(s[2:])

# 4.
print(set('Mississippi'))

# 5.
def isPalindrome(paragraph):
    words = paragraph.split("\n")
    for i in range(1, len(words)):
        temp = ""
        words[i] = words[i].upper()
        for j in range(len(words[i])):
            if(ord(words[i][j]) >= 65 and ord(words[i][j]) <= 90):
                temp+= words[i][j]
        if temp == temp[::-1]:
            print("y", end=" ")
        else:
            print("n", end=" ")


isPalindrome("""3
Stars
O, a kak Uwakov lil vo kawu kakao!
Some men interpret nine memos
A man, a plan, a canal, Panama
banana""")

#print("is 'A man a plan a canal Panama' a palindrome ", isPalindrome("A man a plan a canal Panama"))
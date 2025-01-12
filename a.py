def is_palindrome(s):
    s1 = s.replace(" ", "").lower() 
    print(s1==s1[::-1])  

inp = input("Enter a string: ")
is_palindrome(inp) 
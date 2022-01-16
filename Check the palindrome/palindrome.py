def IsPalindrome(string):
    string = string.replace(' ', '')
    string_palindrome = string[::-1]
    if string in string_palindrome:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

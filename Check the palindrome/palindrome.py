s = str(input("Enter the string to check the palindrome"))
s = s.replace(' ', '')
palindrome = s[::-1]
if s in palindrome:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

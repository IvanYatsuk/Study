vowels = 'aeiou'
counter = 0
string = str(input().lower())
for i in string:
    if i in vowels:
        counter += 1
print(counter)

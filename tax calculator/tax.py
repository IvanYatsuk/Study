salary = int(input("Enter your mounth salary"))
tax = float(input("Enter mounthly tax")) / 100
change = salary * tax
print("Your salary without tax",salary)
print("Your salary with tax", salary - change)

choose = input("Choose decimal or binary converter").lower()
choose = choose.replace(' ', '')
n = int(input("Enter the number that will convert"))
if choose == "binary":
    print(bin(n))
elif choose == "decimal":
    str_n = str(n)
    printed = 0
    degree = len(str_n) - 1
    for i in str_n:
        result = int(i) * 2 ** degree
        degree = degree - 1
        printed = printed + result
    print(printed)

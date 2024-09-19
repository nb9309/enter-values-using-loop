
lst = []
while (1):
    val = input()
    if  (not val.isalnum()) and (not val.isspace()) and (not val.__contains__('.')) and (not val.startswith('-')):
        break
    else:
        lst.append(val)
print(lst)


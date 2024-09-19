lst = []
while 4:
    val = input()
    if (not val.isalnum()) and (not val.isspace()):
        if val.__contains__('.'):
            lst.append(float(val))
        elif val.startswith('-') and val.__contains__('.'):
            lst.append(val)
        elif val.startswith('-'):
            lst.append(val)
        elif (not val.__contains__('.')):
            break
    else:
        lst.append(val)
print(lst)
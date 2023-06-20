import re

i = input(
    "Enter your choice:\n1. Printing File\n2. Writing in File.\n3. Getting mobile number and mail ID\n")
if i == '1':
    fileptr = open("text1.txt", "rt")
    content1 = fileptr.read()
    fileptr.close()
    print(content1)  # printing the contents of file
if i == '2':
    file = open("txt.1", "a")
    txt = input ("Enter content:-\n")
    file.write("\n\n")
    file.write(txt)
    file.close()
if i == '3':
    print("ALL MAIL ID's")
    pattern = re.compile("[a-z]+\.+[a-z]+[0-9]+@+[a-z]+\.+[a-z]+[a-z]+")
    for line in open("text1.txt"):
        for match in re.finditer(pattern, line):
            print(line)
            break
    print("ALL Phone numbers")
    pat = re.compile("\++[0-9]+[0-9]+")
    for line in open("text1.txt"):
        for match in re.finditer(pat, line):
            print(line)
            break
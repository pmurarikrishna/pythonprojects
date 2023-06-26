import shelve
f = open("text.txt")                #opening file
a=f.read()                           #reading file
password=input("enter password here")   #taking password input
if(password==a):                        #matching password
    s = shelve.open("test")             #opening or creating shelve
    s['name'] = "parth"
    s['age'] = 19
    s['marks'] = 90
    s['address']= "maharastra"
    s['school']= "vit"
    print(s['marks'])
    s['marks']=73                       #updating marks
    print(s['marks'])                   #printing marks
    print(s.get('name'))                #printing value of key name by call get
    print(list(s.items()))              #printing item of shelve
    print(list(s.keys()))               #printing keys of shelve
    print(list(s.values()))             #printing values of shelve

    s.close()
else:                                   #if password doesnt match
    print("incorrect password please try again")
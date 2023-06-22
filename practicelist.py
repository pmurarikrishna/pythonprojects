# mylist0=[1,2,3,4]   # list of integer
# print(mylist0)

# #a list can have diffferent datatypes like

# mylist1=[1,4,7,"krishna"]
# print(mylist1)

# #list indeing
# print(mylist1[3])

# ###listslicing in list

# print(mylist1[0:3])

# # change element in list
# mylist1[3]="vimal"

# # to del list items 
# del mylist1[2]


# #  to insert value in desired location 

# # Demonstration of list insert() method
# odd = [1, 9]
# odd.insert(1,3)

# print(odd)

# odd[2:2] = [5, 7]

# print(odd)

 
 
#  # a list can have nested lis
# mynestedlist=[1,2,7,["krishna",676],"hello"]
# print(mynestedlist)

# # to create a empty list 

mylist3=[]
print(type(mylist3))

# for i in range(0,4):
#     s=input()
#     mylist3.append(s)
#     print(mylist3(s))

for i in range(0,3):
    s=int(input())
    mylist3.append(s)
print("mylist3")
print(mylist3)

for k in mylist3:
  if k==1|8|9|6|0 :
    if k==6:
      print(9)
    if k==9 :
       print (6)
       print (mylist3)

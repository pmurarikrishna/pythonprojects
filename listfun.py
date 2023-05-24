from tkinter import N


mylist=[]
n=int(input())
for i in range (0,n) :
  s=int(input())
  mylist.append(s)
  print(mylist)

# for i in range (len(mylist+1)):
#     sum+=mylist(i)

print("sum of list" ,sum(mylist))

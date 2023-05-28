n=int(input("enter no"))
mylist=[]
n=int(input())
for i in range (0,n) :
  s=int(input(i))
  mylist.append(s)
  
  print(mylist)
  
mylist.insert(0,5)
mylist.insert(1,10)
mylist.insert(0,6)
  
print(mylist)
  
mylist.remove(6)
mylist.append(9)
mylist.append(1)
mylist.sort()
  
print(mylist)
  
mylist.pop()
  
mylist.reverse()
  
print(mylist)

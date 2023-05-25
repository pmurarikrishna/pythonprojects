
  
# multiple inheritance 

class addition:  
    def Summation(self,a,b):  
        return a+b; 

class multiplication:  
    def Multiplication(self,a,b):  
        return a*b;  

class mulinherit(addition,multiplication):  
    def Divide(self,a,b):  
        return a/b; 
         
d =mulinherit()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20)) 


s['address']="bihar"
s['school']="rps"
print(s['marks'])
s['marks']=75
print(s['marks'])
print(s.get('name'))
print(list(s.item()))
print(list(s.values()))
print(list(s.keys()))

s.close()
else:
    print("incorect password")





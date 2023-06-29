# Function to take multiple arguments 

def add(datatype, *args): 
  if datatype =='int': 

        answer = 0


        if datatype =='str': 

            answer ='' 

   

    # Traverse through the arguments 

  for x in args: 
      answer = answer + x 

       print(answer) 

   
# Intege
add('int', 5, 6) 

   
# String 

add('str', 'Hi ', 'krishna')

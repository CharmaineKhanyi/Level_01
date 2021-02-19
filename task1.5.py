def triangle(n):
     
    
    for i in range(0, n):
     
        
        for j in range(0, i+1):
         
           
            print("# ",end="")
      
     
        print("\r")
 

n = 2
triangle(n)
##

n = 4
triangle(n)

##triangle(-4)

row = int(input('Enter number of rows required: '))

for i in range(row,0,-1):
    for j in range(row-i):
        print(' ', end='') # printing space and staying in same line
    
    for j in range(1*i-1):
        print('*',end='') # printing * and staying in same line
    print() # printing new l
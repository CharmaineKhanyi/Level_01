def countList(st1, st2): 
    return [sub[item] for item in range(len(st2)) 
                      for sub in [st1, st2]] 
      
# Driver code 
 st1 = [11, 22, 33] 
 st2 = [1, 2, 3] 
print(countList(st1, st2)) 

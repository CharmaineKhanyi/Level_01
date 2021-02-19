def countList(lst1, lst2): 
    return [sub[item] for item in range(len(lst2)) 
                      for sub in [lst1, lst2]] 
      
# Driver code 
lst1 = [11, 22, 33] 
lst2 = [1, 2, 3] 
print(countList(lst1, lst2)) 
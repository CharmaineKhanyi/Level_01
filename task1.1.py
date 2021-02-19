sum1 = []
for i in range(0,1000,3):
    sum1.append(i)
sum2 = []
for n in range(0,1000,5):
    sum2.append(n)
del sum2[::3] #delete every 3-rd element in list
print(sum((sum1)+(sum2)))
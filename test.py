str = 'geeksforgeeks'
k = 3

dict1={}
for char in str:
    if char not in dict1:
        dict1[char]=1
    else:
        dict1[char]=dict1[char]+1
        
print(dict1)  
print(dict(sorted(dict1.items(),key=lambda x :x[1])))
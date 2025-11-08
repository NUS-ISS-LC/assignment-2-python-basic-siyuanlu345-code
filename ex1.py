
def find(s, n):
   # write your implementation here
    seen = {}
    
    for i, num in enumerate(s):
    
        complement = n - num
        
       
        if complement in seen:
            return [seen[complement], i]
       
        seen[num] = i
    
    return None
print(find([2, 7, 11, 15], 9))  # [0, 1]
print(find([3, 2, 4], 6))       # [1, 2]
print(find([3, 3], 6))          # [0, 1]
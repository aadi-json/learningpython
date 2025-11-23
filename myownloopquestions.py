# a=[10,20,30,34,35,65,75,53]
# b=[]
# for i in a:
#     if i%2==0:
#         print(i, end=',')

# d={2:3,'hii':7,'python':'prabhusir','sql':'vikas sir'}
# for i in d.items():
#     print(i,end=',')

# l=[2,3,5,7,10,13,17,19,20]
# for i in l:
#     if i%2==0:
#         print(i,end=',')
    
# str="helloo"
# str2=""
# for i in str:
#     if len(str)%2==0:
#         str2=i+str2
#     else:
#         print(str)
# print(str2)

# Q1.
# Given a 2D list nums=[[10,20,30],[40,50,60]], use nested loops to print all elements in a single line separated by spaces.

# nums=[[10,20,30],[40,50,60]]
# for i in nums:
#     for j in i:
#         print(j)

# Q2.
# Using the list nums=[[1,2,3],[4,5,6],[7,8,9]], print only the numbers that are greater than 4 using nested loops.

# nums=[[1,2,3],[4,5,6],[7,8,9]]

# for i in nums:
#     for j in i:
#         if j>4:
#             print(j) 

# data = {
#     "emp1": {"name": "John", "salary": 30000},
#     "emp2": {"name": "Sara", "salary": 45000}
# }
# for i in data:
#     for j in data[i]:
#         print(data[i][j],end=" ")


# For the list matrix=[[2,4,6],[1,3,5],[7,9,11]], use nested loops to calculate and print the average of each row.

# matrix=[[2,4,6],[1,3,5],[7,9,11]]
# for i in matrix:
#     total=0
#     for j in i:
#         total=total+j
#     avg=total/len(i)
#     print(avg)

# Use nested loops to print all possible combinations of characters from both strings.

# a="pq"
# b="123"
# for i in a:
#     for j in b:
#         print(i,j)

# names=["Alice","Bob"]
# subjects=["Math","Science","English"]
# # Use nested loops to print every combination of name and subject.

# for i in names:
#     for j in subjects:
#         print(i,j)

# Write a nested for loop to print a 5×5 pattern of # symbols.

# for i in range(5):
#     for j in range(5):
#         print("#",end="")
#     print()            

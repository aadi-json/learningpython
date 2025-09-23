# IT IS A TYPE PF DATATYPE IN WHICH IT IS A COMBINATION OF BOTH HOMOGEMOUS AND HETEROGENOUS DATA

# a=[1,2,3]------------->HOMOGEMOUS
# b=['a',2,'b',3]-------->HETEROGENOUS

# NOTE:--> LIST IS A ORDERED DATATYPE AND IT ACCEPTS DUPICATE ELEMENT

# a=[1,2,3,3,3,2,1]
# print(a)

# IN LIST WE CAN USE LEN() FUNCTION IT STARTS 1

# b=['a',2,'b',3]
# print(len(b))

# NOTE---> LIST ARE MUTABLE

# b=['a',2,'b',3]
# b[0]='b'
# print(b)


# MUTABLE--->UNHASHABLE-->MUTABILITY
# IMMUTABLE--->HASHABLE--->MUTABILITY

# WE CAN PERFORM INDEXING IN LIST SAME AS STRING BUT THERE IS ONLY DIFFERENCE IS BOUNDRY CONDITION 

# a=[1,2,3,4]
# print(a[7])--->IndexError: list index out of range

# a=[1,2,3,4]
# print(a[0])
# print(a[-1])

#slicing--> the process of extracting multiple element

# types-->
#  1.froward 2.backward 3.combination

#froward slicing-->var_name[si:ei+1:step]

# s=[[[[[[["program",["webtech","instagram"],"snap"]]]]]]] 
# print(s[0][0][0][0][0][0][1][1][0:7:3])
# print(s[0][0][0][0][0][0][0][1:4:1])

# e=["assert","await","return","yeild","elif"]


#forward

#wait

# #positive
# print(e[1][1::1])
# print(e[1][-4:6:1])

#negative
# print(e[-4][4:-5:-1])
# print(e[-4][-1:0:-1])


#turn
e=["assert","await","return","yeild","elif"]

#positive

# print(e[2][2::1])
# print(e[2][-4:6:1])

#negative

# print(e[-3][-1:1:-1])
# print(e[-3][5:-5:-1])

#method in list

# 1.append()
# --> it is used to add element at the end we can only one item at a time

# syntax---->v_n.apppend(element)

# e=["assert","await","return","yeild","elif"]
# e.append(100)
# print(e)

# x=[]
# print(x)---->empty list
# x.append(10)
# x.append(10.7)
# x.append('True')
# x.append(1+3j)

# print(x)



# Execution time

# -->append()

# a=[1,2,3,4]
# a.append((5,6))
# a.append([1,2,3])
# a.append('python')
# a.append({1,2,3})
# print(a)


#--->extend()
# a=[1,2,3,4]
# a.extend((5,6))
# a.extend([1,2,3])
# a.extend(['python'])
# a.extend({1,2,3})
# print(a)


# # --->insert()

# a=[]

a=['Apple','yellow','Orange']
a.sort()
print(a)
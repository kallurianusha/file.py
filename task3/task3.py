#Add two numbers using Recursion:
# def add_recursion(a,b):
#     if b==0:
#         return a
#     else:
#         return add_recursion(a+1,b-1)
# num1 =6
# num2=8
# result =add_recursion(num1,num2)
# print("sum of",num1,"and", num2,"is",result)


# highest frequency in list:
# l = [1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3, 4, 5, 6, 5, 4, 5]
# freq_dict = {}
# for i in l:
#     if i in freq_dict:
#         freq_dict[i] += 1
#     else:
#         freq_dict[i] = 1
# highest_freq_element = max(freq_dict, key=freq_dict.get)
# print("Highest frequency element:", highest_freq_element)


#merging 2 lists:
# a= [1, 2, 3]
# b= [4, 5, 6]
# list= a+ b
# print("list =",list)


#program to print odd numbers in list:
# l =[10,21,4,77,88,93]
# for num in l:
#     if num%2!=0:
#         print(num,end=" ")

#list comprehension:
# l =[10,21,4,77,88,93]
# odd_num =[num for num in l if num%2==1]
# print(odd_num)


#print all even numbers in list:
# num =([5,20,21,42,35,60])
# for num in num:
#     if num%2==0:
#         print(num,end=' ')

#find sum of elements in list:
#sum():
# list=[10,8,4,3]
# print(sum(list))

#list comprehension:
# list=[10,8,4,3]
# s=[i for i in list]
# print(sum(s))

#lambda():
# list=[10,8,4,3]
#print(sum(list(filter(lambda x:(x),list))))

# for loop:
# num =[10,39,45,42,68,79]
# total=0
# for num in num:
#     total+=num
# print("sum of num is:",total)

#append:
# list =[]
# num1= int(input("enter numbers:"))
# for n in range(num1):
#     num2=int(input("enter numbers"))
#     list.append(num2)
# print("sum of elements:",sum(list))


#Delete Element at Given Index in list:
#pop()
# list=[1,2,9,42,54]
# list.pop(3)
# print(list)

#del():
# list=[1,2,9,42,54]
# del list[2]
# print(list)

#slicing():
# list =[1,4,8,5,3,9]
# list = list[:2]+list[3:]
# print(list)


#delete element from list:
#remove():
# list =['python','java','devops']
# list.remove('devops')
# print("list:",list)

#clear():
# l =['python','java','devops']
# element = l.pop(2)
# print(l)

#clear():
#l =['python','java','devops']
# element = l.clear(1)
# print(l)

# #list comprehension:
# l = [1,3,7,9]
# l =[x for x in l if x!=3]
# print(l)


#delete element at the end of list:
# l =[1,3,6,9]
# l.pop()
# print(l)


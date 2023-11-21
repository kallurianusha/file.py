# #reverse number using while loop:
# num = 1234
# reverse_num = 0
# while num>0:
#     digit =num%10
#     reverse_num =reverse_num * 10+digit
#     num = num // 10
# print("reverse_num:"+str(reverse_num))

# #using string slicing:
# num = 123456
# print(str(num)[::-1])

# #check amstrong using while loop:
# num = int(input("enter a number:"))
# sum =0
# temp = num
# count = len(str(num))
# while temp >0:
#     digit = temp%10
#     sum+=digit**count
#     temp //=10
# if num == sum:
#     print("number is an armstrong")
# else:
#     print("number is not armstrong")
        
# #using list comprehension:
# num = int(input("enter number:"))
# digits =[int(digit)for digit in str(num)]
# count =len(digits)
# sum = sum([digit ** count for digit in digits])
# if num == sum:
#     print("number is an armstrong")
# else:
#     print("number is not armstrong")


# # check number is prime or not:
# def is_prime(number):
#     if number>1:
#         for x in range(2,number):
#             if number%x==0:
#                 return False
#         return True
#     else:
#      return False
    
# #check number is palindrome or not using iterative method:
# n = int(input("please give a number : "))
# reverse =0
# temp = n
# while temp!=0:
#     reverse = reverse*10 + temp%10;        
#     temp=temp//10;
# if reverse==n:
#     print("number is palindrom")
# else:
#     print("number is not palindrom")


# #find greatest of 3 numbers:
# n1 = int(input("please give first number n1: "))
# n2 = int(input("please give second number n2: "))
# n3 = int(input("please give third number n3: "))
# if n1>=n2 and n1>=n3: 
# 	print(" n1 is greatest")
# if n2>=n1 and n2>=n3:
# 	print(" n2 is greatest")
# if n3>=n1 and n3>=n2:
# 	print("n3 is greatest")

# #swapping of 2 numbers without using 3rd variable:
# num1 = int(input("please give first number num1: "))
# num2 = int(input("please give second number num2: "))
# num1=num1-num2
# num2=num1+num2
# num1=num2-num1
# print("after swapping numbers")
# print("value of a is : ", num1)
# print("value of b is : ", num2)

# #add 2 numbers without using + operator:
# def add(x,y):
#     while y!=0:
#           temp = x&y
#           x = x%y
#           y =temp<<1
#     return x
# print(add(10,15))


# #check number is even or not:
# num = int(input("Enter a number to check even/odd "))  
# if num%2 == 0:
#    print(num,"is even number")
# else:
#    print(num,"is odd number")


# #find smallest number among 3 :
# a = int(input("Enter the value for a :"))
# b = int(input("Enter the value for b :"))
# c = int(input("Enter the value for c :"))
# if a<=b and a<=c:
# 	print("a is smallest")
# elif b<=a and b<=c:
# 	print("b is smallest")
# elif c<=a and c<=b:
# 	print("c is smallest")
     

# #calculate the square of given number:
# num = int(input("Enter a number to calculate square : "))
# print("square =",num*num)


# #calculate the cube of given number:
# num = int(input("Enter a number to calculate cube : "))
# print("cube =",num*num*num)
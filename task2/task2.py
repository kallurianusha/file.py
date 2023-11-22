# #remove character from string:
# str = input("enter a string : ")
# cha = input("enter a character : ")
# print(str.replace(cha," ")) 

# #replace():
# def remove_char(s1,s2):
#     print(s1.replace(s2, ''))
# s1 = input("enter a String : ")
# s2 = input("enter Character to remove : ")
# remove_char(s1,s2)

# #count occurence of charcacter in string:
# #for loop:
# s1 = input("enter string:")
# s2 = input("enter character")
# count =0
# for i in s1:
#     if i == s2:
#         count = count+1
# print(count)


# #count():
# s1 = input("enter string:")
# s2 = input("enter character")
# print(s1.count(s2))

# #check 2 strings are anagram or not:
# #sorted()
# s1 = input("enter first string:")
# s2 = input("enter second string:")
# if sorted(s1)==sorted(s2):
#     print("strings are in anagram")
# else:
#     print("strings are not in anagram")

# #check strings are in palindrome or not:
# string = input("enter string:")
# if string==string[::-1]:
#     print("string is in palindrome")
# else:
#     print("string is not palindrome")


# #check given letter is vowel or consonent:
# l =input("enter character is vowel or consonent:")
# if (l=='a','e','i','o','u'):
#     print("character is vowel")
# else:
#     print("character is consonent")

# #check character is digit or not:
# str = input("enter string")
# print(string.isdigit())


# #check code to replace the string space with given character:
# #replace()
# s = "i am learning python"
# s = s.replace('','_',3)
# print(s)


# string = input("Enter a String : ")
# result = ''  
# ch = input("Enter a Character : ")
# for i in string:  
#         if i == ' ':  
#             i = ch   
#         result += i   
# print("String  with t = ",result)

# #code to convert lowercase character to uppercase character of string:
# s ="learning python"
# print(string.isupper())
# s= "python coding"
# print(string.islower())


# str = input("Enter a String : ")
# result=''
# for i in str:  
#         if i.islower():  
#             i = i.upper() 
#         result += i 
# print("String :",result)

# #convert lowercase vowel to uppercase :
# str= input("Enter a string: ")
# vowels = "aeiou"
# for char in str:
#     if char in vowels:
#         upper_char = char.upper()
#         string = str.replace(char, upper_char)
# print("string:", str)



# # code to remove vowels from the string:
# string = input("Enter a String : ") 
# result=''
# for i in string:  
#     if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  
#         i = '' 
#     result += i
# print("after removing the vowels :",result)


# # code to count vowels and consonants in the string:
# string = input("Enter a String : ")   
# vowels = 0  
# consonants = 0 
# for i in string:  
#     if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):  
#         vowels+=1 
#     elif i.isalpha():  
#         consonants+=1  
# print("Vowels :",vowels,"Consonants:",consonants)



#highest frequency Character in String :
# s = input("Please Enter a string: ")
# freq_dict= {}
# for char in s:
#     if char in freq_dict:
#         freq_dict[char] += 1
#     else:
#         freq_dict[char] = 1
# max_freq = max(freq_dict.values())
# for char in freq_dict:
#     if freq_dict[char] == max_freq:
#         print(char, end=' ')


#replace 1st occurence vowels with '-' :
# s = input("enter string:")
# v=['a','e','i','o','u']
# for i in s:
#     if i in v:
#         s= s.replace(i,'-')
#         break
#print(s)


#count alphabets, digits, and special characters in the string:
# string = input("Enter a String : ")
# alphabets=0
# digits=0
# specialChars=0
# for i in string: 
#     		if i.isalpha():
#        			alphabets+=1
#     		elif i.isdigit():
#         		digits+=1
#     		else:
#         	    specialChars+=1
# print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)


#Separate Characters in a Given String
# str = "python programming"
# for char in str:
#     print(char)
#     print("\n")

#str = "Hello Python"
#list(map(lambda x: print(x, "\n"), str))


#remove all the blank spaces in a given string:
# s1 = input("enter string:")
# s2 =''
# s1 = s1.replace(' ','')
# print(s1)

# concatenate two string using join() function:
# str1 = input('Enter first string: ')
# str2 = input('Enter second string: ')
# print("String:","".join([str1, str2]))


#concatenate two string without using join method:
# str1 = input('Enter first string: ')
# str2 = input('Enter second string: ')
# string = str1 + str2
# print("String:",string)

#Remove Repeated Character from String:
# s = input("enter string:")
# p =""
# for i in s:
#     if i not in p:
#         p=p+i
# print(p)


#find sum of integers in the string:
# s =input("enter string:")
# sum=0
# for i in s:
#     if i.isdigit():
#         sum +=int(i)
# print("sum=",sum)


#find all nonrepeating characters in the String:
# s = input('Please enter a string: ')
# freq_dict = {}
# for char in s:
#     if char in freq_dict:
#         freq_dict[char] += 1
#     else:
#         freq_dict[char] = 1
# non_repeating_chars = ""
# for char in s:
#     if freq_dict[char] == 1:
#         non_repeating_chars += char
# print("Non-repeating characters:", non_repeating_chars)



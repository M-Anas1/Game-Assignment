user_name = input("please input your name : ")
# print(user_name)
first_num = int(input("please input a number as first number : "))
sec_num = int(input("please input a number as second number : "))
third_num = int(input("please input a number as third number : "))
print(f"\nAsslam o alaikum {user_name} ,Thanks for entering numbers. ")
numbers : list = [first_num , sec_num ,third_num]

# Checking even or Odd
even_odd = []
for number in numbers:
  
    if  number % 2 == 0:
        even_odd.append((number ,"Even"))
    else :
      even_odd.append((number ,"Odd"))
     
# print result of even odd
for number , stats in even_odd:
   print(f"\n{number} is {stats} number .")

# Square of numbers 
square_list = []
for nums in numbers:
   square_list.append((nums , nums **2))

# printing the squares 
print ("\nThere is a square of your given numbers ")   
for num,square in square_list:
   print(f"\nThe square of {num} is {square} .")

# Sum of all 
check : int = first_num + sec_num + third_num
print(f"\nsum of {first_num} + {sec_num} + {third_num} is : ",check)

# Check the Prime number
if check % 2 == 0:
   print (f"\nDear {user_name} ,the sum of all number is {check} that is a prime number . ")
else:
   print (f"\nDear {user_name} ,the sum of all numbers is {check} that is a not a prime number .")

# last message
print ("\n I hope you are enjoy from this .")
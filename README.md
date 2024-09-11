## Personal Information

- My image

![My Image](/Dp.jpg)

- My name is **M Anas**.
- My age is 20 .
- My all information you can get for this [My profile](https://github.com/M-Anas1)

## Experience

- I am a **passionate Python Student .**
- I am also **Forntend developer .**

## About Repo

- This is a **Game** repository .

## About Game

- This game tells that the sum of you given number is **Either prime or nor .**

### Steps of game

**First :** you have to give **Name** the **Three numbers** for this statement .

```python
user_name = input("please input your name : ")
first_num = int(input("please input a number as first number : "))
sec_num = int(input("please input a number as second number : "))
third_num = int(input("please input a number as third number : "))
```

**Second :** This programme Print a Beautiful message for you and store all these number into List by this code.

```python
print(f"\nAsslam o alaikum {user_name} ,Thanks for entering numbers. ")
numbers : list = [first_num , sec_num ,third_num]
```

**Third :** The programme process you number and **multiply by 2** to check **even** or **odd** situation and store result into list in the shape of **Tuple** .
By this statement

```python
even_odd = []
for number in numbers:
    if  number % 2 == 0:
        even_odd.append((number ,"Even"))
    else :
      even_odd.append((number ,"Odd"))
```

**Fourth :** The programme print the the list of **Even odd** result with message .
By this statement

```python
for number , stats in even_odd:
   print(f"\n{number} is {stats} number .")
```

**Fifth :** The programme again process your numbers and find **Square** of them , store into a **new list** and then **print with message**
By this statement

```Python
square_list = []
for nums in numbers:
   square_list.append((nums , nums **2))

print ("\nThere is a square of your given numbers ")
for num,square in square_list:
   print(f"\nThe square of {num} is {square} .")
```

**Sixth :** This programme **calculate** the **Sum** of all your numbers and print .
By this satement

```Python
check : int = first_num + sec_num + third_num
print(f"\nsum of {first_num} + {sec_num} + {third_num} is : ",check)
```

**Seventh :** The programme **Check** the **Sum** and tell that this is **Prime or Not** by **Formula** to check .
By this statement

```Python
if check % 2 == 0:
   print (f"\nDear {user_name} ,the sum of all number is {check} that is a prime number . ")
else:
   print (f"\nDear {user_name} ,the sum of all numbers is {check} that is a not a prime number .")
```

### At the End

- The programme print a beautifull message for **You** with your **Name .**
- By this statement

```Python
print ("\n I hope you are enjoy from this .")
```

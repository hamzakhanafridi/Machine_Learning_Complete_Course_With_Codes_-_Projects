#    ......................    conditional logics    ..................
'''
color = input('Enter color:')
if color=='red':
    print('stop')
elif color == 'green':
    print('go')
elif color=='yellow':
    print('look and wait')
else:
    print('wrong color')
    '''

'''
age= int(input('Enter your age:'))
if age < 18:
    print('you are adult')
elif (age >=18 and age==30):
    print('you are young')
elif (age > 50):
    print('you are old')
    '''


'''
n= int(input('Enter a number:'))
if n%5==0:
    print(n,'is the multiple of 5')
else:
    print(n,'is not the multiple of 5')
'''

#      ......................   NESTING   ....................
'''
username = input('Enter username:')
passward = input('Enter password:')
if(username=='Hamza' and passward=='admin'):
    print('login successful')
else:
    if username!='Hamza':
        print('username is incorrect')
    else:
        print('password is incorrect')
'''


#      ..................     MATCH CASE    ...................
# it work like if else but it is more readable and easy to use but it is used less in python
# color = input('Enter color:')
# match color:
#     case 'red':
#         print('stop')
#     case 'green':
#         print('go')
#     case 'yellow':
#         print('look and wait')
#     case _:
#         print('wrong color')


#           ...................... WHILE LOOP .......................

count=1
# while count <=10:
#     print('Hamza')
#     count+=1

# print(f'End of the loop after {count} iterations')

#     .......         loops printing numbers from 1 to 10 in reverse order        ....... lect 7

# i=10
# while i>=1:
#     print(i)
#     i-=1

#     ........      Multiplication table of n using while loop      ........  lecture 8
# n= int(input('Enter a number:'))
# i=1
# while i<=10:
#     print (f'{n} x {i} = {n*i}')
#     i+=1


#    ............    Break and continue statement in while loop    ............  lecture 9

# i=1
# while i<=10:
#     if i%6==0:
#         break
#     print(i)
#     i+=1
# print(f'End of the loop after {i} iterations')


# i=1
# while i<=10:
#     if i%3==0:
#         i+=1
#         continue
#     print(i)
#     i+=1


#      printing odd numbers from 1 to 10 using while loop
# i=0
# while i<10:
    # i+=1
    # if i%2==0:
    #     continue
    # print(i)


#  2nd method of above code printing odd numbers from 1 to 9
# i=1
# while i<10:
#     print(i)
#     i+=2

#       ..........       For loop in python       ..........  lecture 10

# for i in range(1,11):     # printing numbers from 1 to 10 using for loop
#     print(i)


#    ............ counting the number of i's in a word using for loop
# word= 'artificial Intelligence'
# no_of_i= 0
# for ch in word:
#     if ch=='i':
#         no_of_i+=1
# print(f'No of i in the word {word} is {no_of_i}')   # it does not count the capital I in the word so we can use lower() method to convert all the letters into lower case and then count the i's


#     ............   counting numbers of vowels in a word using for loop   ........

# word= 'artificial Intelligence'
# count=0 
# for ch in word:
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='I':
#         count+=1                          # we can also write it like this     if ch in 'aeiouAEIOU':       count+=1
# print(f'No of vowels in the word {word} is {count}')


 #    ,............  sum of first n natural numbers using for loop   ............  lecture 13
# n= int(input('Enter a number:'))
# sum=0
# for i in range(1,n+1):
#                sum+=i
# print(f'Sum of first {n} natural numbers is {sum}')


#      ...........    Function in python    ...........  lecture 14

# def sum (a,b):
#     s= a+b
#     return s

# ans=sum(10,7)
# print(sum(20,25))
# print(f'the sum is {ans}')


#    ......  default argument in function   .......  lecture 15
# def sum (a,b=5):
#     s= a+b
#     return s
# an=sum(10)
# new=sum(10,20)
# print(f'the sum is {an}')
# print(f'the sum is {new}')


#     ............  lambda function in python   ............  lecture 17
# sum = lambda a,b: a+b
# avg = lambda a,b: (a+b)/2
# print(sum(10,20))
# print(int(avg(10,20)))


#     ..........     Factorial of a number using Function in python    ..........  lecture 18

# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact *=i
#     return fact
# n= int(input('Enter a number:'))
# print(f'Factorial of {n} is {factorial(n)}')


#     .......... nested for loop in python   ........ 
for i in range(1, 3): 
    for j in range(1, 3): 
         print(f"({i}, {j})") 

#      ............    Strings   ............      #1

# string= 'Hamzakhan'
# for i in string:
#     print(i)


# print(string[3])


#     concatenation of strings
# first_name= 'Hamza' 
# last_name= 'Khan'
# full_name= first_name + ' ' + last_name
# print(full_name)


#    .........   string slicing   ..........    #2
# str='Python is a programming language'
# print(str[0:6])  # output: Python
# print(str[10:21])  # output: programming
# print(str[0:len(str):2])  # output: Pto saprgrmmlagu   mean leave 1 and print 2nd



#   .......     formatting and f strings   ..........    #3
# a=2 
# b=7
# sum = a+b
# # formatting method
# print('sum of {1} and {0} is {2}'.format(a,b,sum))  # output: sum of 2 and 7 is 9
# print('sum of {} and {} is {}'.format(a,b,sum))  # output: sum of 2 and 7 is 9

# #f-strings method
# print(f'sum of {a} and {b} is {sum}')  # output


#     ............    Lists   ............      #4
# marks= [90, 80, 70, 60, 50, 'abc', 91.5]
# print(len(marks))  
# print(marks[-5:-1])
# print(marks[1])
# marks[3]=98
# print(marks)


#     ...........   Lists methods   ...........      #5
# l=[1,5,6,2,10]
# l.sort()
# print(l)
# l.reverse()
# print(l)
# l.append(100)
# print(l)
# l.insert(2, 200)
# print(l)
# l.sort(reverse=True)
# print(l)


#   ...........    using for loop with lists   ...........      #6
# l=[1,5,6,2,10]
# x=10
# idx=0
# for i in l:
#     if i==x:
#         print(f'{x} is founded at idx={idx}')
#         break
#     idx+=1


#    ...........    Tuples   ...........      #7
# t= (1, 2, 3, 4, 5, 'abc', 'Hamza', 91.3)
# print(type(t))
# print(t[6])
# print(t[-4:-1])
# print(len(t))

#    ......    tuple methods      ............  #8
# t=(1,2,4,6,8,8,3,2,8)
# sum=0
# for i in t:
#     sum+=i
# print(f'the sum of t is {sum}')   # it will give us sum of all tuple(t)
# print(t.count(8))
# print(t.index(8))    # it will give the ist occrance location 


#    .............   Dictionary     ............  #9
'''
dict={
    'name': 'Hamza',
    'cgpa':3.23,
    'course':['machine learning', 'data science'],
    3.14: 'pi'
}
print(dict)
print(dict['course'])
print(dict[3.14])
'''


#  ............        Dictionary methods   ...............  #10
# dict={
#     'name': 'Hamza',
#     'cgpa':3.23,
#     'course':['machine learning', 'data science'],
#     3.14: 'pi'
# }

# print(dict.get('cgpa'))      # we can also use dict['cgpa']
# print(dict.values())
# print(dict.items())
# dict.update({
#     'last_name':'Afridi'
# })
# print(dict)


#    .......       SETS     ...................
# s={1,2,4,3,56,3,4,3}
# print(len(s))
# print(type(s))
# s.add(40)
# print(s)

#      ..................        set methods   ...............  #12
# s={1,2,4,3,56,3,4,3}
# s1={1,2,4,3,4,3, 20}
# s.remove(2)
# print(s)
# print(s.pop())
# print(s.union(s1))
# print(s.intersection(s1))


#    ............     Practise problems ...............   # 13, 14
s=[
    ('hamza','maths'),
    ('bob','maths'),
    ('tom','maths'),
    ('hamza','Data science'),
    ('bob','data science'),
    ('hamza','machine learning')
]
# Part 1
# set=set()
# for name,course in s:
#     set.add(course)
# print(set)

# Part 2
# set=set()
# for name,course in s:
#     if course=='maths':
#         set.add(name)
# print(set)

# Part 3
dict={}
for name,courses in s:
    if (dict.get(name)==None): # if there is no name in above dictionary update name in next line
        dict.update({name:set()})  # update the dict with the name and empty set
        dict[name].add(courses)   # add course in empty set of the above line in front of that name 
    else:
        dict[name].add(courses)      # mean if name exist in above dict only add course of that name
print(dict)
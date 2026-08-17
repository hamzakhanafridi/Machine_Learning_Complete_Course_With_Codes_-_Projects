#    ...............  Modes of file operations  reading, writing etc ................  #2
# f=open('sample.txt', 'r')
# data= f.read()     # for reading complete file
# print(data)

# d=f.readline()      # for reading single line
# print(d)

 # for Writing
# f=open('sample.txt', 'w')
# f.write('this is hamza afridi \n from darra adam khel \n studing machine learning')
# f.close()


#    .........   Using with keyword      ..............  #3
#we can use with keyword to open the file instead of the above method here we dont need to write close function
# with open('sample.txt', 'r') as f:
#     data=f.read()
#     print(data)
#     print(len(data))     # this can also count spaces


#    ..............     Deleting the file    ...............  #4
# import os
# os.remove('sample1.txt')


#     ...............    Different type of operations    .............   #5

# with open('sample.txt' , 'a+') as f:   # this is now append mode append mode for read and write(r+)
#     f.write('\nmy name is hamza')    # first append then read in next line
#     data=f.read()
#     print(data)

#     ...............    Word search   .................  #6
# data= True
# word= 'machine learning'
# count=1

# with open('sample.txt', 'r') as f:
#     while data:
#         data=f.readline()
#         if (word in data):
#             print('word exist')
#             break
#         count+=1
# print(f'{word} is found at line {count}')


#   .............    Exception handling (try, except, else, finally)
# try:
#     n=int(input('enter a number : '))
#     ans=10/n

# except ZeroDivisionError:
#     print('division by zero is not possible')

# except ValueError:
#     print('invalid input')

# else:
#     print(f' The answer is {ans}')

# finally:
#     print('i am running in every situation')


#    ..............   List comprehension   
# square=[i*i for i in range(8)]
# print(square)

#  same above method using for loop
# square =[]
# for i in range(8):
#     square.append(i*i)
# print(square)


# second scenirio of list comprehensive
# lis=[-3,2,6,-8,55,-6,4]
# zer=[0 if val<0 else val for val in lis]
# print(zer)


#    ...............  JSON module ...........
# import json
# py_obj={
#     'name':'Hamza',
#     'sub':'Ml/Ai',
#     'is':True
# }
# json_str=json.dumps(py_obj)      # converted py object into json string
# print(type(json_str), json_str)

# json_str='{"name": "Hamza", "sub": "Ml/Ai", "is": true}'
# py_obj=json.loads(json_str)
# print(type(py_obj), py_obj)

#   ............   reading from JSON file
# import json
# with open('data.json', 'r') as f:
#     py_obj= json.load(f)
#     print(type(py_obj), py_obj)

# ............   Writing python object in the json file ......
import json
py_obj={'name': 'Hamza', 
 'is': True, 
 'address': {
     
    'city': 'peshawar',
    'country': 'pakistan'
    }, 
 'subject': ['machine learning', 'data science'],
 'new_name':'afridi'
 }
with open('data.json', 'w') as f:
    json.dump(py_obj, f, indent=4, sort_keys=True)  #  indent mean add spacing, sort key mean add all in ascending order
    
# print('hello Python world')
# message = "Hi world!"
# #message = "Hi new world!"
# print(message)
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())
# from pyautogui import resolution
# from pymsgbox import prompt
from collections import OrderedDict

from importlib_resources import contents

# from numbers import response

# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# print(full_name)
# print("Hello," + full_name.title()+"!")

# print("Python")
# print("\tPython")
# print("Languages:\n\tPython\n\tC\n\tJavaScript")
# favorite_language = "python 111   "
# print(favorite_language)
# print(favorite_language.rstrip())

# age = 23  #类型错误 无法判断 age为int  还是str
# # message = "Happy" + age + "rd Birthhday!"
# # print(message)
# message = "Happy " + str(age) + "rd Birthday!"
# print(message)
# print(5+3)

# bicycles = ['trek','cannondale','redline','specialized']
# print(bicycles[0])
# print(bicycles[0].title())
# message ="My first bicycle was a " + bicycles[0].title() + "."
# print(message)

# motorcycles = ['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles.insert(0,'ducati')
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# first_owned = motorcycles.pop(0)
# print("The first motorcyle I owned was a " + first_owned.title()+'.')

# motorcycles.remove('ducati')
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA "+ too_expensive.title() + "is too expensive for me")

# cars = ['bmw','audi','toyota','subaru'] #根据首字母排序
# cars.sort(reverse=True)
# print(cars)

# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

# motorcycles = ['honda','yamaha','suzuki',]
# print(motorcycles[-1])

# magicians = ['alice','david','carolina']
# for magician in magicians:
#         print(magician.title() + ", that was a great trick!")
# #在magicians中取出一个名字 储存在变量magician中
# # for cat in cats:
# # for dog in dogs:
# # for item in list_of_items:
# for value in range(1,5):
#         print(value)
# numbers = list(range(2,11,2)) #从2开始数 不断加2 <=11
# print(numbers)
# squares = []
# for value in range(1,11):
#     # square = value**2  #平方
#     # squares.append(square)
#     squares.append(value**2)
#     print(squares)
# players = ['charles','martina','michael','florence','eli']
# # print(players[-3:])
# print("Here are the first three players on my team:")
# for player in players[:3]:
# #         print(player.title())
# dimensions = (200,50)
# # print(dimensions[0])
# # print(dimensions[1])
# # dimensions[0] = 250
# # for dimension in dimensions:
# #     print(dimension)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)
#
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#         print("Hold the anchovies!")
#
# answer = 18
# if answer != 42:
#         print("That is not the correct answer . Please try again!")
# banned_user = ['andrew','carolina','david']
# user = 'marie'
# if user not in banned_user:
#         print(user.title()+",you can post a response if you wish.")

# age = 17
# if age >= 18:
#     print("You are old enough to votel!")
# else:
#     print("Sorry,you are too young to vote.")
# age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")
# alien_0 = {'color': 'green', 'points': 5}
#
# print(alien_0['color'])
# print(alien_0['points'])
#
# alien_0['x_postion'] = 0
# alien_0['y_postion'] = 25
# print(alien_0)
# user_0 = {
# 'username': 'efermi',
# 'first': 'enrico',
# 'last': 'fermi',
# }
# for key,value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)
# message = input("Tell me something,and I will repeat it back to you: ")
# print(message)
# prompt = "If you tell us who you are,we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("\nHello, "+name+"!")
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to "+ city.title() + "!")
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number %2 == 0:
#         continue
#     print(current_number)
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: "+ current_user.title())
#     confirmed_users.append(current_user)
# print("\nThe following users have been confirmed: ")
# for confirmed_users in confirmed_users:
#     print(confirmed_users.title())
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name?")
#     response = input("Which mountain would you like to climb someday? ")
#
#     responses[name] = response
#
#     repeat = input("Would you like to let another person respond?(yes/no) ")
#     if repeat == 'no':
#         polling_active = False
#
#
#     print("\n--- Poll Results ---")
#     for name,response in responses.items():
# #         print(name + "would like to climb "+ response + ".")
# responses = {}
# # 设置一个标志，指出调查是否继续
# polling_active = True
# while polling_active:
# # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
# # 将答卷存储在字典中
#     responses[name] = response
# # 看看是否还有人要参与调查
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
# # 调查结束，显示结果
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")

# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!!!")
#
# greet_user()
# def describe_pet(pet_name,animal_type='dog'):
#     print("\nI have a "+animal_type+'.')
#     print("My "+ animal_type + "'s name is "+ pet_name.title()+".")
#
# describe_pet('hamster','harry')
# describe_pet('dog','willie')
# def get_formatted_name(first_name,last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
# musician = get_formatted_name('jimi','hendrix')
# print(musician)
# def describe_pet(pet_name,animal_type='dog'):
#     """显示宠物的信息"""
#     print("\nI have a "+animal_type+ ".")
#     print("My "+ animal_type+"'s name is "+ pet_name.title() + ".")
# describe_pet(pet_name='willie')
# def get_formatted_name(first_name,middle_name,last_name):
#     """返回格式化的姓名"""
#     full_name = first_name + ' '+middle_name+' '+last_name
#     return full_name.title()
#
# musician = get_formatted_name('john','lee','hooker')
# # print(musician)
# def get_formatted_name(first_name,last_name,middle_name=''):
#     """返回格式化的姓名"""
#     if middle_name:
#         full_name = first_name + ' '+middle_name+' '+last_name
#     else:
#         full_name = first_name + ' '+last_name
#     return full_name.title()
# #
# musician = get_formatted_name('john','hooker','lee')
# print(musician)
# musician = get_formatted_name('jimi','hendrix')
# print(musician)
# def build_person(first_name,last_name,age=''):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('jimi','hendrix',age=27)
# print(musician)
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print("\nHello, "+ formatted_name + "!")
# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
# usernames = ['hannah','ty','margot']
# greet_users(usernames)
# 首先创建一个列表 其中包含一些要打印的设计
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
# # 模拟打印每个设计 直到没有未打印的设计为止
# # 打印每个设计后  都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # 模拟根据设计制作3D打印模型的过程
#     print("Printing model: "+ current_design)
#     completed_models.append(current_design)
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs,completed_models):
#
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
#
# # print_models(unprinted_designs,completed_models)
# print_models(unprinted_designs[:],completed_models)
# show_completed_models(completed_models)
# from pizza import make_pizza as mp
# import pizza as p
# # import pizza
# # def make_pizza(size,*toppings):
# #     print("\nMaking a "+ str(size)+ " -inch pizza with the following toppings:")
# #     for topping in toppings:
# #         print("-" + topping)
# p.make_pizza(16,'pepperoni')
# p.make_pizza(12,'mushrooms','green peppers','extra cheese')
# def build_profile(first,last,**user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key,value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert','einstein',location='princeton',field='physics')
# print(user_profile)
# class Dog():
#     """模拟小狗"""
#     def __init__(self,name,age):
#         """初始化"""
#         self.name = name
#         self.age = age
#         # self 指向自己的指针  -- this指针
#     def sit(self):
#         print(self.name.title()+" is now sitting.")
#     def roll_over(self):
#         print(self.name.title()+ " rolled over! ")
#
# my_dog = Dog('willie',6)
# # 实例化
# print("My dog's name is "+ my_dog.name.title()+ ".")
# print("My dog is "+ str(my_dog.age)+ " years old.")

# # my_tesla = ElectricCar('tesla','model y',2020)
# # print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# from Car import Car,ElectricCar
# my_new_car = Car('audi','a4',2025)
# print(my_new_car.get_descriptive_name())
# my_tesla = ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())

# from collections import OrderedDict
# # 模块collections 中的一个类 orderedDict
# favorite_languages = OrderedDict()
# favorite_languages['jen'] = 'python'
# favorite_languages['sarach'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
#
# for name,language in favorite_languages.items():
#     print(name.title() + "'s favourite language is " + language.title()+ ".")
#
# from random import randint
# x = randint(1,6)
# print(x)
"""文件操作"""
# # with open('test.txt') as file_object:
# #     contents = file_object.read()
# #     print(contents)
# filename = 'test.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# # for line in lines:
# #         print(line.rstrip())
# string = ''
# for line in lines:
#     string += line.rstrip()
# # print(string)
# # print(len(string))
#
# birthday = input("Enter your birthday,in the form mmddyy: ")
# if birthday in string:
#     print("Your birthday apperars in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")
# filename = 'programming.txt'
# with open(filename,'a') as file_object:
#     file_object.write("I also  love finding meaning in large datasets.\n")
#     file_object.write("I love creating apps that can run in a browser.\n")


# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# filename = 'alices.txt'
# try:
#     with open(filename) as f_obj: #错误是从open导致的
#         contents = f_obj.read()
# except FileNotFoundError:
#     pass
#     # msg = "Sorry,the file "+ filename + " does not exist."
#     # print(msg)
# else:
#     words = contents.split()
#     num_words = len(words)
#     print("The file " + filename + "has about " + str(num_words)+ " word.")
# import json
# numbers = [2,3,5,7,11,13]
# filename = 'numbers.json'
# # with open(filename,'w') as f_obj:
# #     json.dump(numbers,f_obj)
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)
# # username = input("What is your name? ")
# # filename = 'username.json'
# # with open(filename,'w') as f_obj:
# #     json.dump(username,f_obj)
# #     print("We'll remember you when you come back, "+ username+"!")
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, "+ username+"!")
import json
# import remember_me,greet
# # 如果以前储存了用户名 就加载 否则就输入 并储存
# filename = 'username.json'
# try:
#     greet.greet()
# except FileNotFoundError:
#     remember_me.remeber()
# else:
#     print("Welcome back")
# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = first + ' ' + last
#     return full_name.title()

import unittest
# print("\\t")
# msg = "  i am kiier  "
# print(msg.strip())
for value in range(5):
    print(value)
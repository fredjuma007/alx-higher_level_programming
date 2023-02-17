#!/usr/bin/python3
"""
Module 3-say_my_name
Contains method that prints out "My name is [full name]"
Takes in two strings: first and last name
"""
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

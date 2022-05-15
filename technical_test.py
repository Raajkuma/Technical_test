# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:10:35 2020

@author:Raajkumar
"""
import re
def add(string):
    "Calculating the Sum of Total digit value from the string"
    string=re.split(";|,|\s|(?<!\d)[,.](?!\d)", string)
    sum_of_string_numbers=0
    negative_values=[]
    for i in string:
        if i.lstrip('-').replace('.', '', 1).isdigit():
            if int(i)>=0:
                sum_of_string_numbers+=int(i)
            else:
                print()
                negative_values.append(i)

    if len(negative_values)>0:
        raise Exception("negatives not allowed",",".join(negative_values))
    return sum_of_string_numbers

INPUT_STRING="1\n2,3"
print(add(INPUT_STRING))

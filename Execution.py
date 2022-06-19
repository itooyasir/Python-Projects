# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:39:20 2022

@author: Yasir Itoo
"""

#to calculate the execution time of a Python program, we need to follow the steps mentioned below:

 #   First, store the time of initiation of the program into a variable;
 #   Write the Python program;
 #   Store the end time of the program into a variable;
 #   Subtract the time of initiation of the program from the end time of the program;
  #  In the end, you will get the execution time of your program in seconds.

from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence Engineering"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)
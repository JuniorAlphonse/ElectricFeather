# Write a program with the function of graphing an array, list, or key-dictionary pair without using the input-value function of cin().

## The goal of this program is to, hopefully, generate images, or better yet pictographs, without the manual input of using a pre-existing human generated image database. Essentially, the code will have the capacity to generate images just from intergalatic search engine (like Google but not just using Earth satellites).

import math
import cmath

pi = math.pi;
# print(pi);

i = cmath.sqrt(-1);
e = i**2;
list = [];
array = {(1/2), 1.00, 2.00, 3.00, e, i};

def graph_function_zipper(list, array):
    if list == []:
        for i in range(len(array)):
             print(i, array);
    elif list == list.pop(array): 
        print(list.pop(zip(list, array)));
    else:
        print("No results found.");

graph_function_zipper([], array);

# Write a program with the function of graphing an array, list, or key-dictionary pair without using the input-value function of cin().

## The goal of this program is to, hopefully, generate images, or better yet pictographs, without the manual input of using a pre-existing human generated image database. Essentially, the code will have the capacity to generate images just from intergalatic search engine (like Google but not just using Earth satellites).

import math
import cmath

pi = math.pi;
# print(pi);

i = cmath.sqrt(-1);
e = i**2;
originallist = [];
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

list2 = array;
array_two = {(2**0/2**1), 1.0, 1.9, 9.8, 8.29, 9.84};
list3 = list(zip(list2, array_two));
# Erroneous Logic based on the definition of list using curly brackets, which are typically used to create dictionaries. list4 = [i * array_two.index(9.84) in array_two];

def graph_function_paiger(list2, array_two, list3):
    if array_two == list2:
        return list2; return list3; print(list3);
    else:
        print(list3);
    
    if any(item in list3 for item in array):
        for i in range(len(list3)):
            print(i, list3);

graph_function_paiger([1], ["I love you"], list3)
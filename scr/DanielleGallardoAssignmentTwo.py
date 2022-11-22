# -*- coding: utf-8 -*-
"""
CSC 499 Homework

CSC 499
Fall 2022
Homework 1: (20 pts.)

Danielle
"""
this_file = open('Sort Me.txt', 'r')
new_file = open('Sorted_MeTwo.txt', 'w')


def store_sort_array(ar): # here we put are sorted array in the file
    i = 0
    print("made it")
    for i in range(len(ar)):
        new_file.write(ar[i])
        new_file.write('\n')
        
    print("done")
    new_file.close()
    return ar

def sort_array(ar):# Here we sort the array
    print("sorting")

    ar.sort()
    #try sorted
    #How we sort by lenght
    
    
    
    print(ar)
    
    ar.sort(key=len, reverse=True)
        
    print("final")
    print(ar)
    
    store_sort_array(ar)
    return ar



def make_array(): #here where the array gets made
    next_line = this_file.readline()
    print("Starting to make")
    ar = []
    
    while next_line != "":
        ar.append(next_line)
        next_line = this_file.readline()
        
        
    # Clean the text
    for i in range(len(ar)-1):
               
        ar[i] = ar[i].replace(" ", "")
        ar[i] = ar[i].replace("\n", "")
        if ar[i] == "":
            del ar[i]
        ar[i] = ar[i].replace(" ", "")# For some reason some words get thougth with spaces this fixs that
        ar[i] = ar[i].replace("\n", "")
        
    sort_array(ar)
    return 0


def main():
    # the start
    making_array = True

    if making_array:
        make_array()
        making_array = False
    
    return 0
main()
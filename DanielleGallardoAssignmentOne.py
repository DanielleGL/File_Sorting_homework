# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:55:30 2022
CSC 499 Homework

CSC 499
Fall 2022
Homework 1: (20 pts.)
Download and extract the Suran Developer Exam resources:
https://download.suran.com/developer/developer_exam_resources.zip

Locate the text file called “Sort Me.txt” containing a list of names. 
Write a command-lineprogram to sort the contents of this file 
in ascending order first by the length of the name, then
alphabetically. Expected output is listed below.

You must read input from stdin or a file—do not prompt for user input to specify the file.

You must write output to stdout or to a file. Using a print() command is fine.

You can use any language to write the program. Python is a good choice, especially if you are
unfamiliar working with stdin and stdout.

The program must run on Linux or macOS. If you have a Windows computer, install the WSL
(Windows Subsystem for Linux) to get a Linux environment. Ubuntu is a popular distribution to
use.
Submit the source code and instructions on how to run it by email to Alex Clay at
aclay@mac.com by 11:59 PM EST Wednesday September 14, 2022.
Danielle Gallardo
"""
this_file = open('Sort Me.txt', 'r')
new_file = open('Sorted_Me.txt', 'w')


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
    
    ar.sort(key=len)
        
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
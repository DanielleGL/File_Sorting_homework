@echo off
"C:\Users\liana\anaconda3\python.exe" "C:\Users\liana\OneDrive\Desktop\CSC 499\For Homework Two\DanielleGallardoAssignmentOne.py"


fc /b Sorted_Me.txt CorrectOne.txt > nul
if errorlevel 1 (
    echo Fail
) else (
    echo Succes
)

"C:\Users\liana\anaconda3\python.exe" "C:\Users\liana\OneDrive\Desktop\CSC 499\For Homework Two\DanielleGallardoAssignmentTwo.py"


fc /b Sorted_MeTwo.txt CorrectTwo.txt > nul
if errorlevel 1 (
    echo Fail
) else (
    echo Succes
)


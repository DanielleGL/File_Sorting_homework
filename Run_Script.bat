@echo off
"python.exe" "DanielleGallardoAssignmentOne.py"


fc /b Sorted_Me.txt CorrectOne.txt > nul
if errorlevel 1 (
    echo Fail
) else (
    echo Succes
)

"python.exe" "DanielleGallardoAssignmentTwo.py"


fc /b Sorted_MeTwo.txt CorrectTwo.txt > nul
if errorlevel 1 (
    echo Fail
) else (
    echo Succes
)


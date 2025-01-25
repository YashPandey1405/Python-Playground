import os
import sys
from os.path import dirname, join, abspath

# Get the parent directory path
parent_dir_path = abspath(join(dirname(__file__), '..'))
print(parent_dir_path)

# Insert the parent directory path into sys.path
sys.path.insert(0, parent_dir_path)
print(sys.path)

# Import the student_details module
from Yash import YashPandey

def DivyamJain():
    print("Currently In DivyamJain() Of Module 'Divyam")
    print("Hello , Myself Divyam Jain")
    print()
    print("Calling YashPandey() Of Module 'Yash")
    YashPandey.YashPandey()

print()
DivyamJain()
print()
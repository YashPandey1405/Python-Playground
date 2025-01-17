"""
Here are single-line descriptions of the modes for opening files in Python:

1. `"r"` (Read)**: Opens a file for reading (default mode); file must exist.  
2. `"w"` (Write)**: Opens a file for writing, creating it if it does not exist or truncating it if it does.  
3. `"a"` (Append)**: Opens a file for appending, creating it if it does not exist; writes are added at the end.  
4. `"r+"` (Read and Write)**: Opens a file for both reading and writing; file must exist.  
5. `"w+"` (Write and Read)**: Opens a file for writing and reading, truncating it if it exists or creating it otherwise.  
6. `"a+"` (Append and Read)**: Opens a file for appending and reading, creating it if it does not exist.  
7. Binary Modes (`"rb"`, `"wb"`, etc.)**: Add `"b"` to handle files in binary mode instead of text.  
"""

f = open("file.txt")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()
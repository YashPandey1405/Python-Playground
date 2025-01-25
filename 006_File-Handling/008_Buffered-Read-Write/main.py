import io

# Writing to a file using BufferedWriter
with open("test_buf.txt", "wb") as f:
    file_writer = io.BufferedWriter(f)
    file_writer.write(b"A computer is a machine that can be programmed to automatically carry out sequences of operations.\n")
    file_writer.write(b"hello\n")
    file_writer.write(b"I am good\n")
    file_writer.flush()

# Reading from the file using BufferedReader
with open("test_buf.txt", "rb") as f:
    file_reader = io.BufferedReader(f)
    data = file_reader.read(100)  # Read 100 bytes
    print(data.decode())  # Print the data as a string

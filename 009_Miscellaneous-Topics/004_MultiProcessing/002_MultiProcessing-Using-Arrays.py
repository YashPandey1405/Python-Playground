import multiprocessing  # Importing the multiprocessing module to create and manage processes.
import time  # Importing the time module to measure execution time.

# Record the start time of the program.
start = time.perf_counter()

def test_func():
    """
    A test function to simulate some work.
    Prints messages, sleeps for 1 second, and then indicates completion.
    """
    print("Do something")
    print("Sleep for 1 second")
    time.sleep(1)  # Simulates a task by sleeping for 1 second.
    print("Done with sleeping")

# Create and start multiple processes.
processes = []
for i in range(10):  # Loop to create 10 processes.
    p = multiprocessing.Process(target=test_func)  # Create a process targeting test_func.
    p.start()  # Start the process.
    processes.append(p)  # Append the process to the list.

# Wait for all processes to complete.
for process in processes:
    process.join()

# Record the end time of the program.
end = time.perf_counter()

# Print the total execution time.
print(f"The program finished in {round(end - start, 2)} seconds.")

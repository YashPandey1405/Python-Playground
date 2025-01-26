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

# Create two processes targeting the test_func function.
p1 = multiprocessing.Process(target=test_func)
p2 = multiprocessing.Process(target=test_func)

# Start both processes.
p1.start()
p2.start()

# Wait for both processes to complete.
p1.join()
p2.join()

# Record the end time of the program.
end = time.perf_counter()

# Print the total execution time.
print(f"The program finished in {round(end - start, 2)} seconds.")

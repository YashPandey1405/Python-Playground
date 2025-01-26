'''
1. Python threads enable concurrent execution of multiple tasks within a single process, allowing programs to handle multiple operations simultaneously.  
2. The **`threading`** module in Python provides tools to create and manage threads efficiently.  
3. Threads share the same memory space, making inter-thread communication simpler but requiring synchronization mechanisms like locks to avoid race conditions.  
4. Python's Global Interpreter Lock (GIL) limits true parallelism in CPU-bound tasks, but threads are effective for I/O-bound operations.  
5. Thread-based concurrency can improve performance in applications like web servers, data scraping, and real-time event handling.  
'''
import time
import threading

def perform_task(task_id: int, sleep_time: int = 5):
    """Function executed by threads."""
    print(f"Task {task_id}: Starting...")
    print(f"Task {task_id}: Sleeping for {sleep_time} seconds...\n")
    time.sleep(sleep_time)
    print(f"Task {task_id}: Finished sleeping.\n")

def main():
    start = time.perf_counter()
    
    threads = []
    num_threads = 4
    sleep_time = 5

    # Create and start threads
    for i in range(1, num_threads + 1):
        thread = threading.Thread(target=perform_task, args=(i, sleep_time))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end = time.perf_counter()
    print(f"Total time taken: {int(end - start)} seconds")

if __name__ == "__main__":
    main()

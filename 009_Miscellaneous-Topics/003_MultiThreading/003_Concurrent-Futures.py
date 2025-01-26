import time
from concurrent.futures import ThreadPoolExecutor

def task(name: str):
    """Simulates a task by sleeping for 2 seconds."""
    print(f"Task {name} starting...")
    time.sleep(2)
    print(f"Task {name} completed!")
    return f"Result from {name}"

def main():
    start = time.perf_counter()

    # Create a thread pool with 3 workers
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        task_names = ["A", "B", "C", "D"]
        futures = [executor.submit(task, name) for name in task_names]

        # Collect results as tasks complete
        for future in futures:
            print(future.result())

    end = time.perf_counter()
    print(f"Total time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()

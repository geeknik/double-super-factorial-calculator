import math
import concurrent.futures
import os
import time

def factorial(n):
    return math.factorial(n)

def double_super_factorial(n):
    result = 1
    for i in range(n, 0, -2):
        result *= factorial(i)
    return result

def find_dsf_solution(n):
    nfactorial = factorial(n)
    m = 1
    while True:
        dsf_m = double_super_factorial(m)
        if dsf_m == nfactorial:
            return n, m
        if dsf_m > nfactorial:
            return None
        m += 1

def worker(start_n, num_iterations):
    solutions = []
    for n in range(start_n, start_n + num_iterations):
        result = find_dsf_solution(n)
        if result:
            solutions.append(result)
    return solutions

def main():
    print("Double Super Factorial Calculator - Multi-threaded Search")
    print("========================================================")

    start_n = 1  # Start searching from n = 1
    num_cores = os.cpu_count()
    chunk_size = 100  # Number of iterations per worker task

    print(f"Using {num_cores} CPU cores")
    print("Searching for solutions to n! = dsf(m) for n > 10:")
    print("(This may take a very long time. Press Ctrl+C to stop.)")

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
            current_n = start_n
            futures = []

            while True:
                # Submit tasks to the thread pool
                for _ in range(num_cores):
                    future = executor.submit(worker, current_n, chunk_size)
                    futures.append(future)
                    current_n += chunk_size

                # Process completed tasks
                for future in concurrent.futures.as_completed(futures):
                    solutions = future.result()
                    for n, m in solutions:
                        print(f"Found solution: {n}! = dsf({m}) = {factorial(n)}")

                futures.clear()

                print(f"Checked up to n = {current_n}, continuing search...")
                time.sleep(0.1)  # Short sleep to allow for keyboard interrupt

    except KeyboardInterrupt:
        print("\nSearch interrupted by user.")

    print("Search completed.")

if __name__ == "__main__":
    main()

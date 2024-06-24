# Double Super Factorial Calculator

Welcome to the Double Super Factorial Calculator! This project is a multi-threaded Python application that searches for solutions to the equation `n! = dsf(m)`, where `dsf(m)` represents the double super factorial of `m`.

## Project Inspiration

The idea for this project is inspired by a post on [John D. Cook's blog](https://www.johndcook.com/blog/2024/03/25/double-superfactorial/), where the concept of double super factorials is discussed. We aim to explore this mathematical concept further by finding pairs of integers `(n, m)` such that the factorial of `n` equals the double super factorial of `m`. Allegedly, we'll never find a result for n > 10 but we'll see.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Performance Considerations](#performance-considerations)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Double Super Factorial Calculator is designed to:

1. Compute the factorial of a given number `n`.
2. Compute the double super factorial of a number `m`.
3. Search for solutions where `n! = dsf(m)`.
4. Utilize multi-threading to speed up the search process by leveraging multiple CPU cores.

![image](https://github.com/geeknik/double-super-factorial-calculator/assets/466878/5f3116b9-5942-4992-a1e8-aa95a160294e)

## Installation

To get started, clone the repository and install the required dependencies. Ensure you have Python 3.x and `gmpy2` installed.

```bash
git clone https://github.com/geeknik/double-super-factorial-calculator/
cd double-super-factorial-calculator
pip install gmpy2
```

## Usage

Run the main script to start the search for solutions:

```bash
python3 dsf.py
```

The script will start searching for solutions to `n! = dsf(m)` for `n > 10` and will continue indefinitely until stopped by the user (Ctrl+C).

## Algorithm Explanation

### Factorial Calculation

The `factorial` function calculates the factorial of a given number `n` using the `gmpy2` library for arbitrary-precision arithmetic:

```python
def factorial(n):
    return gmpy2.fac(n)
```

### Double Super Factorial Calculation

The `double_super_factorial` function calculates the double super factorial of a given number `m`:

```python
def double_super_factorial(m):
    result = gmpy2.mpz(1)
    for i in range(m, 0, -2):
        result *= factorial(i)
    return result
```

### Solution Search

The `find_dsf_solution` function searches for pairs `(n, m)` such that `n! = dsf(m)`:

```python
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
```

### Multi-threading

The `main` function uses the `concurrent.futures.ThreadPoolExecutor` to distribute the workload across multiple CPU cores:

```python
def main():
    ...
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        ...
        while True:
            for _ in range(num_cores):
                future = executor.submit(worker, current_n, chunk_size)
                futures.append(future)
                current_n += chunk_size
            
            for future in concurrent.futures.as_completed(futures):
                solutions = future.result()
                for n, m in solutions:
                    print(f"Found solution: {n}! = dsf({m}) = {factorial(n)}")
            
            futures.clear()
            print(f"Checked up to n = {current_n}, continuing search...")
            time.sleep(0.1)
    ...
```

## Performance Considerations

- The search process can be computationally intensive and time-consuming, especially for large values of `n` and `m`.
- Multi-threading helps to speed up the search by distributing the work across multiple CPU cores.
- The `gmpy2` library is used for efficient arbitrary-precision arithmetic.

## Contributing

We welcome contributions! If you have suggestions for improvements or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore the code, run the program, and contribute to the project. Happy calculating!

---

By [@geeknik](https://twitter.com/geeknik)

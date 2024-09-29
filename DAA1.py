def fibonacci_iter(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1

    steps = 0
    fib_series = [0, 1]
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        fib_series.append(c)
        a, b = b, c
        steps += 1
    return fib_series, steps + 1

def fibonacci_recur(n):

    def helper(n):
        if n == 0:
            return [0], 1
        elif n == 1:
            return [0, 1], 1
        
        fib_series_1, steps_1 = helper(n - 1)
        fib_series_2, steps_2 = helper(n - 2)
        fib_series = fib_series_1 + [fib_series_1[-1] + fib_series_2[-1]]
        return fib_series, steps_1 + steps_2 + 1
    
    if n < 0:
        return [], 1
    return helper(n)

def main():
    while True:
        print("Fibonacci Series Calculator")
        print("1. Iterative Approach")
        print("2. Recursive Approach")
        print("3. Exit")
        choice = input("Choose an option : ")
        
        if choice == '1':
            n = int(input("Enter a number: "))
            iter_series, iter_steps = fibonacci_iter(n)
            print(f"Iterative: Fibonacci series up to {n}: {iter_series}")
            print(f"Iterative Steps: {iter_steps}")
        
        elif choice == '2':
            n = int(input("Enter a number: "))
            recur_series, recur_steps = fibonacci_recur(n)
            print(f"Recursive: Fibonacci series up to {n}: {recur_series}")
            print(f"Recursive Steps: {recur_steps}")
        
        elif choice == '3':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()

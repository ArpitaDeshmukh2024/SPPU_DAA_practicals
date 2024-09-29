def fractional_knapsack(capacity, profits, weights):
    items = sorted(zip(profits, weights), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0.0

    for profit, weight in items:
        if capacity >= weight:
            total_value += profit
            capacity -= weight
        else:
            total_value += profit * (capacity / weight)
            break

    return total_value

def main():
    n = int(input("Enter the number of items: "))
    
    profits = []
    weights = []

    for i in range(n):
        profit = int(input(f"Enter profit of item {i + 1}: "))
        weight = int(input(f"Enter weight of item {i + 1}: "))
        profits.append(profit)
        weights.append(weight)
    
    capacity = int(input("Enter the capacity of the knapsack: "))
    max_value = fractional_knapsack(capacity, profits, weights)
    
    print(f"Maximum value in knapsack: {max_value}")

if __name__ == "__main__":
    main()

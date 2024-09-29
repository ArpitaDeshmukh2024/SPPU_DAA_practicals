def knapsack_01(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][W]

    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return max_value, selected_items

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    
    values = []
    weights = []

    for i in range(n):
        value = int(input(f"Enter value of item {i + 1}: "))
        weight = int(input(f"Enter weight of item {i + 1}: "))
        values.append(value)
        weights.append(weight)
    
    W = int(input("Enter the capacity of the knapsack: "))

    max_value, selected_items = knapsack_01(values, weights, W)
    
    print("Maximum value:", max_value)
    print("Selected items (by index):", selected_items)

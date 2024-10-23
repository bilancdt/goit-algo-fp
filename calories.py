# Доступні страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Створюємо список зі страв та їх співвідношенням калорій до вартості
    items_sorted = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, data in items_sorted:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(item)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen_items, total_calories, total_cost

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    # Перетворюємо словник у списки для зручної роботи з динамічним програмуванням
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    
    # Створюємо таблицю для збереження максимальних калорій при різних бюджетах
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    
    for i in range(1, len(items) + 1):
        for b in range(1, budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]
    
    # Визначаємо, які страви були вибрані
    total_calories = dp[len(items)][budget]
    total_cost = 0
    chosen_items = []
    b = budget
    for i in range(len(items), 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen_items.append(names[i - 1])
            total_cost += costs[i - 1]
            b -= costs[i - 1]

    return chosen_items, total_calories, total_cost

# Тестування
budget = 100

# Жадібний алгоритм
chosen_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", chosen_greedy)
print("Загальні калорії:", total_calories_greedy)
print("Загальні витрати:", total_cost_greedy)

# Алгоритм динамічного програмування
chosen_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", chosen_dp)
print("Загальні калорії:", total_calories_dp)
print("Загальні витрати:", total_cost_dp)

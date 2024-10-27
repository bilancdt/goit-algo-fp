import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def simulate_dice_rolls(num_rolls):
    # Ініціалізуємо масив для зберігання сум
    sums = []
    
    for _ in range(num_rolls):
        die1 = np.random.randint(1, 7)  # Кидаємо перший кубик
        die2 = np.random.randint(1, 7)  # Кидаємо другий кубик
        sums.append(die1 + die2)  # Додаємо суму до списку

    return sums

def calculate_probabilities(sums):
    # Підраховуємо частоти для кожної можливої суми
    frequency = {i: 0 for i in range(2, 13)}
    
    for s in sums:
        frequency[s] += 1
    
    # Обчислюємо ймовірності
    probabilities = {s: freq / len(sums) for s, freq in frequency.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    # Візуалізація ймовірностей
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, alpha=0.7, color='blue')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.xticks(sums)
    plt.grid(axis='y')
    plt.show()

# Основний блок програми
num_rolls = 1000000  # Кількість імітацій
sums = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sums)
plot_probabilities(probabilities)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}

# Порівняння з аналітичними ймовірностями
comparison_df = pd.DataFrame({
    'Сума': list(probabilities.keys()),
    'Монте-Карло': list(probabilities.values()),
    'Аналітичні': [analytical_probabilities[s] for s in probabilities.keys()]
})

print(comparison_df)

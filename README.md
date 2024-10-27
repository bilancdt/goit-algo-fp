# goit-algo-fp
# Симуляція кидання кубиків за допомогою методу Монте-Карло

## Опис завдання
Ця програма імітує багаторазове кидання двох кубиків, обчислює суми чисел, які випадають, та визначає ймовірності кожної можливої суми за допомогою методу Монте-Карло. Метою є порівняти результати симуляції з аналітичними ймовірностями для кожної суми, які наведені в таблиці.

## Аналітичні розрахунки ймовірностей
Аналітичні ймовірності, іказані в табиці д.з.:

| Сума | Імовірність  | 
|------|--------------|
| 2    | 2.78% (1/36) |
| 3    | 5.56% (2/36) |
| 4    | 8.33% (3/36) |
| 5    | 11.11% (4/36)|
| 6    | 13.89% (5/36)|
| 7    | 16.67% (6/36)|
| 8    | 13.89% (5/36)|
| 9    | 11.11% (4/36)|
| 10   | 8.33% (3/36) |
| 11   | 5.56% (2/36) |
| 12   | 2.78% (1/36) |

## Результати симуляції
Симуляція за методом Монте-Карло виконана з використанням 1,000,000 ітерацій. За підрахунками частот випадіння кожної суми, ми отримали наступні ймовірності.
| Сума |Монте-Карло | Аналітичні Python |
|------|------------|-------------------|
|  2   |  0.027692  | 0.027778          |
|  3   |  0.055613  | 0.055556          |
|  4   |  0.083815  | 0.083333          |
|  5   |  0.111717  | 0.111111          |
|  6   |  0.138478  | 0.138889          |
|  7   |  0.166104  | 0.166667          |
|  8   |  0.139066  | 0.138889          |
|  9   |  0.111537  | 0.111111          |
|  10  |  0.083131  | 0.083333          |
|  11  |  0.055045  | 0.055556          |
|  12  |  0.027802  | 0.027778          |

## Висновки

1. **Точність симуляції**: Результати, отримані за допомогою симуляції Монте-Карло, досить близькі до аналітичних значень. Зі збільшенням кількості симуляцій (1,000,000 ітерацій) отримані значення збігаються з аналітичними розрахунками з невеликим відхиленням.
  
2. **Відхилення**: Незначні відхилення можуть бути обумовлені випадковістю симуляції. Однак, у великих симуляціях вони стають мінімальними і наближаються до теоретичних значень.

3. **Висновок щодо методу Монте-Карло**: Метод Монте-Карло є ефективним інструментом для оцінки ймовірностей в задачах, де важко або неможливо отримати аналітичні рішення. Для задачі з двома кубиками цей метод продемонстрував високу точність навіть при великій кількості можливих комбінацій.

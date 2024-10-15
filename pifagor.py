import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(branch_length, level, angle):
    if level == 0:
        return
    
    # Малюємо основну гілку
    turtle.forward(branch_length)
    
    # Поворот і малювання лівої гілки
    turtle.left(angle)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, angle)
    
    # Поворот назад і малювання правої гілки
    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_length * 0.7, level - 1, angle)
    
    # Повертаємося до початкового напрямку
    turtle.left(angle)
    turtle.backward(branch_length)

# Основна функція для візуалізації дерева Піфагора
def pythagoras_tree(level):
    # Ініціалізація вікна turtle
    turtle.speed('fastest')
    turtle.left(90)  # Поворот на 90 градусів вгору для старту
    turtle.penup()
    turtle.goto(0, -250)  # Початкова позиція (для зручного відображення дерева)
    turtle.pendown()

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(100, level, 30)

    # Завершення малювання
    turtle.done()

# Користувач вводить рівень рекурсії
level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))

# Викликаємо функцію для малювання дерева з вказаним рівнем
pythagoras_tree(level)

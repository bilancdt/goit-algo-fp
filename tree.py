import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Отримуємо кольори та мітки для відображення
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    # Візуалізація дерева
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, with_labels=True, font_size=10, font_color="black")
    plt.show()

def count_nodes_iteratively(root):
    """
    функція для підрахунку кількості вузлів у бінарному дереві.
    Використовує чергу 
    """
    if root is None:
        return 0

    count = 0
    queue = deque([root])
    while queue:
        current = queue.popleft()
        count += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return count

def generate_color(step, max_steps):
    """
    Генерує кольори від темного до світлого синього відтінку залежно від кроку.
    Колір генерується в 16-річній системі RGB.
    0 - Білий, бо значення вузла з нульовим значенням не встановлювався правильно через генерацію кольорів.
    """
    ratio = step / max_steps
    blue_value = int(50 + (205 * (1 - ratio)))  # Обмежуємо колір до темно-синього від #3232ff до світлого
    return f'#{blue_value:02x}{blue_value:02x}ff'

def bfs_traversal(root):
    
    if root is None:
        return

    queue = deque([root])
    steps = 0
    total_nodes = count_nodes_iteratively(root)

    while queue:
        current = queue.popleft()

        # Оновлюємо колір вузла залежно від кроку
        current.color = generate_color(steps, total_nodes)

        # Візуалізуємо дерево після зміни кольору
        draw_tree(root)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        steps += 1

def dfs_traversal(root):
    
    if root is None:
        return

    stack = [root]
    steps = 0
    total_nodes = count_nodes_iteratively(root)

    while stack:
        current = stack.pop()

        # Оновлюємо колір вузла залежно від кроку
        current.color = generate_color(steps, total_nodes)

        # Візуалізуємо дерево після зміни кольору
        draw_tree(root)

        # Додаємо спочатку правий, потім лівий вузол у стек, щоб лівий оброблявся першим
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        steps += 1

# Створення дерева
root = Node(0)  # Вузол з нульовим значенням
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід дерева в ширину (BFS) з візуалізацією
print("Обхід у ширину (BFS):")
bfs_traversal(root)

# Перезавантажуємо кольори для демонстрації DFS
root.color = "skyblue"
root.left.color = "skyblue"
root.left.left.color = "skyblue"
root.left.right.color = "skyblue"
root.right.color = "skyblue"
root.right.left.color = "skyblue"

# Обхід дерева в глибину (DFS) з візуалізацією
print("Обхід у глибину (DFS):")
dfs_traversal(root)

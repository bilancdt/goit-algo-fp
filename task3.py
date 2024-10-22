import heapq

def dijkstra(graph, start):
    # Ініціалізуємо відстані для всіх вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Відстань до початкової вершини дорівнює 0

    # Пріоритетна черга для вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]  # Пара (відстань, вершина)

    while priority_queue:
        # Отримуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдено більше оптимальний шлях, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Перебираємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусідньої вершини
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Кожна вершина має список сусідів у форматі (суміжна_вершина, вага_ребра)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Викликаємо алгоритм Дейкстри від вершини 'A'
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

# результат
print(f"Найкоротші відстані від вершини '{start_vertex}':")
for vertex, distance in shortest_paths.items():
    print(f"Вершина {vertex}: {distance}")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Вставка на початок
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Вставка в кінець
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Вставка після певного вузла
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Видалення вузла за значенням
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # Пошук елемента
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Друк списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    # Реверсування списку
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next  # Зберігаємо наступний вузол
            cur.next = prev  # Міняємо напрямок посилання
            prev = cur  # Пересуваємо prev на поточний вузол
            cur = next_node  # Пересуваємо cur на наступний вузол
        self.head = prev  # Оновлюємо головний елемент списку

    # Сортування вставками
    def sorted_insert(self, new_node: Node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None and cur.next.data < new_node.data:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

    def insertion_sort(self):
        sorted_list = LinkedList()  # Порожній список для зберігання відсортованих вузлів
        cur = self.head
        while cur is not None:
            next_node = cur.next  # Зберігаємо наступний вузол
            cur.next = None  # Від'єднуємо вузол
            sorted_list.sorted_insert(cur)  # Вставляємо у відсортований список
            cur = next_node
        self.head = sorted_list.head  # Оновлюємо голову списку


# Функція для об'єднання двох відсортованих списків
def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_list = LinkedList()
    
    cur1 = list1.head
    cur2 = list2.head
    
    while cur1 is not None and cur2 is not None:
        if cur1.data <= cur2.data:
            merged_list.insert_at_end(cur1.data)
            cur1 = cur1.next
        else:
            merged_list.insert_at_end(cur2.data)
            cur2 = cur2.next

    # Додаємо решту елементів зі списків
    while cur1 is not None:
        merged_list.insert_at_end(cur1.data)
        cur1 = cur1.next
    
    while cur2 is not None:
        merged_list.insert_at_end(cur2.data)
        cur2 = cur2.next
    
    return merged_list

# Демонстрація роботи однозв'язного списку
llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список до реверсування:")
llist.print_list()

# Реверсування списку
llist.reverse()
print("\nЗв'язний список після реверсування:")
llist.print_list()

# Сортування вставками
print("\nЗв'язний список до сортування:")
llist.print_list()
llist.insertion_sort()
print("\nЗв'язний список після сортування:")
llist.print_list()

# Створюємо два відсортовані списки для об'єднання
list1 = LinkedList()
list2 = LinkedList()

list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

# Об'єднуємо два відсортовані списки
merged_list = merge_sorted_lists(list1, list2)

print("\nОб'єднаний відсортований список:")
merged_list.print_list()

print("Реализация структуры данных - Дек!")

class Node:
    """"Реализация объекта класса, его данных(data), ссылки на следующий элемент(.next), ссылки на предыдущий элемент(.prev)."""
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class Deck:

    """"Инициализация класса, его размера,головы,хвоста."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def push_front(self, value):
        """Функция добавления элемента вперед. О(1)."""
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size = self.size + 1

    def push_back(self, value):
        """Функция добавления элемента назад. О(1)."""
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size = self.size + 1

    def remove_first(self):
        """Функция удаления элемента спереди. O(1)."""
        if self.size == 0:
            raise EmptyStructureError("Deck","Удалять нечего!")
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size = self.size - 1

    def remove_last(self):
        """Функция удаления элемента сзади. О(1)."""
        if self.size == 0:
            raise EmptyStructureError("Deck","Удалять нечего!")
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size = self.size - 1

    def get_size(self):
        """Функция вывода длинны списка. О(1)."""
        return self.size

    def get_deck(self):
        """Функция вывода дека. О(n)"""
        if self.size == 0:
            raise EmptyStructureError("Deck","Выводить нечего, список пуст!")
        elif self.size == 1:
            return self.head.data
        else:
            list = []
            current = self.head
            while current is not None:
                list.append(str(current.data))
                current = current.next
        list_out = " -> ".join(list)
        return list_out

    def peek_front(self):
        """Функция для вывода первого элемента дека. O(1)."""
        if self.size == 0:
            raise EmptyStructureError("Deck", "Ошибка вывода, дек пуст!")
        else:
            return self.head

    def peek_last(self):
        """"Функция для вывода последнего элемента дека. O(1)."""
        if self.size == 0:
            raise EmptyStructureError("Deck", "Ошибка вывода, дек пуст!")
        else:
            return self.tail






class StructureError(Exception):
    """Базовый класс для всех исключений структур данных"""
    pass

class EmptyStructureError(StructureError):
    """ошибка при попытке операции с пустой структурой"""
    def __init__(self, structure_name, message="Structure is empty"):
        self.structure_name = structure_name
        super().__init__(f"{message}: {structure_name}")

class IndexError(StructureError):
    """ошибка при обращении по несуществующему индексу"""
    def __init__(self, index, message="Index out of range"):
        self.index = index
        super().__init__(f"{message}: {index}")

class ValueNotFoundError(StructureError):
    """ошибка при поиске несуществующего значения"""
    def __init__(self, value, message="Value not found"):
        self.value = value
        super().__init__(f"{message}: {value}")












class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0


    def push(self, value):
        """Функция добавления элемента в стек. O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size = self.size + 1


    def pop(self):
        """Функция удаления элемента из стека. O(1)."""
        if self.head is None:
            raise EmptyStructureError("Стек пуст, удалять нечего!!!")
        else:
            deleted = self.head.data
            self.head = self.head.next
            self.size = self.size - 1
            return deleted

    def peek(self):
        """Функция проверки первого элемента. O(1)."""
        if self.head is None:
            raise EmptyStructureError("Стек пустой, удалять там нечего!!)")
        else:
            return self.head.data

    def is_empty(self):
        """Функция проверки стека на пустоту """
        if self.head is None:
            return f"Стек пуст!"
        else:
            return f"Стек не пуст!"

    def clear(self):
        """Очистка стека. O(1)."""
        self.head = None
        self.size = 0

    def contains(self, value):
        """Проверка элемента в стеке. O(n) - в худшем случае."""
        if self.head is None:
            raise EmptyStructureError("Стек пустой, искать нечего!!)")
        else:
            current = self.head
            while current is not None:
                if current.data == value:
                    return f"Значение есть в стеке!"
                current = current.next
        raise ValueNotFoundError("Значение не найдено в списке!")

    def sum(self):
        """Сумма элементов стека. O(n)."""
        if self.size == 0:
            raise EmptyStructureError("Стек пуст, суммировать нечего!")
        elif self.size == 1:
            return self.head.data
        else:
            current = self.head
            sum = 0
            while current is not None:
                sum = sum + current.data
                current = current.next
            return sum

    def print_stack(self):
        if self.size == 0:
            return f"Stack пуст!"
        elif self.size == 1:
            return str(self.head.data) + " -> None"
        else:
            all = []
            current = self.head
            while current is not None:
                all.append(current.data)
                current = current.next
            string = " ".join(str(i) for i in all)
            string = string + ' -> None'
            return string










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









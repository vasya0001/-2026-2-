class Node:
    """"Класс узла, ссылка на его данные и на следуюзий элемент."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        """Функция добавления в начало очереди. O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size = self.size + 1

    def push_back(self, value):
        """Функция добавления элемента в конец очереди. O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size = self.size + 1

    def peek_front(self):
        """Функция проверки первого элемента очереди. O(1)."""
        if self.head is None:
            raise EmptyStructureError("Очередь пуста!!!")
        else:
            return self.head.data

    def peek_back(self):
        """Функция проверки последнего элемента очереди. O(1)."""
        if self.head is None:
            raise EmptyStructureError("Очередь пуста!!!")
        else:
            return self.tail.data

    def pop_back(self):
        """Функция удаления последнего элемента. O(n)."""
        if self.head is None:
            raise EmptyStructureError("Очередт пуста!Удалять сзади нечего!")
        elif self.size == 1:
            destroyed = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return destroyed
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.tail = current
            self.size = self.size - 1


    def pop_front(self):
        """Функция удаления элемента в начале. O(1)."""
        if self.head is None:
            raise EmptyStructureError("Очередь пуста! Спереди удалять нечего!")
        if self.size == 1:
            destroyed = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return destroyed
        else:
            deleted = self.head.data
            self.head = self.head.next
            self.size = self.size - 1
            return deleted

    def destroy(self):
        """Функция удаления очереди. O(1)."""
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        """Функция вывода размера очереди. O(1)."""
        return self.size

    def is_empty(self):
        """Функция проверки очереди на пустоту. O(1)."""
        return self.head is None

    def contains(self, item):
        """Функция проверки списка на находимость элемента. O(n)."""
        if self.head is None:
            raise EmptyStructureError("Очередь пуста! Тут искать нечего!!!")
        else:
            current = self.head
            while current is not None:
                if current.data == item:
                    return f"Такое значение присутствует в очереди!"
                current = current.next
            raise ValueNotFoundError("Значения нету в очереди!")

    def print_queue(self):
        """Функция вывода очереди. O(n)."""
        if self.head is None:
            return f"Очередь пуста!"
        else:
            all = []
            current = self.head
            while current is not None:
                all.append(current.data)
                current = current.next
            string = ' '.join(str(i) for i in all)
            return f"{string} -> None"

    def find_all(self, value):
        """Функция вывода всех всхождений определенного значения. O(n). """
        if self.head is None:
            raise EmptyStructureError("Очередь пуста! выводить нечего!")
        else:
            indices = []
            k = 0
            current = self.head
            while current is not None:
                if current.data == value:
                    indices.append(k)
                k = k + 1
                current = current.next
            if len(indices) == 0:
                return f'Таких значений нету!'
            else:
                string = " ".join(str(x)for x in indices)
                return string


    def first_plus_last(self):
        """Функция суммы первого и последнего элемента очереди. O(2)."""
        if self.size == 0:
            raise EmptyStructureError("Очередь пуста")
        elif self.size == 1:
            return f"В очереди есть только 1 элемент, {self.head}"
        else:
            return f"Сумма первого и последнего элементов равна: {self.head.data + self.tail.data}"

    def sum(self):
        """Функция суммы всех элементов очереди. O(n)."""
        if self.size == 0:
            raise EmptyStructureError("очередь пуста!")
        elif self.size == 1:
            return self.head
        else:
            loi = []
            summ = 0
            current = self.head
            while current is not None:
                loi.append(current.data)
                current = current.next
            for i in loi:
                summ = summ + i
            return summ





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


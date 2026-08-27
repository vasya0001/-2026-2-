from debugpy.common.timestamp import current


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class OneSideList:
    def __init__(self):
        self.head = None
        self.size = 0


    def append(self, data):
        """Функция добавления элемента назад. O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
             current = self.head
             while current.next is not None:
                 current = current.next
             current.next = new_node
        self.size += 1


    def prepend(self, item):
        """Функция добавления элемента назад. O(1). """
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size = self.size + 1


    def insert_before(self, item, index):
        """Функция добавление элемента перед индексом. O(n - 1) - в противном случае."""
        new_node = Node(item)
        if index > self.size or index < 0:
            raise IndexError(index,"Неверный индекс")
        elif index == 0:
            self.prepend(item)
            return
        else:
            k = 0
            current = self.head
            while k < index - 1:
                current = current.next
                k = k + 1
            new_node.next = current.next
            current.next = new_node
        self.size = self.size + 1


    def insert_after(self,item,index):
        """Функция добавления элемента после индекса"""
        new_node = Node(item)
        if index >= self.size or index < 0:
            raise IndexError(index,"Неверный индекс")
        if index == self.size - 1:
            self.append(item)
            return

        current = self.head
        k = 0
        while k < index:
            current = current.next
            k = k + 1
        new_node.next = current.next
        current.next = new_node
        self.size = self.size + 1


    def remove_first(self):
        """Функция удаления первого элемента из списка. O(1)."""
        if self.head is None:
            raise EmptyStructureError("Список пуст, удалять нечего!")
        elif self.size == 1:
            self.head = None
        else:
            self.head = self.head.next
            self.size = self.size - 1

    def remove_last(self):
        """Функция удаления посленего элемента из списка. O(n)."""
        if self.head is None:
            raise EmptyStructureError("Список пуст, удалять нечего!")
        elif self.size == 1:
            self.head = None
            self.size = 0
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
        self.size = self.size - 1

    def remove_at(self, index):
        """Функция удаления элемента по индексу. O(n) - в худшем случае."""
        if index > self.size - 1 or index < 0:
            raise IndexError(index,"Неверный индекс!!!")
        if index == 0:
            self.remove_first()
            return
        else:
            current = self.head
            k = 0
            while k < index-1:
                current = current.next
                k = k + 1
            current.next = current.next.next
            self.size = self.size - 1

    def remove_value(self, value):
        """Функция удаления элемента по значению. O(n) - в худшем случае."""
        current = self.head
        if self.head is None:
            raise EmptyStructureError("Список пуст, удалть нечего!")
        elif self.head.data == value:
            self.remove_first()
            return
        else:
            while current.next is not None:
                if current.next.data == value:
                    current.next = current.next.next
                    self.size = self.size - 1
                    return f"Значение по индексу удалено!"
                current = current.next
        raise ValueNotFoundError("Значение не найдено!")

    def is_empty(self):
        """Функия проверки списка на пустоту. O(1)."""
        if self.size == 0:
            return f"Список пуст!\n"
        else:
            return f"Список не пуст!\n"

    def get_size(self):
        """Функция выведения размера списка на экран. O(1)."""
        return self.size

    def contains(self, value):
        """Функция поиска определенного значения в списке. O(n) -  худшем случае."""
        if self.size == 0:
            raise EmptyStructureError("Нельзя найти значение в пустом списке!")
        current = self.head
        if current.data == value:
            return f"Элемент есть в списке!"
        while current.next is not None:
            if current.next.data == value:
                return f"Элемент есть в списке!"
            current = current.next
        return f"Элемента нету в списке!"

    def print_list(self):
        """Функция вывода списка на экран. O(n)."""
        if self.head is None:
            print("List is empty!")
        else:
            current = self.head
            while current is not None:
                print(f"{current.data}", end=" ")
                current = current.next
            print("-> None")

    def clear(self):
        """"Функция отчистки списка. O(n)."""
        self.head = None
        self.size = 0


    def find_all(self, value):
        """Функция поиска всех вхождений элементов. O(n!)."""
        if self.size == 0:
            raise EmptyStructureError("Список пуст, искать нечего!")
        elif self.size == 1:
            raise ValueNotFoundError(value,f"Список состоит из 1 элемента: {self.head.data}")
        else:
            aoi = []
            current = self.head
            count = 0
            while current is not None:
                if current.data == value:
                    aoi.append(count)
                current = current.next
                count = count + 1
            string = ""
            if len(aoi) == 0:
                return f"Вхождений элемента {value} нету!"
            else:
                for i in aoi:
                    string = string + " " +str(i)
            return f"Вхождения: {string}"


    def sum(self):
        """Функция суммы всех элементов. O(n)."""
        if self.size == 0:
            raise EmptyStructureError("Список пуст, удалять нечего!")
        elif self.size == 1:
            return self.head.data
        else:
            sum = 0
            current = self.head
            while current is not None:
                sum = sum + current.data
                current = current.next
            return sum





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


















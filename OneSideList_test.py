from oneSideList import OneSideList,StructureError,EmptyStructureError, IndexError,ValueNotFoundError
print("Тестирование программы oneSideList.py, которая реализует структуру данных - односвязный(односторонний) список.")
print("\n")
print("Создание и добалние элемента 5  в начало спискa (prepend):")

oslist = OneSideList()
oslist.prepend(5)
oslist.print_list()
print("\n")

print("Добавление элемента 15 в конец списка(append):")
oslist.append(15)
oslist.print_list()
print("\n")

print("Добавление элемента 10 перед индексом 1(числом 15),(insert_before):")
oslist.insert_before(10,1)
oslist.print_list()
print("\n")

print("Добавение элемента 12 после индекса 1(числом 10), (insert_after):")
oslist.insert_after(12,1)
oslist.print_list()
print("\n")

print("Удаление первого элемента списка(5), (remove_first):")
oslist.remove_first()
oslist.print_list()
print("\n")

print("Удаление последнего элемента списка(15), (remove_last):")
oslist.remove_last()
oslist.print_list()
print("\n")

print("Удаление элемента по индексу 1 (12). O(n) - в худшем случае, (remove_at):")
oslist.remove_at(1)
oslist.print_list()
print("\n")

print("Удаление элемента по значению (10). O(n) - в худшем случае. (remove_value):")
oslist.remove_value(10)
oslist.print_list()
print("\n")

print("Проверка листа на пустоту(is_empty). O(1):")
print(oslist.is_empty())
print("Добавление элемента (10) в список для корректной проверки пустоты списка(is_empty). O(1):")
oslist.append(10)
print("Список:", end=' ')
oslist.print_list()
print(oslist.is_empty())

print("Вывод размера листа(get_size).O(1).")
print("Список:", end=' ')
oslist.print_list()
print(f" Размер списка:{oslist.get_size()}\n")

print("Поиск определенного значения(10) в списке(contains). O(n) - в худшем случае.")
print("Список:", end=' ')
oslist.print_list()
print(oslist.contains(10))
print("\n")

print("Вывод списка(print_list):")
oslist.print_list()
print("\n")

print("Очистка списка(clear). O(1).")
oslist.clear()
print("Список:", end=' ')
oslist.print_list()
print("\n")

print("ДОБАВИМ ЭЛЕМЕНТЫ ДЛЯ ДАЛЬНЕЙШЕГО ТЕСТИРОВАНИЯ!!!")
oslist.append(10)
oslist.append(20)
oslist.append(10)
oslist.append(30)

print("Список:", end=' ')
oslist.print_list()
print("\n")

print("Найдем все вхождения элемента(10). O(n!).")
print(oslist.find_all(10))
print("\n")

print("Найдем сумму списка(sum). O(n).")
print("Список:", end=' ')
oslist.print_list()
print(f"Cумма: {oslist.sum()}")


print("\n")
print("Тест ошибок в функциях!")
print("\n")

print("Функция добавления элемента перед индексом , который выходит за пределы списка:")
try:
    oslist.insert_before(99,20)
except IndexError as e:
    print(f"Ошибка: {e}")
print("\n")

print("Функция добавления элемента после индекса, который выходит за рамки списка:")
try:
    oslist.insert_after(99,20)
except IndexError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция удаления первого элемента из пустого списка(предварительно перед этим oslist.clear() - очистить список:")
oslist.clear()
try:
    oslist.remove_first()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция удаления последнего элемента из пустого списка:")
try:
    oslist.remove_last()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция удаления элемента по индексу, который выходит за границы списка:")
try:
    oslist.remove_at(-15)
except IndexError as e:
    print(f"Ошибка: {e}")

print("\n")
oslist.clear()
print("Функция удаления элемента по значению, если список пуст:")
try:
    oslist.remove_value(14)
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

oslist.prepend(10)
print("\n")
print("Функция удаления элемента по значению, если его нету:")
try:
    oslist.remove_value(14)
except ValueNotFoundError as e:
    print(f"Ошибка: {e}")

oslist.clear()
print("\n")
print("Функция нахождения элемента, если список пуст:")
try:
    oslist.contains(10)
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция нахождения всех индексов значения, когда список пуст:")
try:
    oslist.find_all(10)
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция суммы, если список пуст:")
try:
    oslist.sum()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")









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















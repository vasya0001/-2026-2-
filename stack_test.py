from stack import Stack,StructureError,EmptyStructureError,ValueNotFoundError,IndexError,Node
print("\n")
print("Тестирование программы stack.py, которая реализует структуру данных - Стек.")

print("\n")
print("Создание стека и добавление элемента 5(push):")
stack = Stack()
stack.push(5)
print(stack.print_stack())

print("\n")
print("Удаление элемента (pop):")
stack.pop()
print(stack.print_stack())

print("\n")
print("Добавим элементы(10,20,30,40) в стек для дальнейшего тестирования:")
stack.push(40)
stack.push(30)
stack.push(20)
stack.push(10)
print("Стек:", end=" ")
print(stack.print_stack())

print("\n")
print("Проверка первого элемента стека!(peek)")
print(stack.peek())

print("\n")
print("Проверка стека на пустоту(is_empty):")
print(stack.is_empty())

print("\n")
print("Очистка стека(clear):")
stack.clear()
print("Стек:", end=" ")
print(stack.print_stack())

print("\n")
print("Добавим элементы(10,20,30,40) в стек для дальнейшего тестирования:")
stack.push(40)
stack.push(30)
stack.push(20)
stack.push(10)
print("Стек:", end=" ")
print(stack.print_stack())

print("\n")
print("Проверка значения 10 в стеке(contains):")
print(stack.contains(10))

print("\n")
print("Вывод стека(print_stack):")
print("Стек:", end=" ")
print(stack.print_stack())

print("\n")
print("Вывод суммы стека:")
print(stack.sum())

print("\n")
print("Тестирования ошибок в функциях реализации!!!")

stack.clear()
print("\n")
print("Ошибка удаления элемента в пустом стеке:")
try:
    stack.pop()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Ошибка проверки элемента в пустом стеке:")
try:
    stack.peek()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Ошибка проверки определенного элемента на присутствие в пустом стеке:")
try:
    stack.contains(10)
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

stack.push(12)
print("\n")
print("Ошибка проверки определенного элемента на присутствие(его нет):")
try:
    stack.contains(999)
except ValueNotFoundError as e:
    print(f"Ошибка: {e}")

stack.clear()
print("\n")
print("Ошибка суммы стека при пустом стеке:")
try:
    stack.sum()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")











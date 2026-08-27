from Queque import Queue, ValueNotFoundError,EmptyStructureError,IndexError,StructureError, Node
print("\n")
print("Программы тестирования программы Queue.py, которая реализует структуру данных - Очередь:")

print("\n")
print("Создание очереди и добавление элемента 5 в начало(push_front):")
queue = Queue()
queue.push_front(5)
print(queue.print_queue())

print("\n")
print("Добавление элемента 20 в конец очереди(push_back):")
queue.push_back(20)
print(queue.print_queue())

print("\n")
print("Проверка первого элемента в очереди(peek_front):")
print(queue.peek_front())

print("\n")
print("Проверка последнего элемента в очереди(peek_back):")
print(queue.peek_back())

print("\n")
print("Удаление первого элемента(pop_front):")
queue.pop_front()
print(queue.print_queue())

print("\n")
print("Удаление последнего элемента(pop_back):")
queue.pop_back()
print(queue.print_queue())

print("\n")
print("ДОБАВИМ ЭЛЕМЕНТЫ(10,20,30,10,40,10) ДЛЯ ДАЛЬНЕЙШЕГО ТЕСТИРОВАНИЯ!")

queue.push_front(10)
queue.push_front(40)
queue.push_front(10)
queue.push_front(30)
queue.push_front(20)
queue.push_front(10)
print("Очередь: ", end='')
print(queue.print_queue())

print("\n")
print("Удаление очереди(destroy):")
queue.destroy()
print(queue.print_queue())

print("\n")
print("ДОБАВИМ ЭЛЕМЕНТЫ(10,20,30,10,40,10) ДЛЯ ДАЛЬНЕЙШЕГО ТЕСТИРОВАНИЯ!")

queue.push_front(10)
queue.push_front(40)
queue.push_front(10)
queue.push_front(30)
queue.push_front(20)
queue.push_front(10)
print("Очередь: ", end='')
print(queue.print_queue())

print("\n")
print("Вывод размера очереди(get_size):")
print(queue.get_size())

print("\n")
print("Функция проверки списка на пустоту(is_empty):")
print(f"Список пуст: {queue.is_empty()}")

print("\n")
print("Функция нахождение элемента(10) в очереди(contains):")
print(queue.contains(10))

print("\n")
print("Функция вывода списка(print_queue):")
print(queue.print_queue())

print("\n")
print("Функция нахождение всех вхождений элементов (10), (find_all):")
print(queue.find_all(10))

print("\n")
print("Функция первого и последнего(first_plus_last):")
print(queue.first_plus_last())

print("\n")
print("Функция суммы всех элементов очереди(sum):")
print(queue.sum())

print("\n")
print("Тесты ошибок в функциях!!!")

queue.destroy()
print("Функция проверки первого элемента в пустой очереди:")
try:
    queue.peek_front()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция проверки последнего элемента в пустой очереди:")
try:
    queue.peek_back()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция удаления последнего элемента в пустой очереди:")
try:
    queue.pop_back()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция удаления первого элемента в пустой очереди:")
try:
    queue.pop_front()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция нахождения элемента в пустой очереди:")
try:
    queue.contains(33)
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

queue.push_front(10)
queue.push_front(40)
queue.push_front(10)
queue.push_front(30)
queue.push_front(20)
queue.push_front(10)

print("\n")
print("Функция нахождения элемента в очереди, если его нету:")
try:
    queue.contains(33)
except ValueNotFoundError as e:
    print(f"Ошибка: {e}")

queue.destroy()
print("\n")
print("Функция нахождения элементов в пустой очереди:")
try:
    queue.find_all(33)
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция нахождения суммы первого и последнего элемента в пустой очереди:")
try:
    queue.first_plus_last()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

print("\n")
print("Функция нахождения суммы:")
try:
    queue.sum()
except EmptyStructureError as e:
    print(f"Ошибка: {e}")

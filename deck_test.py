from deck import Deck
print("Тест для программы deck.py, которая реализует структуру данных - Дек!")
print("Создание и добавление элемента спереди в структуру данных!\n")
deck = Deck()
deck.push_front(5)
print(f"Дек после добавления элемента 5 в начало(push_front): {deck.get_deck()}\n")
deck.push_back(10)
print(f"Дек псоле добавления числа 10 в конец(push_back): {deck.get_deck()}\n")
deck.push_back(15)
print("Добавим число 15 в конец дека")
print(f"После добавления: {deck.get_deck()}\n")
deck.remove_first()
print(f"Дек после удаления элемента 5 в начале(remove_first): {deck.get_deck()}\n")
deck.remove_last()
print(f"Дек после удаления элемента 15 в конце(remove_last): {deck.get_deck()}\n")
print(f"Вывод размера дека: {deck.get_size()}")






import math
import random

def test_greeting():

    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."


    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():

    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = 2 * (a + b)

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b

    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    PI = math.pi

    # TODO сосчитайте площадь
    area = PI * (r ** 2)

    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * PI * r

    assert length == 144.51326206513048

    print(f"Длина = {length}")
    print(f"Площадь = {area}")

    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список

    l = [random.randint(1, 100) for _ in range(10)]
    l.sort()

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
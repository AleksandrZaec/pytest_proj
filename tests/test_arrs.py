from utils.arrs import get, my_slice


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
    assert get([], 0, "test") == "test"
    assert get([1, 2, 3], -1, "test") == "test"  # Проверка отрицательного индекса


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]
    assert my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]  # Проверка отрицательных индексов
    assert my_slice([], 0, 2) == []  # Проверка пустого списка

"""
Задание 1, вариант 5.

Исходная функция:
    def foo(nums):
        for x in nums:
            if x % 2 == 0:
                return True
            else:
                return False

Функция проверяет ТОЛЬКО первый элемент списка и сразу возвращает
результат. Цикл фактически выполняется один раз.

Сложность: O(1) — константная.
"""

import time
import matplotlib.pyplot as plt


def foo(nums):
    """Исходная (некорректная) реализация из задания."""
    for x in nums:
        if x % 2 == 0:
            return True
        else:
            return False


def foo_correct(nums):
    """Корректная версия: есть ли в списке хотя бы один чётный элемент.
    Сложность: лучший случай O(1), худший O(n)."""
    for x in nums:
        if x % 2 == 0:
            return True
    return False


def benchmark(func, sizes, reps=1000):
    times = []
    for n in sizes:
        data = list(range(1, 2 * n, 2))  
        start = time.perf_counter()
        for _ in range(reps):
            func(data)
        end = time.perf_counter()
        times.append((end - start) / reps)
    return times


def plot(sizes, times, title, filename):
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, times, marker='o', linewidth=2)
    plt.xlabel('Размер входных данных N')
    plt.ylabel('Время выполнения, с')
    plt.title(title)
    plt.xscale('log')
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.show()


if __name__ == '__main__':
    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

    t_foo = benchmark(foo, sizes, reps=1000)
    t_foo_correct = benchmark(foo_correct, sizes, reps=100)

    plot(
        sizes, t_foo,
        'Задание 1 (вар. 5): время работы foo() — O(1)',
        'task1_foo.png'
    )

    plot(
        sizes, t_foo_correct,
        'Задание 1 (вар. 5): корректная версия — O(n) в худшем случае',
        'task1_foo_correct.png'
    )

    print('Готово. Графики сохранены в task1_foo.png и task1_foo_correct.png')
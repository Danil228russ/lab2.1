"""
Задание 2, вариант 5.

Дана строка. Определить, какая буква встречается чаще всего.

Алгоритм 1: подсчёт через словарь (Counter) — O(n).
Алгоритм 2: наивный перебор с s.count() — O(n^2).
"""

import random
import string
import time
import matplotlib.pyplot as plt
from collections import Counter

def most_frequent_dict(s: str):
    if not s:
        return None
    counts = Counter(s)
    return counts.most_common(1)[0][0]

def most_frequent_naive(s: str):
    if not s:
        return None
    max_char = s[0]
    max_count = 0
    for ch in s:
        cnt = s.count(ch)          # O(n)
        if cnt > max_count:
            max_count = cnt
            max_char = ch
    return max_char


def benchmark(func, sizes, reps=10):
    times = []
    for n in sizes:
        s = ''.join(random.choices(string.ascii_lowercase, k=n))
        start = time.perf_counter()
        for _ in range(reps):
            func(s)
        end = time.perf_counter()
        times.append((end - start) / reps)
    return times


def plot(sizes, t1, t2, filename):
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, t1, marker='o', linewidth=2, label='Словарь (Counter) — O(n)')
    plt.plot(sizes, t2, marker='s', linewidth=2, label='Наивный s.count() — O(n²)')
    plt.xlabel('Длина строки N')
    plt.ylabel('Время выполнения, с')
    plt.title('Задание 2 (вар. 5): поиск самой частой буквы')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.show()


if __name__ == '__main__':
    sizes = [100, 500, 1_000, 2_000, 5_000, 10_000]

    t_dict = benchmark(most_frequent_dict, sizes, reps=20)
    t_naive = benchmark(most_frequent_naive, sizes, reps=3)

    plot(sizes, t_dict, t_naive, 'task2_comparison.png')

    test = "abracadabra"
    print(f"Строка: {test!r}")
    print(f"Словарь:  {most_frequent_dict(test)}")
    print(f"Наивный:  {most_frequent_naive(test)}")
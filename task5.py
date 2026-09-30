"""
Задание 5.

Сравнение производительности оператора in для множеств и списков.
- x in list -> O(n)
- x in set  -> O(1) в среднем
"""

import time
import matplotlib.pyplot as plt


def time_in_list(n, reps):
    lst = list(range(n))
    target = n - 1  
    start = time.perf_counter()
    for _ in range(reps):
        _ = target in lst
    return (time.perf_counter() - start) / reps


def time_in_set(n, reps):
    s = set(range(n))
    target = n - 1
    start = time.perf_counter()
    for _ in range(reps):
        _ = target in s
    return (time.perf_counter() - start) / reps


if __name__ == '__main__':
    sizes = [1_000, 10_000, 100_000, 1_000_000, 5_000_000]
    t_list, t_set = [], []

    for n in sizes:
        reps = 1000 if n <= 100_000 else 100
        t_list.append(time_in_list(n, reps))
        t_set.append(time_in_set(n, reps))

    plt.figure(figsize=(9, 5))
    plt.plot(sizes, t_list, marker='o', linewidth=2, label='x in list — O(n)')
    plt.plot(sizes, t_set, marker='s', linewidth=2, label='x in set  — O(1)')
    plt.xlabel('Размер коллекции N')
    plt.ylabel('Время выполнения, с')
    plt.title('Задание 5: оператор in для списка и множества')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('task5.png', dpi=150)
    plt.show()

    for n, tl, ts in zip(sizes, t_list, t_set):
        print(f"N={n:>9}: list={tl:.3e} c, set={ts:.3e} c")
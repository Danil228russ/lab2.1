"""
Задание 4.

Сравнение производительности оператора del для списков и словарей.
- del list[i]  -> O(n) (сдвиг элементов)
- del dict[k]  -> O(1) в среднем (хэш-таблица)
"""

import time
import matplotlib.pyplot as plt


def time_del_list(n, reps):
    total = 0.0
    for _ in range(reps):
        lst = list(range(n))
        start = time.perf_counter()
        del lst[n // 2]
        total += time.perf_counter() - start
    return total / reps


def time_del_dict(n, reps):
    total = 0.0
    for _ in range(reps):
        d = {i: i for i in range(n)}
        start = time.perf_counter()
        del d[n // 2]
        total += time.perf_counter() - start
    return total / reps


if __name__ == '__main__':
    sizes = [1_000, 10_000, 100_000, 1_000_000, 5_000_000]
    t_list, t_dict = [], []

    for n in sizes:
        reps = 200 if n <= 100_000 else 20
        t_list.append(time_del_list(n, reps))
        t_dict.append(time_del_dict(n, reps))

    plt.figure(figsize=(9, 5))
    plt.plot(sizes, t_list, marker='o', linewidth=2, label='del list[i]  — O(n)')
    plt.plot(sizes, t_dict, marker='s', linewidth=2, label='del dict[k]  — O(1)')
    plt.xlabel('Размер коллекции N')
    plt.ylabel('Время выполнения, с')
    plt.title('Задание 4: del для списка и словаря')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('task4.png', dpi=150)
    plt.show()

    for n, tl, td in zip(sizes, t_list, t_dict):
        print(f"N={n:>9}: list={tl:.3e} c, dict={td:.3e} c")
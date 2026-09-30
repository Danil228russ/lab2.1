"""
Задание 3.

T1(N) = N^2 - N - 10
T2(N) = 4N + 40

Приравниваем: N^2 - N - 10 = 4N + 40
              N^2 - 5N - 50 = 0
              D = 25 + 200 = 225
              N1 = 10, N2 = -5 (отбрасываем)

Ответ: N = 10.
"""

import numpy as np
import matplotlib.pyplot as plt


def T1(N):
    return N**2 - N - 10


def T2(N):
    return 4*N + 40


if __name__ == '__main__':
    
    coeffs = [1, -5, -50]
    roots = np.roots(coeffs)
    print(f"Корни уравнения: {roots}")
    N = int(round(max(roots.real)))
    print(f"N = {N}")
    print(f"T1({N}) = {T1(N)}")
    print(f"T2({N}) = {T2(N)}")

    xs = np.arange(0, 25)
    plt.figure(figsize=(9, 5))
    plt.plot(xs, T1(xs), marker='o', label='T1(N) = N² − N − 10')
    plt.plot(xs, T2(xs), marker='s', label='T2(N) = 4N + 40')
    plt.axvline(N, color='red', linestyle='--', alpha=0.6, label=f'N = {N}')
    plt.scatter([N], [T1(N)], color='red', zorder=5)
    plt.xlabel('N')
    plt.ylabel('Число операций')
    plt.title('Задание 3: точка равенства T1(N) = T2(N)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('task3.png', dpi=150)
    plt.show()
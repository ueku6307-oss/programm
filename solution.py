import sys


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    p = int(data[0])

    # Периметр квадрата: P = 4a, поэтому сторона a = P // 4.
    # По условию сторона — натуральное число, значит P кратно 4 нацело.
    a = p // 4

    # Площадь: S = a * a.
    # В C++ здесь нужен long long: при P = 1e9 -> S = 6.25e16.
    # В Python целые числа не переполняются.
    s = a * a

    print(s)


if __name__ == "__main__":
    main()

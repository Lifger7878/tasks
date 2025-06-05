# Завдання 1: Зворотній рядок
# Головна рекурсія
def reverse_string_main(s):
    if s == "":
        return ""
    return reverse_string_main(s[1:]) + s[0]

# Хвостова рекурсія
def reverse_string_tail(s, acc=""):
    if s == "":
        return acc
    return reverse_string_tail(s[1:], s[0] + acc)


# Завдання 2: Обмін пар у зв'язаному списку
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Головна рекурсія
def swap_pairs_main(head):
    if not head or not head.next:
        return head
    first = head
    second = head.next
    first.next = swap_pairs_main(second.next)
    second.next = first
    return second

# Хвостова рекурсія (через допоміжну функцію)
def swap_pairs_tail(head):
    def helper(prev, curr):
        if not curr or not curr.next:
            return head if prev is None else head
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = curr
        if prev:
            prev.next = nxt
        return helper(curr, curr.next)
    return helper(None, head)


# Завдання 3: Числа Фібоначчі
# Головна рекурсія
def fib_main(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_main(n-1) + fib_main(n-2)

# Хвостова рекурсія
def fib_tail(n, a=0, b=1):
    if n == 0:
        return a
    return fib_tail(n-1, b, a + b)


# Завдання 4: Кількість шляхів по сходах
# Головна рекурсія
def climb_stairs_main(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return climb_stairs_main(n-1) + climb_stairs_main(n-2)

# Хвостова рекурсія
def climb_stairs_tail(n, a=1, b=1):
    if n == 0:
        return a
    return climb_stairs_tail(n-1, b, a + b)


# Завдання 5: Піднесення до степеня
# Головна рекурсія
def my_pow_main(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow_main(x, -n)
    half = my_pow_main(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x

# Хвостова рекурсія
def my_pow_tail(x, n, acc=1):
    if n == 0:
        return acc
    if n < 0:
        return my_pow_tail(1 / x, -n, acc)
    if n % 2 == 0:
        return my_pow_tail(x * x, n // 2, acc)
    else:
        return my_pow_tail(x, n - 1, acc * x)


# Інтерфейс командного рядка
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    while True:
        print("\nОберіть завдання:")
        print("1 - Розвернути рядок")
        print("2 - Обмін пар у зв'язаному списку")
        print("3 - Обчислення числа Фібоначчі")
        print("4 - Кількість шляхів сходами")
        print("5 - Піднесення до степеня")
        print("0 - Вийти")
        choice = input("Ваш вибір: ")

        if choice == "0":
            break
        elif choice == "1":
            s = input("Введіть рядок: ")
            print("Головна рекурсія:", reverse_string_main(s))
            print("Хвостова рекурсія:", reverse_string_tail(s))
        elif choice == "2":
            raw = input("Введіть список чисел через пробіл: ").split()
            dummy = ListNode(0)
            current = dummy
            for num in raw:
                current.next = ListNode(int(num))
                current = current.next
            print("Головна рекурсія:", end=" ")
            print_list(swap_pairs_main(dummy.next))
            # Повторно створимо список для хвостової
            dummy = ListNode(0)
            current = dummy
            for num in raw:
                current.next = ListNode(int(num))
                current = current.next
            print("Хвостова рекурсія:", end=" ")
            print_list(swap_pairs_tail(dummy.next))
        elif choice == "3":
            n = int(input("Введіть n: "))
            print("Головна рекурсія:", fib_main(n))
            print("Хвостова рекурсія:", fib_tail(n))
        elif choice == "4":
            n = int(input("Скільки сходинок: "))
            print("Головна рекурсія:", climb_stairs_main(n))
            print("Хвостова рекурсія:", climb_stairs_tail(n))
        elif choice == "5":
            x = float(input("x = "))
            n = int(input("n = "))
            print("Головна рекурсія:", my_pow_main(x, n))
            print("Хвостова рекурсія:", my_pow_tail(x, n))
        else:
            print("Невірний вибір. Спробуйте ще раз.")

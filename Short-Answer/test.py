def test(n):
    sum = 0  # O(1)
    for i in range(n):  # O(n)
        j = 1  # 0(1)
        while j < n:  # 0(n)
            j *= 2 #O(1)
            sum += 1 #O(1)

print(test(5))

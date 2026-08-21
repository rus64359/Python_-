def year(n):
    return f"Год {n} Высокосный?: {n % 4 == 0}"


print(year(2026))
print(year(2020))
print(year(2030))
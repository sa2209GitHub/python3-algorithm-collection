# Алгоритм Эвклида
# Найти наибольший общий делитель для a и b

def gcd(a, b):
    """Возвращает наибольший общий делитель для A и B"""

    while b != 0:
        reminder = int(a % b)
        a = b
        b = reminder
    return a

# ----------------------
print(gcd.__doc__, ":", gcd(200, 120))
print(gcd.__doc__, ":", gcd(160, 132))
print(gcd.__doc__, ":", gcd(200, 100))
print(gcd.__doc__, ":", gcd(13, 4))

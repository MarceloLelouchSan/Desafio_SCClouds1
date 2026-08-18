def fibonacci_recursivo(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("O parâmetro n deve ser inteiro maior ou igual a zero (N >= 0).")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_linear(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("O parâmetro n deve ser inteiro maior ou igual a zero (N >= 0).") 

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b 
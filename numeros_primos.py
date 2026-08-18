def se_primo_recursivo(numero: int, divisor: int = 2) -> bool:
    #Função criada para checar se um número é primo.
    if divisor * divisor > numero:
        return True
    if numero % divisor == 0:
        return False
    return se_primo_recursivo(numero, divisor + 1)

def primos_recursivo(n: int) -> list:
    if not isinstance(n, int) or n <= 1:
        raise ValueError("O parâmetro N deve ser inteiro maior que 1 (N > 1).")
    
    if n == 2:
        return [2]
    
    lista_primos = primos_recursivo(n - 1)
    
    if se_primo_recursivo(n):
        lista_primos.append(n)
        
    return lista_primos

def primos_linear(n: int) -> list:
    if not isinstance(n, int) or n <= 1:
        raise ValueError("O parâmetro N deve ser inteiro maior que 1 (N > 1).")
        
    primos = []
    
    for num in range(2, n + 1):
        eh_primo = True
        divisor = 2
        
        while divisor * divisor <= num:
            if num % divisor == 0:
                eh_primo = False
                break  
            divisor += 1
            
        if eh_primo:
            primos.append(num)
            
    return primos
def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

#Приймання данних від користувача
def main():
    try:
        fib = caching_fibonacci()
        u_input = int(input("ВВедіть число Фібоначчі: "))
        result = fib(u_input)
        print(f"Число Фібоначчі {u_input} це {result}")

    except ValueError:
        print("Помилка!\nВведіть ціле значення.")

if __name__ == "__main__":
    main()



import time


def excec_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(
            f"La función {func.__name__} tardó {total_time:.2f} segundos en ejecutarse."
        )
        return result

    return wrapper


@excec_time
def test_funcions(n):
    value = 0
    for i in range(1, n + 1):
        value += i

    time.sleep(2.5)
    return value


# Ejemplo de uso
test_funcions(100)
